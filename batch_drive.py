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
        server = subprocess.Popen(["torcs", "-t 1000000000", "-r", fullpath + "/configs/" + str(port) + ".xml"])
    else:
        server = subprocess.Popen(["torcs",  fullpath + "/configs/" + str(port) + ".xml"])
    call_agent = ["python", "snakeoil.py"]
    port = ["-p", str(port)]
    parameters = map(str, parameters)
    call_agent.extend(port)
    call_agent.extend(parameters)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    subprocess.check_call(call_agent)
    server.kill()
    server.kill()
    server.kill()
    server.kill()
    server.kill()
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
    races = [2,4,5,6,7,8]
    placing = [-1,-1,-1,-1,-1,-1,-1,-1]
    for race in range(6):
        for place in range(2):
            #print str(root[races[race]][1][0][1][place][0].attrib.get("val"))
            if root[races[race]][1][0][1][place][0].attrib.get("val") in ("scr_server 1", "scr_server 2", "scr_server 3", "scr_server 4", "scr_server 5", "scr_server 6", "scr_server 7", "scr_server 8", "scr_server 9", "scr_server 10", "scr_server 11"):
               placing[race] = place
               #print "inif: "+str(root[races[race]][1][0][1][place][0].attrib.get("val"))+" place: "+str(place)
    time1 = root[2][1][0][1][placing[0]][4].attrib.get("val")
    time2 = root[4][1][0][1][placing[1]][4].attrib.get("val")
    time3 = root[5][1][0][1][placing[2]][4].attrib.get("val")
    time4 = root[6][1][0][1][placing[3]][4].attrib.get("val")
    time5 = root[7][1][0][1][placing[4]][4].attrib.get("val")
    time6 = root[8][1][0][1][placing[5]][4].attrib.get("val")

    penalty_time1 = root[2][1][0][1][placing[0]][5].attrib.get("val")
    penalty_time2 = root[4][1][0][1][placing[1]][5].attrib.get("val")
    penalty_time3 = root[5][1][0][1][placing[2]][5].attrib.get("val")
    penalty_time4 = root[6][1][0][1][placing[3]][5].attrib.get("val")
    penalty_time5 = root[7][1][0][1][placing[4]][5].attrib.get("val")
    penalty_time6 = root[8][1][0][1][placing[5]][5].attrib.get("val")

    damage1=root[2][1][0][1][placing[0]][8].attrib.get("val")
    damage2=root[4][1][0][1][placing[1]][8].attrib.get("val")
    damage3=root[5][1][0][1][placing[2]][8].attrib.get("val")
    damage4=root[6][1][0][1][placing[3]][8].attrib.get("val")
    damage5=root[7][1][0][1][placing[4]][8].attrib.get("val")
    damage6=root[8][1][0][1][placing[5]][8].attrib.get("val")

    p1=abs(float(time1) - float(penalty_time1) > EPSILON)
    p2=abs(float(time2) - float(penalty_time2) > EPSILON)
    p3=abs(float(time3) - float(penalty_time3) > EPSILON)
    p4=abs(float(time4) - float(penalty_time4) > EPSILON)
    p5=abs(float(time5) - float(penalty_time5) > EPSILON)
    p6=abs(float(time6) - float(penalty_time6) > EPSILON)
    print "p1: "+str(p1)

    print "total:"+str(float(time1)+float(time2)+float(time3)+float(time4)+float(time5)+float(time6))+"time1: "+str(time1)+" time2: "+str(time2)+" time3: "+str(time3)+" time4: "+str(time4)+" time5: "+str(time5)+" time6: "+str(time6)+" parameters: "+str(parameters)


    #print "now time1: "+str(float(time1))+" Port: "+str(port)
    #print "now time2: "+str(float(time2))+" Port: "+str(port)


    # Check whether the lap was actually finished and verify lap time
    #if laps > 0 and (float(time) - float(best_lap_time) < EPSILON):
    if (float(damage1)<10000.0) and  (float(damage2)<10000.0) and  (float(damage3)<10000.0) and (float(damage4) < 10000.0) and (float(damage5) < 10000.0)and (float(damage6)<10000.0):
        if float(time1)==0.0 or float(time2)==0.0or float(time3)==0.0:
            time = -1
        elif laps > 0 and p1 and p2 and p3 and p4 and p5 and p6 and ((float(time1)+float(time2)+float(time3)+float(time4)+float(time5)+float(time6))>100.0):
           time = float(time1)+float(time2)+float(time3)+float(time4)+float(time5)+float(time6)
           #print "now timeX: "+str(time)
        else:
            time = -1
    else:
        time=-1
        print "to much damage. track 1: "+str(float(root[2][1][0][1][placing[0]][8].attrib.get("val")))
        print "to much damage. track 2: "+str(float(root[4][1][0][1][placing[0]][8].attrib.get("val")))
    return time

def main():
    rep_length = 9
    popsize =18
    sp = 3
    mut = 1./rep_length
    cross = 0.95
    maxgen = 100
    onlyThebest = 0
    run_id = "1"
    nr_processes =5
    fullpath = os.path.abspath(".")
    for runval in range(31, 1000):
        print "run "+str(runval)
        optimizer = GA.gax(rep_length = rep_length, popsize = popsize, sp = sp, mut = mut, fitfun = evaluation, maxgen = maxgen, cross = cross, nr_processes = nr_processes, run_id = run_id, path = fullpath,onlyThebest=onlyThebest, runval=runval)
        optimizer.run()
        bashCommand = "killall torcs-bin"
        os.system(bashCommand)
        print "killed old torcs processes"

if __name__ == "__main__":
    main()
