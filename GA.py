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
#import matplotlib.pyplot as plt
import  math
import individual
#import pprocess
#from joblib import Parallel, delayed
#import multiprocessing

#from datashape.coretypes import String
#import numpy as np

class RunGA():
    def __init__(self, rep_length, popsize, sp, mut, fitfun, maxgen, cross, nr_processes, run_id , path, onlyThebest):

        self.nr_processes = nr_processes
        self.currentIteration=0
        self.fitfun =fitfun
        self.maxIterations=maxgen
        self.popsize=popsize
        self.cars = []
        self.fitArray = []
        self.onlyTheBest = onlyThebest
        if self.onlyTheBest == 0:
            for i in range(self.popsize):
                self.cars.append(individual.individual(random.uniform(0,200), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1)))

        if self.onlyTheBest == 1:
            print "runing the best three agents"
            self.cars.append(individual.individual('177.252500534', '0.192081339496', '13.8485509463', '0.174913216207', '43.6777054637', '0.739736950556', '0.606430928903', '1.37505237389', '0.392079630538'))
            self.cars.append(individual.individual('182.982132289', '0.480256960754', '17.871674573', '0.19948437725', '81.026873882', '0.368079019305', '0.774779060289', '7.9373501551', '0.165187675688'))
            self.cars.append(individual.individual('192.982132289', '0.480256960754', '17.871674573', '0.19948437725', '81.026873882', '0.368079019305', '0.774779060289', '7.9373501551', '0.165187675688'))
        self.tournamentSize=sp
        self.crossoverChance = cross
        self.debug=0
        self.mutationChance = mut

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
            self.numberOfElites = (int((1-self.crossoverChance)*self.popsize))+1
            #print self.numberOfElites
            if  replacer < self.numberOfElites: ##keep the elites
                #self.tempArray.append(self.cars[self.returnFittest()])
                # print self.cars[self.returnFittest()].getParameters()
                self.tempArray[replacer] = self.cars[self.returnFittest()]
                pass
            else:
                for i in range(0,self.tournamentSize):##select parents in tournament
                   # print "TMMMMMMMMMMMMMMMMM"
                    self.parent1 = 9999999
                    self.parent2 = 9999999
                    self.randomPos = random.randint(0, len(self.fitArray)-1)
                    while(self.fitArray[self.randomPos] == -1):
                        #print "-1.. get a new one"
                        self.randomPos = random.randint(0, len(self.fitArray)-1)
                    if self.parent1==9999999:
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
                    if self.parent2==9999999:
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
        #write fittest back
        for i in range(len(self.cars)):
            self.cars[i] = self.tempArray[i]

        for i in range(self.numberOfElites, len(self.cars)):
            for gene in range(9):
                if (random.uniform(0, 1) <= self.mutationChance):
                   #print "gene "+str(gene)+" is: "+str(self.cars[i].values[gene])
                   #print "param "+str(gene)+" is: "+str(self.cars[i].parameters[gene])
                   muval = self.cars[i].values[gene] * random.uniform(-0.1,0.1)
                   self.cars[i].values[gene] = self.cars[i].values[gene] + muval
                   self.cars[i].parameters[gene] = str(float(self.cars[i].parameters[gene]) + muval)
                   #print "now gene "+str(gene)+" is: "+str(self.cars[i].values[gene])
                   #print "now param "+str(gene)+" is: "+str(self.cars[i].parameters[gene])
                   pass

        print "generation:   "+str(self.currentIteration)
        print "fittest at:   "+str(self.returnFittest())+"  its fitness: "+str(self.returnFittestFitness())
        print "it's values:  "+str(self.returnFittestValues())
        print "fitnessarray: "+str(self.fitArray)
        print"\n\n"

        f = open("test.txt","a") #opens file with name of "test.txt"
        f.write("generation:   "+str(self.currentIteration)+"\n")
        f.write("fittest at:   "+str(self.returnFittest())+"  its fitness: "+str(self.returnFittestFitness())+"\n")
        f.write("it's values:  "+str(self.returnFittestValues())+"\n")
        f.write("fitnessarray: "+str(self.fitArray)+"\n")
        f.close

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
        #print "making fitness"
        self.fitArray =  [i for i in range(len(self.cars))]
        if self.debug == 1:
             for i in range(len(self.fitArray)):
                 self.fitArray[i]= random.uniform(50,500)
        else:
           for i in range(len(self.cars)):
               self.fitArray[i] = self.fitfun(self.cars[i].getParameters(), 2)

    def commented(self):
        '''
from joblib import Parallel, delayed
import multiprocessing

# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)
def processInput(i):
    return i * i

num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)





for i in inputs
    results[i] = processInput(i)
end
// now do something with results

'''

    def printFitnessArray(self):
        if self.fitArray == []:
            print "No fitness values collected, yet"
        else:
            for i in range(len(self.fitArray)):
                print self.fitArray[i]

    def returnFittest(self):
        leader=1000
        for i in range(len(self.fitArray)):
            #print "i am here"
          #  print self.fitArray[i]
            if leader == 1000:
                leader = i
            elif self.fitArray[i] < self.fitArray[leader]:
                if self.fitArray[i] != -1:
                    leader = i

           # else:
           #     print "error"+str(self.fitArray[i])+" not smaller "+str(self.fitArray[leader])
        return leader

    def returnFittestValues(self):
        return self.cars[self.returnFittest()].getParameters()

    def returnFittestFitness(self):
        return self.fitArray[self.returnFittest()]
