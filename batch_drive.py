#!/usr/bin/env python

import os
import subprocess
import glob
import xml.etree.ElementTree as ET
import GA
import signal
import time

EPSILON = 0.000001

def evaluation(parameters, ind):
    # Evaluation function is passed to the GA
    # Takes phenotype as parameters and port_id (=individual id, int) for parallel processing

    fullpath = os.path.abspath(".")
    port = 3000 + ind + 1
    server = subprocess.Popen(["torcs", "-r", fullpath + "/configs/" + str(port) + ".xml"])
    call_agent = ["python", "snakeoil.py"]
    port = ["-p", str(port)]
    parameters = map(str, parameters)
    call_agent.extend(port)
    call_agent.extend(parameters)
    subprocess.call(call_agent)
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

    # Check whether the lap was actually finished and verify lap time
    #if laps > 0 and (float(time) - float(best_lap_time) < EPSILON):
    if laps > 0 and abs(float(time) - float(penalty_time) > EPSILON):
       time = float(time)
    else:
        time = -1
    return time

def main():
    rep_length = 9
    popsize = 15
    sp = 2
    mut = 1./rep_length
    cross = 1.0
    maxgen = 50
    run_id = "1"

    # set max threads for evaluation
    nr_processes = 8
    fullpath = os.path.abspath(".")
    optimizer = GA.gax(rep_length = rep_length, popsize = popsize, sp = sp, mut = mut, fitfun = evaluation, maxgen = maxgen, cross = cross, nr_processes = nr_processes, run_id = run_id, path = fullpath)
    optimizer.run()

if __name__ == "__main__":
    main()
