#!/usr/bin/env python

import os
import subprocess
import glob
import xml.etree.ElementTree as ET
import GA
import signal
import time
import csv
import random
import logging
import operator
import shutil
import glob
import pprocess
EPSILON = 0.000001

def evaluation(parameters, ind):
    # Evaluation function is passed to the GA
    # Takes phenotype as parameters and port_id (=individual id, int) for parallel processing

    fullpath = os.path.abspath(".")
    port = 3000 + ind + 1
    guiless=1
    if (guiless==1):
        server = subprocess.Popen(["torcs", "-t 10000", "-r", fullpath + "/configs/" + str(port) + ".xml"])
    else:
        server = subprocess.Popen(["torcs", "-nodamage", fullpath + "/configs/" + str(port) + ".xml"])
    call_agent = ["python", "snakeoil.py"]
    port = ["-p", str(port)]
    parameters = map(str, parameters)
    call_agent.extend(port)
    call_agent.extend(parameters)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    server.kill()

    # Gather data and parse
    result_file = "/home/max/.torcs/results/"+ str(port[1]) +"/*.xml"
    newest = max(glob.iglob(result_file), key = os.path.getctime)
    tree = ET.parse(newest)
    root = tree.getroot()

    # Read times, laps info from disk
    laps = root[2][1][0][1][0][3].attrib.get("val")
    time = root[2][1][0][1][0][4].attrib.get("val")
    penalty_time = root[2][1][0][1][0][5].attrib.get("val")
    best_lap_time = root[2][1][0][1][0][6].attrib.get("val")


    races = [2,4,5]
    placing = [-1,-1,-1,-1,-1]
    for race in range(2):
        for place in range(1):
            if root[races[race]][1][0][1][place][0].attrib.get("val") == "scr_server 1":
               placing[race] = place

    time1 = root[2][1][0][1][placing[0]][4].attrib.get("val")
    time2 = root[4][1][0][1][placing[1]][4].attrib.get("val")


    # Check whether the lap was actually finished and verify lap time
    #if laps > 0 and (float(time) - float(best_lap_time) < EPSILON):
    if laps > 0 and abs(float(time) - float(penalty_time) > EPSILON):
       time = float(time1)+float(time2)
    else:
        time = -1
    return time

def main():
    rep_length = 9
    popsize = 10
    sp = 3
    mut = 1./rep_length
    cross = 0.95
    maxgen = 20
    onlyThebest = 0
    run_id = "1"
    #debug =1

    # set max threads for evaluation
    nr_processes = 10
    fullpath = os.path.abspath(".")
    for runval in range(1000):
        print "run "+str(runval)
        optimizer = GA.gax(rep_length = rep_length, popsize = popsize, sp = sp, mut = mut, fitfun = evaluation, maxgen = maxgen, cross = cross, nr_processes = nr_processes, run_id = run_id, path = fullpath,onlyThebest=onlyThebest, runval=runval)
        optimizer.run()

if __name__ == "__main__":
    main()
