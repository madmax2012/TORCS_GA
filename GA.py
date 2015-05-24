#!/usr/bin/env python
import sys
import os
import time
import csv
import random
import logging
import operator
import shutil
import glob
import matplotlib.pyplot as plt
import  math
import individual
import batch_drive
#from datashape.coretypes import String

import numpy as np

class RunGA():
    def __init__(self,rep_length, popsize, sp, mut, fitfun, maxgen, cross, nr_processes, run_id , path):

        self.nr_processes = nr_processes
        self.currentIteration=0
        self.fitfun =fitfun
        self.maxIterations=maxgen


        pass

    def step(self):
        pass

    def stop(self):
        pass



    def run(self):
        while True:
            self.step()
            if self.stop():
                break
        return

    def get_current_iteration(self):
        return self.current_iteration

class gax(RunGA):
    def __init__(self, *args, **kwargs):
        RunGA.__init__(self, *args,**kwargs)
        print("dfg")
        print ""+str(self.nr_processes)
        self.stop_reached = False

    def step(self):
        # Simple stopping condition
       # self.current_iteration = self.current_iteration + 1
       # if self.current_iteration >= self.max_iterations:
       #     self.stop_reached = True
        print "nb of processes: "+str(self.nr_processes)
        print "iteration:        "+str(self.currentIteration)




        print self.fitfun(["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"], (self.nr_processes-self.nr_processes)+self.currentIteration)




        self.currentIteration=self.currentIteration+1
        if self.currentIteration >= self.maxIterations:
            self.stop_reached = True
