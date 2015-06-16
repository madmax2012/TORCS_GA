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
import pprocess
#import matplotlib.pyplot as plt
import  math
import individual

class RunGA():
    def __init__(self, rep_length, popsize, sp, mut, fitfun, maxgen, cross, nr_processes, run_id , path, onlyThebest, runval):

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
                self.cars.append(individual.individual(random.uniform(50,150), random.uniform(0,0.1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,70), random.uniform(0,1), random.randint(5000,8000),random.uniform(0,1),random.uniform(50,110),random.uniform(50,110),random.uniform(5,15)))
        print len(self.cars)
        if self.onlyTheBest == 1:
            #total:1340.766s time1: 106.93 time2: 202.336 time3: 136.432 time4: 136.6 time5: 122.886 time6: 94.084 time7: 59.344 time8: 149.394 time9: 127.42 time10: 175.34 parameters:
            self.cars.append(individual.individual('154.897575174', '-0.0199', '-0.139884752072', '0.779904990626', '82.8097466274', '1.19039046912', '0.384730869454', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '49.7170137868', '17.9086116398'))
            self.cars.append(individual.individual('154.897575174', '-0.0199', '-0.139884752072', '0.779904990626', '82.8097466274', '0.971351422208', '0.246257782509', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '49.7170137868', '17.9086116398'))
        self.tournamentSize=sp
        self.crossoverChance = cross
        self.debug=0
        self.mutationChance = mut
        self.runval=runval

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
        for replacer in range (len(self.cars)):
            self.numberOfElites = (int((1-self.crossoverChance)*self.popsize))+2
            if  replacer < self.numberOfElites: ##keep the elites
                self.tempArray[replacer] = self.cars[self.returnFittest()]
                pass
            else:
                for i in range(0,self.tournamentSize):##select parents in tournament
                    self.parent1 = 9999999
                    self.parent2 = 9999999
                    self.randomPos = random.randint(0, len(self.fitArray)-1)
                    while(self.fitArray[self.randomPos] == -1):
                        #print "-1.. get a new one"
                        self.randomPos = random.randint(0, len(self.fitArray)-1)
                    if self.parent1==9999999:
                        self.parent1=self.randomPos
                    elif self.fitArray[self.randomPos] < self.fitArray[self.parent1]:
                        if self.fitArray[self.randomPos] == -1:
                            pass
                        else:
                            self.parent1=self.randomPos
                    self.randomPos = random.randint(0, len(self.fitArray)-1)
                    while(self.fitArray[self.randomPos] == -1):
                        self.randomPos = random.randint(0, len(self.fitArray)-1)
                    if self.parent2==9999999:
                        self.parent2=self.randomPos
                    elif self.fitArray[self.randomPos] < self.fitArray[self.parent2]:
                        if self.fitArray[self.randomPos] == -1:
                            pass
                        else:
                            self.parent2=self.randomPos
                self.tempArray[replacer]=individual.individual(self.cars[self.parent1].values[0],self.cars[self.parent2].values[1], self.cars[self.parent1].values[2], self.cars[self.parent2].values[3], self.cars[self.parent1].values[4], self.cars[self.parent2].values[5], self.cars[self.parent1].values[6], self.cars[self.parent2].values[7],self.cars[self.parent1].values[8],self.cars[self.parent2].values[9],self.cars[self.parent1].values[10],self.cars[self.parent2].values[11],self.cars[self.parent1].values[12], self.cars[self.parent2].values[13] )

        for i in range(len(self.cars)):
            self.cars[i] = self.tempArray[i]

        for i in range(self.numberOfElites, len(self.cars)):
            for gene in range(14):
        #        print "mutating "+str(i)
                if (random.uniform(0, 1) <= self.mutationChance):
                    muval = (self.cars[i].values[gene] * 0.1)+0.1 #random.uniform(-0.1,0.1)

                    if (random.uniform(0,1) <= 0.5):
                       muval = muval*-1
                    self.cars[i].values[gene] = self.cars[i].values[gene] + muval
                    self.cars[i].parameters[gene] = str(float(self.cars[i].parameters[gene]) + muval)
                    pass
        self.cars[0]=self.cars[self.returnFittest()]
        if self.currentIteration == 0:
           print "----------------------------------------------"
           print "run "+str(self.runval)+" starts here"
        print "run: "+str(self.runval)+" generation: "+str(self.currentIteration)+" fittest at: "+str(self.returnFittest())+" its fitness: "+str(self.returnFittestFitness())
        print "it's values:  "+str(self.returnFittestValues())
        print "pop avg fitn: "+str(self.returnAvgFitness())
        print "fitnessarray: "+str(self.fitArray)
        print "number of invalids: "+str(self.invalid)
        print"\n\n"
        bashCommand = "killall torcs-bin"
        os.system(bashCommand)
        print "killed old torcs processes"

        f = open("debugline_wheel2_aal_forza_eroad_street_alpine1.csv","a")
        f.write("run: "+str(self.runval)+" generation: "+str(self.currentIteration)+" fittest at: "+str(self.returnFittest())+" its fitness: "+str(self.returnFittestFitness())+"\n")
        f.close

        f = open("june14_aal_wheel2_aal_forza_eroad_street_alpine1.csv","a") #opens file with name of "test.txt"
        if self.currentIteration == 0:
            f.write(("\n\n\n\n"))
            f.write(("run "+str(self.runval)+" starts here\n"))
        f.write("generation;   "+str(self.currentIteration)+"; ")
        f.write("it's values;  "+str(self.returnFittestValues())+"; number of invalids;"+str(self.invalid)+" ; ")
        f.write("fitnessarray; "+str(self.fitArray)+"; ")
        f.write("pop avg fitn; "+str(self.returnAvgFitness())+"; ")
        f.write("fittest at;   "+str(self.returnFittest())+";  its fitness; "+str(self.returnFittestFitness())+";\n ")
        if self.currentIteration >= self.maxIterations:
            f.write(("the end:\n\n\n\n\n"))
        f.close

        self.currentIteration=self.currentIteration+1
        if self.currentIteration >= self.maxIterations:
            self.stop_reached = True


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
            self.fitArray = self.evaluate()



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
                 if self.fitArray[i] != -1:
                    leader = i
            elif (self.fitArray[i] < self.fitArray[leader]) and leader!=1000:
                if self.fitArray[i] != -1:
                    leader = i
        return leader

    def returnFittestValues(self):
        return self.cars[self.returnFittest()].getParameters()

    def returnFittestFitness(self):
        return self.fitArray[self.returnFittest()]

    def returnAvgFitness(self):
        total = 0
        self.invalid =0
        for i in range(len(self.fitArray)):
            if self.fitArray[i]==-1:
                self.invalid = self.invalid+1
            elif self.fitArray[i]!=-1:
                total = total + self.fitArray[i]
        avg = total/(len(self.fitArray)-self.invalid)
        return avg

    def evaluate(self):
        for ind in range(len(self.cars)):
            self.cars[ind].express()

        nproc = self.nr_processes
        times = []
        batches = len(self.cars)/nproc+1
        for batch in range(batches):
            if batch is not range(batches)[-1]:
                indivs = [a_+(nproc*batch) for a_ in range(nproc)]
            else:
                indivs = [a_+(nproc*batch) for a_ in range(len(self.cars)%nproc)]
            results = pprocess.Map(limit=nproc, reuse=1)
            parallel_function = results.manage(pprocess.MakeReusable(self.fitfun))
            [parallel_function(self.cars[ind].phenotype, (ind-nproc*batch)) for ind in indivs];
            times.extend(results[0:nproc])
            time.sleep(1)


        for ind in range(len(self.cars)):
            times[ind] = float(times[ind])
            return times
        return times
