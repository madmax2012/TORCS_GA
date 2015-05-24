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
        self.tournamentSize=sp
        self.crossoverChance = cross
        self.debug=1

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
        self.tempArray = [i for i in range(len(self.cars))]
        self.getFitnessValues()
   #     print "printing all fitnesses"
    #    self.printFitnessArray()
    #    print "\n\n"
    #    self.returnFittest()
     #   print "fittest at: "+str(self.returnFittest())
  #      print "it's values: "+str(self.returnFittestValues())


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
        for replacer in range (len(self.cars)):
           # self.numberOfElites = (int((1-self.crossoverChance)*self.popsize))+1
           # if  replacer < self.numberOfElites: ##keep the elites
           #     self.tempArray.append(self.cars[self.returnFittest()])
           #     pass
           # else:
            for i in range(0,self.tournamentSize):##select parents in tournament
               # print "TMMMMMMMMMMMMMMMMM"
                self.parent1 = np.empty
                self.parent2 = np.empty
                self.randomPos = random.randint(0, len(self.fitArray)-1)
                while(self.fitArray[self.randomPos] == -1):
                    #print "-1.. get a new one"
                    self.randomPos = random.randint(0, len(self.fitArray)-1)
                if self.parent1==np.empty:
                    self.parent1=self.randomPos
                    #self.parent2=self.parent1
                    #print "our first parents are"+str(self.fitArray[self.parent1])+"  and  "+str(self.fitArray[self.parent2])+""
                elif self.fitArray[self.randomPos] < self.fitArray[self.parent1]:
                    if self.fitArray[self.randomPos] == -1:
                        #print "-1 is no legit parent"
                        pass
                    else:
                        #print "tm: "+str(self.fitArray[self.randomPos])+"  is smaller than  "+str(self.fitArray[self.parent1])+""
                        #self.parent2=self.parent1
                        self.parent1=self.randomPos
                self.randomPos = random.randint(0, len(self.fitArray)-1)
                while(self.fitArray[self.randomPos] == -1):
                   # print "-1.. get a new one"
                    self.randomPos = random.randint(0, len(self.fitArray)-1)
                if self.parent2==np.empty:
                    self.parent2=self.randomPos
                elif self.fitArray[self.randomPos] < self.fitArray[self.parent2]:
                    if self.fitArray[self.randomPos] == -1:
                       # print "-1 is no legit parent"
                        pass
                    else:
                        self.parent2=self.randomPos
            #print "now our parents are:"+str(self.fitArray[self.parent1])+"  and  "+str(self.fitArray[self.parent2])+""


            ### "crossover"
            #print "parent1: "+str(self.cars[self.parent1].getParameters())+" has the fitness value "+str(self.fitArray[self.parent1])+""
            #print "parent2: "+str(self.cars[self.parent2].getParameters())+" has the fitness value "+str(self.fitArray[self.parent2])+""
            self.tempArray[replacer]=individual.individual(self.cars[self.parent1].values[0],self.cars[self.parent2].values[1], self.cars[self.parent1].values[2], self.cars[self.parent2].values[3], self.cars[self.parent1].values[4], self.cars[self.parent2].values[5], self.cars[self.parent1].values[6], self.cars[self.parent2].values[7],self.cars[self.parent1].values[8] )
            #print "child 1 is:"+str(self.tempArray[replacer].getParameters())
            #self.printPop()
            #print "value0: "+str(self.cars[0].values[0])

        for i in range(len(self.cars)):
            self.cars[i] = self.tempArray[i]
        print "fittest at: "+str(self.returnFittest())
        print "it's values: "+str(self.returnFittestValues())

        self.currentIteration=self.currentIteration+1
        if self.currentIteration >= self.maxIterations:
            self.stop_reached = True




##fittest at: 12
##it's values: ['190.277074091', '0.362349985495', '9.02742820427', '0.285502127651', '55.2049926684', '0.844332584546', '0.0843421917131', '6.82010070771', '0.966949879827']



    def stop(self):
        return self.stop_reached
        pass

    def printPop(self):
        for i in range (len(self.cars)):
                 print self.cars[i].getParameters()
                 pass

    def getFitnessValues(self):
        self.fitArray = []
        if self.debug == 1:
             self.fitArray.append(550.0)
             self.fitArray.append(500.0)
             self.fitArray.append(123.0)
             self.fitArray.append(144.0)
             self.fitArray.append(132.0)
             self.fitArray.append(234.0)
             self.fitArray.append(432.0)
             self.fitArray.append(265.0)
             self.fitArray.append(199.0)
             self.fitArray.append(333.0)
        else:
            for i in range(len(self.cars)):
                self.fitArray.append(self.fitfun(self.cars[i].getParameters(), 2))

    def printFitnessArray(self):
        if self.fitArray == []:
            print "No fitness values collected, yet"
        else:
            for i in range(len(self.fitArray)):
                print self.fitArray[i]

    def returnFittest(self):
        leader=np.empty
        for i in range(len(self.fitArray)):
            #print "i am here"
            if leader == np.empty:
                leader = i
            elif self.fitArray[i]<self.fitArray[leader]:
                if self.fitArray[i] == -1:
                    pass
                else:
                    #print str(self.fitArray[i])+" is smaller than "+str(self.fitArray[leader])
                    leader = i
        return leader

    def returnFittestValues(self):
        return self.cars[self.returnFittest()].getParameters()



