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
        tempArray = []
        self.getFitnessValues()
        print "printing all fitnesses"
        self.printFitnessArray()
        print "fittest at: "+str(self.returnFittest())
        print "it's values: "+str(self.printFittestValues())


        '''keep for parallel function
        foos = [self.cars[0].getParameters(),["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"],["100","0.05","10","0.10","50","0.01","0.01","5", "0.2"]]
        bars = [1,2,3]
        def maptest(foo):
            #print foo
            print"\n\n\n"
            print self.fitfun(foo, (self.nr_processes-self.nr_processes)+self.currentIteration)
            print"\n\n\n"

        map(maptest, foos)


        for replacer in range (len(self.population)):
            self.parent1 = np.empty
            self.parent2 = np.empty
            self.numberOfElites = (int((1-self.crossoverChance)*self.popsize))+1
            if  replacer < self.numberOfElites: ##keep the elites
                self.tempArray.append(self.population[self.returnBestIndividualPOS()])
                pass
            else:
                for i in range(0,self.tournamentSize):##select parents in tournament
                    self.randomParentCandidate = self.population[random.randint(0, len(self.population)-1)]
                    if self.parent1==np.empty:
                        self.parent1=self.randomParentCandidate
                        self.parent2=self.parent1
                    elif (self.getCityFitness(self.city_coordinates, self.parent1.position)) > (self.getCityFitness(self.city_coordinates, self.randomParentCandidate.position)):
                        self.parent2=self.parent1
                        self.parent1=self.randomParentCandidate

        '''
        self.printPop()
        print "collecting now"
        #print "value0: "+str(self.cars[0].values[0])

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
        if self.fitArra y== []:
            print "No fitness values collected, yet"
        else:
            for i in range(len(self.fitArray)):
                print self.fitArray[i]

    def returnFittest(self):
        leader =99999
        if self.fitArray == []:
            self.getFitnessValues()
        for i in range(len(self.fitArray)):
            if leader == 99999:
                leader = i
            elif i<leader:
                leader = i
        return leader

    def printFittestValues(self):
        print self.cars[self.returnFittest()].getParameters()



