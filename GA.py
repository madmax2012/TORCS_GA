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
            for i in range(self.popsize/20):
                    '''
                    #this one ONLY works on intel corei CPUs. xeon/amd does not work #self.cars.append(individual.individual(154.897575174, -0.19, 0.179856307171, 0.779904990626, 93.0625663607, 1.01137784125, 0.271561863594, 33.9671867449, 0.0215211462875, 6565.8878, 0.829675710924, 71.9746111702, 50.2293068554))
                    self.cars.append(individual.individual(154.897575174, -0.19, 0.179856307171, 0.779904990626, 93.0625663607, 1.01137784125, 0.271561863594, 33.9671867449, 0.0215211462875, 6565.8878, 0.829675710924, 71.9746111702, 50.2293068554, random.uniform(5,15)))

                    '''
                    '''
                    self.cars.append(individual.individual(154.897575174, -0.109, 0.284863518509, 0.618095446024, 82.8097466274, 0.991264062838, 0.398718049953, 24.2361683457, 0.0215211462875, 6500.218922, 0.829675710924, 64.6771500532, 45.1063761699, 17.9086116399))
                    self.cars.append(individual.individual(154.897575174, -0.01, 0.284863518509, 0.618095446024, 92.1219406971, 0.991264062838, 0.398718049953, 27.0401870508, 0.0215211462875, 6565.8878, 0.829675710924, 64.6771500532, 45.1063761699, 14.4706822508))
                    self.cars.append(individual.individual(154.897575174, -0.109, -0.139884752072, 0.618095446024, 92.1219406971, 0.991264062838, 0.258846244958, 29.8442057559, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(154.897575174, -0.109, -0.139884752072, 0.618095446024, 92.1219406971, 0.991264062838, 0.258846244958, 29.8442057559, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 45.1063761699, 10.1896469453))
                    self.cars.append(individual.individual(154.897575174, -0.109, -0.139884752072, 0.618095446024, 92.1219406971, 0.991264062838, 0.258846244958, 29.8442057559, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 45.1063761699, 16.1896469453))
                    self.cars.append(individual.individual(154.897575174, -0.01, -0.139884752072, 0.618095446024, 82.8097466274, 0.991264062838, 0.258846244958, 27.0401870508, 0.0215211462875, 6565.8878, 0.829675710924, 64.6771500532, 49.7170137868, 14.4706822508))
                    self.cars.append(individual.individual(154.897575174, -0.109, 0.272014883324, 0.618095446024, 92.1219406971, 1.19039046912, 0.398718049953, 36.3214889646, 0.0113059348246, 7222.57658, 1.01264328202, 78.4693515643, 44.6453124082, 16.1896469453))
                    self.cars.append(individual.individual(173.969220173, 0, 0.651319848204, 0.834388153164, 87.1289416607, 0.387674878176, 0.427117692025, 25.8047800707, 0.193517740795, 6029.2, 0.512128686714, 71.9746111702, 47, 13))
                    self.cars.append(individual.individual(154.897575174, -0.109, -0.139884752072, 0.618095446024, 92.1219406971, 0.991264062838, 0.258846244958, 29.8442057559, 0.0215211462875, 7222.57658, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(154.897575174, -0.109, -0.139884752072, 0.618095446024, 92.1219406971, 0.991264062838, 0.258846244958, 32.9286263315, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 17.9086116398))
                    '''
                    #1351@xeon ####total:1344.918time1: 99.656 time2: 213.558 time3: 146.26 time4: 137.612 time5: 120.968 time6: 95.914 time7: 61.318 time8: 157.998 time9: 128.394 time10: 183.24 parameters: [154.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398]
                    self.cars.append(individual.individual(154.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    #1345.182@amd
                    self.cars.append(individual.individual(154.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(164.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(164.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(155.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(155.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(156.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(156.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(157.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(157.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(158.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(158.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(159.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(159.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(160.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(160.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(161.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(161.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
                    self.cars.append(individual.individual(162.897575174, -0.0199, -0.139884752072, 0.779904990626, 82.8097466274, 1.19039046912, 0.384730869454, 32.9286263315, 0.0215211462875, 5909.19902, 0.829675710924, 78.4693515643, 49.7170137868, 17.9086116398))
                    self.cars.append(individual.individual(163.897575174, -0.1981, -0.139884752072, 0.456285901422, 92.1219406971, 0.991264062838, 0.523203956399, 29.5357636983, 0.0215211462875, 6565.8878, 0.829675710924, 71.2448650585, 49.7170137868, 16.1896469453))
             #   else:
              #      print"nope"
              #     self.cars.append(individual.individual(random.uniform(50,150), random.uniform(0,0.1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,70), random.uniform(0,1), random.randint(5000,8000),random.uniform(0,1),random.uniform(50,110)))
        print len(self.cars)
        if self.onlyTheBest == 1:
            print "runing the best three agents"
            #run: 31 generation: 38 fittest at: 0 its fitness: 753.984 debugline_aal_forza_eroad_street_alpine1.csv
            #useforbackwards debugging  self.cars.append(individual.individual('208.595628845', '0', '0.337569077045', '0.834388153164', '86.2476522441', '0.387674878176', '0.538589854949', '20.7118718573', '0.169766737753', '6632.22', '0.829675710924', '71.9746111702'))
            #AALBORG!self.cars.append(individual.individual('153.969220173', '-0.0576061041302', '0.651319848204', '0.834388153164', '87.1289416607', '0.387674878176', '0.427117692025', '25.8047800707', '0.193517740795', '6029.2', '0.512128686714', '71.9746111702'))

            #total:1310.766time1: 106.93 time2: 202.336 time3: 136.432 time4: 136.6 time5: 122.886 time6: 94.084 time7: 59.344 time8: 149.394 time9: 127.42 time10: 175.34 parameters:
            self.cars.append(individual.individual('162.897575174', '-0.0199', '-0.139884752072', '0.779904990626', '82.8097466274', '1.19039046912', '0.384730869454', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '86.4162867207', '49.7170137868', '16.0177504758'))


            #run: 38 generation: 0 fittest at: 2 its fitness: 1361.45
            #self.cars.append(individual.individual('154.897575174', '-0.109', '-0.139884752072', '0.618095446024', '92.1219406971', '0.991264062838', '0.258846244958', '29.8442057559', '0.0215211462875', '7222.57658', '0.829675710924', '71.2448650585', '49.7170137868', '16.1896469453'))

            #run: 38 generation: 11 fittest at: 0 its fitness: 1113.0
            #self.cars.append(individual.individual('154.897575174', '0.1979', '0.168057744099', '0.310657311279', '102.468822997', '0.810240057125', '0.398718049953', '24.4910791371', '0.0215211462875', '5909.19902', '0.829675710924', '71.9746111702', '45.1063761699', '14.6186662858'))


#            run: 34 generation: 25 fittest at: 0 its fitness: 862.018
#            it's values:  ['154.897575174', '-0.19', '0.179856307171', '0.779904990626', '93.0625663607', '1.01137784125', '0.271561863594', '33.9671867449', '0.0215211462875', '6565.8878', '0.829675710924', '71.9746111702', '50.2293068554']


        #    run: 34 generation: 99 fittest at: 0 its fitness: 865.536
        #    it's values:  ['154.897575174', '-0.01', '0.284863518509', '0.618095446024', '102.468822997', '0.810240057125', '0.0299651095111', '27.3234212634', '0.0215211462875', '6565.8878', '0.829675710924', '71.9746111702', '50.2293068554']

            #run: 32 generation: 26 fittest at: 1 its fitness: 900.578 aal_forza_eroad_street_alpine1_wheel2   survives spring!!
            #self.cars.append(individual.individual('140.72506834', '0', '0.337569077045', '0.650949337848', '86.2476522441', '0.511177942334', '0.284405922822', '27.8985014421', '0.158069070376', '6632.22', '0.663341555385', '71.9746111702', '50.7467746014'))
            #run: 32 generation: 32 fittest at: 0 its fitness: 872.688 aal_forza_eroad_street_alpine1_wheel2   survives spring!!
            #self.cars.append(individual.individual('140.72506834', '0', '0.203812169341', '0.650949337848', '77.5228870197', '0.511177942334', '0.412846515105', '27.8985014421', '0.0422621633381', '6632.22', '0.829675710924', '71.9746111702', '45.5720971413'))
            # run: 30 generation: 65 fittest at: 0 its fitness: 608.35
            #self.cars.append(individual.individual('208.595628845', '0.21', '0.0618706764536', '1.19741356867', '56.8213986236', '0.00149883632855', '0.384730869455', '38.2448785016', '0.286743411529', '8025.1962', '1.01264328202', '71.9746111702','70'))
            #run: 28 generation: 32 fittest at: 17 its fitness: 229.96
            #self.cars.append(individual.individual('189.541480768', '0', '0.337569077045', '0.816044271632', '87.1289416607', '0.236418316455', '0.271561863595', '28.4852580778', '0.299740819726', '7295.542', '0.829675710924', '71.9746111702','70'))
            #run: 28 generation: 17 fittest at: 14 its fitness: 230.578
            #self.cars.append(individual.individual('210.712756409', '0', '0.634806649722', '1.21960966533', '86.2476522441', '0.662295736567', '0.271561863594', '22.883059043', '0.299740819726', '5968.898', '0.646708139832', '64.0203785526','70'))
            #better than 250. forza/street1self.cars.append(individual.individual('215.660021346', '0', '1.05697326378', '0.82664655709', '66.7693387571', '0.250134392302', '0.570105115953', '2.55696562962', '0.126400385558', '8045.6936', '0.917106689539', '95.4289885556'))
            #fitness 261self.cars.append(individual.individual('188.250791367', '0.203178804399', '0.201697695058', '-0.133966377345', '29.8120257079', '0.379095750017', '-0.0824001900852', '35.3595847493', '0.701470069956', '7281.394', '0.90354898696', '90.6025843724'))
            #kandidat2self.cars.append(individual.individual('184.709123204', '0.110288535475', '4.57730481151', '0.26081797924', '25.3324247442', '0.578153650718', '0.474096761967', '44.7884012447', '0.660050929399', '6265', '0.521770258008', '100.9218245233'))
            # kandidat1self.cars.append(individual.individual('223.201153929', '-0.0937411420639', '0.379818787247', '-0.021153257182', '25.7592542818', '0.442765810551', '0.602867295277', '11.0035569307', '0.558417869716', '7481.2', '0.315208794339', '120.6071405164'))
           # self.cars.append(individual.individual('271.666625844', '0.204192624837', '18.4235771337', '0.680782953372', '53.3010185737', '-0.0637820025866', '0.628801496226', '15.7907437371', '0.366476146494', '5676'))
            #        self.cars.append(individual.individual('207.847515411', '0.0', '15.6251786512', '0.00449124915706', '39.0039459517', '0.674204459854', '0.592745557501', '13.3021387026', '0.734399954582'))
           #goood self.cars.append(individual.individual('182.013620623', '0.0689187178712', '23.4453697172', '0.302216184698', '42.9518949117', '0.339221849058', '0.852102375975', '19.535787977', '0.149008993859'))
            #self.cars.append(individual.individual('162.013620623', '0.0689187178712', '23.4453697172', '0.302216184698', '42.9518949117', '0.339221849058', '0.852102375975', '19.535787977', '0.149008993859'))
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
