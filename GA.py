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
    def __init__(self, rep_length, popsize, sp, mut, fitfun, maxgen, cross, nr_processes, run_id , path):

        self.nr_processes = nr_processes
        self.currentIteration=0
        self.fitfun =fitfun
        self.maxIterations=maxgen
        self.popsize=popsize
        self.cars = []
        self.fitArray = []
        for i in range(self.popsize):
            self.cars.append(individual.individual(random.uniform(0,200), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1)))

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
        print ""+str(self.nr_processes)
        self.stop_reached = False


    def step(self):
        # Simple stopping condition
       # self.current_iteration = self.current_iteration + 1
       # if self.current_iteration >= self.max_iterations:
       #     self.stop_reached = True
        #print "nb of processes: "+str(self.nr_processes)
        #print "iteration:        "+str(self.currentIteration)


        '''keep for parallel function
        foos = [self.cars[0].getParameters(),["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"]]
        bars = [1,2,3]


        def maptest(foo):
            #print foo
            print"\n\n\n"
            print self.fitfun(foo, (self.nr_processes-self.nr_processes)+self.currentIteration)
            print"\n\n\n"

        map(maptest, foos)

        '''

        ##get all fitnesses


        self.printFitnessArray()
        print "collecting now"
        self.getFitnessValues()

        self.currentIteration=self.currentIteration+1
        if self.currentIteration >= self.maxIterations:
            print "stop"
            self.stop_reached = True





    def stop(self):
        return self.stop_reached
        pass

    def printPop(self):
        for i in range (len(self.cars)):
                 print self.cars[i].getParameters()
                 pass

    def getFitnessValues(self):
        self.fitArray = []
        for i in range(len(self.cars)):
            self.fitArray.append(self.fitfun(self.cars[i].getParameters(), 2))

    def printFitnessArray(self):
        if self.fitArray== []:
            print "No fitness values collected, yet"
        else:
            for i in range(len(self.fitArray)):
                print self.fitArray[i]


