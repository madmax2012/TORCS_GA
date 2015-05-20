#!/usr/bin/env python

import os
import subprocess
import glob
import xml.etree.ElementTree as ET
import ga
import signal
import time
import csv

EPSILON = 0.000001

def evaluation(parameters, ind):
    # Evaluation function is passed to the GA
    # Takes phenotype as parameters and port_id (=individual id, int) for parallel processing

    fullpath = os.path.abspath(".")
    port = 3000 + ind + 1
    server = subprocess.Popen(["torcs", fullpath + "/configs/" + str(port) + ".xml"])
    print "Starting agent"
    call_agent = ["python", "snakeoil.py"]
    port = ["-p", str(port)]
    parameters = map(str, parameters)
    call_agent.extend(port)
    call_agent.extend(parameters)
    subprocess.call(call_agent)
    server.kill()

    # Gather data and parse
    result_file = "/home/alex/.torcs/results/"+ str(port[1]) +"/*.xml"
    newest = max(glob.iglob(result_file), key = os.path.getctime)
    tree = ET.parse(newest)
    root = tree.getroot()

    # Read times, laps info from disk
    laps = root[2][1][0][1][0][3].attrib.get("val")
    time = root[2][1][0][1][0][4].attrib.get("val")
    #penalty_time = root[2][1][0][1][0][5].attrib.get("val")
    best_lap_time = root[2][1][0][1][0][6].attrib.get("val")

    # Check whether the lap was actually finished and verify lap time
    if laps > 0 and (float(time) - float(best_lap_time) < EPSILON):
        time = float(time)
    else:
        time = -1
    return time

def main():
    run_id = 1
    with open('test/' + 'run_best_ind_' + str(run_id) + '.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        lastline = reader.next()
        for line in reader:
            lastline = line
    parameters = lastline
    evaluation(parameters,0)


if __name__ == "__main__":
    main()
