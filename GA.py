#!/usr/bin/env python
import sys
import os
import time
import random
import pprocess
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
		self.cars.append(individual.individual(random.uniform(0,200), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1), random.uniform(0,100), random.uniform(0,1), random.uniform(0,1), random.uniform(0,20), random.uniform(0,1), random.randint(5000,8000),random.uniform(0,1),random.uniform(50,110),random.uniform(50,110),random.uniform(5,15)))
        print len(self.cars)
        if self.onlyTheBest == 1:
            #total:1339.172; aalborg: 100.808 alpine1: 212.258 alpine2: 143.42 brondehach: 135.83 corkscrew: 120.926 eroad: 95.704 gtrack: 61.342 forza: 156.748 wheel1: 128.67 wheel2: 183.466 parameters: ['154.897575174', '-0.0199', '-0.139884752072', '0.779904990626', '82.8097466274', '0.971351422208', '0.246257782509', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '49.7170137868', '17.9086116398']
            #FAEHRT SICHER aber auf manchen strecken ein wenig langsammer
            #self.cars.append(individual.individual('154.897575174', '-0.0199', '-0.139884752072', '0.779904990626', '82.8097466274', '0.971351422208', '0.246257782509', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '49.7170137868', '17.9086116398'))
            #total:1314.005; aalborg: 100.144 alpine1: 202.608 alpine2: 139.396 brondehach: 131.636 corkscrew: 123.965 eroad: 95.432 gtrack: 61.22 forza: 154.07 wheel1: 128.66 wheel2: 176.874 parameters: ['154.897575174', '-0.0199', '-0.0538732272792', '0.779904990626', '82.8097466274', '0.774216279987', '0.246257782509', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '44.6453124081', '17.9086116398']
            #SCHNELLER aber unsicherer
            #self.cars.append(individual.individual('154.897575174', '-0.0199', '-0.0538732272792', '0.779904990626', '82.8097466274', '0.774216279987', '0.246257782509', '32.9286263315', '0.0215211462875', '5909.19902', '0.829675710924', '78.4693515643', '44.6453124081', '17.9086116398'))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(183.902630812, 0.391839275478, 12.3853268076, 0.121281210318, 43.3083507585, -0.21471149892, 1.25608148977, 16.5475703255, 0.332463901642, 9740.589, 0.126978514373, 144.165143108, 52.8047758561, 7.91638377093))
            self.cars.append(individual.individual(83.5536275191, 0.4871838697, 1.94057551655, 0.327203389712, 30.1703226641, -0.0768832100989, 0.110052158283, 17.9431759548, 0.0310379895006, 9539.85, 0.198411957036, 81.0568379397, 57.3205897709, 12.2507990055))
            self.cars.append(individual.individual(172.116681754, 0.747403868829, 1.73361578693, 0.252209750679, 88.2306121751, 0.147964951594, 0.413886727673, 14.5322801791, 0.396581289152, 4965.434, 0.194693234273, 88.1849144445, 53.9671619572, 10.8761029498))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(153.243924078, 0.0964773504558, 0.772581305661, 0.471816772942, 26.0427168807, -0.319757921703, 0.453145870714, 13.2689374208, 0.730673628441, 6641.9, 0.52646477953, 102.412126, 45.5075240502, 11.2360814268))
            self.cars.append(individual.individual(176.88056238, 0.730545970362, 10.0591600431, 0.752519709557, 89.4861122267, -0.197046528668, 0.628921731729, 16.4051408123, 0.423575641258, 8744.88, 0.0253659272635, 110.392107617, 65.7412970488, 9.65918593309))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(183.902630812, 0.391839275478, 12.3853268076, 0.121281210318, 43.3083507585, -0.21471149892, 1.25608148977, 16.5475703255, 0.332463901642, 9740.589, 0.126978514373, 144.165143108, 52.8047758561, 7.91638377093))
            self.cars.append(individual.individual(83.5536275191, 0.4871838697, 1.94057551655, 0.327203389712, 30.1703226641, -0.0768832100989, 0.110052158283, 17.9431759548, 0.0310379895006, 9539.85, 0.198411957036, 81.0568379397, 57.3205897709, 12.2507990055))
            self.cars.append(individual.individual(172.116681754, 0.747403868829, 1.73361578693, 0.252209750679, 88.2306121751, 0.147964951594, 0.413886727673, 14.5322801791, 0.396581289152, 4965.434, 0.194693234273, 88.1849144445, 53.9671619572, 10.8761029498))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(153.243924078, 0.0964773504558, 0.772581305661, 0.471816772942, 26.0427168807, -0.319757921703, 0.453145870714, 13.2689374208, 0.730673628441, 6641.9, 0.52646477953, 102.412126, 45.5075240502, 11.2360814268))
            self.cars.append(individual.individual(176.88056238, 0.730545970362, 10.0591600431, 0.752519709557, 89.4861122267, -0.197046528668, 0.628921731729, 16.4051408123, 0.423575641258, 8744.88, 0.0253659272635, 110.392107617, 65.7412970488, 9.65918593309))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(183.902630812, 0.391839275478, 12.3853268076, 0.121281210318, 43.3083507585, -0.21471149892, 1.25608148977, 16.5475703255, 0.332463901642, 9740.589, 0.126978514373, 144.165143108, 52.8047758561, 7.91638377093))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(183.902630812, 0.391839275478, 12.3853268076, 0.121281210318, 43.3083507585, -0.21471149892, 1.25608148977, 16.5475703255, 0.332463901642, 9740.589, 0.126978514373, 144.165143108, 52.8047758561, 7.91638377093))
            self.cars.append(individual.individual(156.883447734, 0.693314885626, 11.7596327005, 0.180565646317, 66.0820915707, -0.0656196812059, 0.400646407141, 11.1188580429, 0.0601250945349, 7158, -0.0105849926423, 166.274486606, 83.4244108345, 10.9694914828))
            self.cars.append(individual.individual(183.902630812, 0.391839275478, 12.3853268076, 0.121281210318, 43.3083507585, -0.21471149892, 1.25608148977, 16.5475703255, 0.332463901642, 9740.589, 0.126978514373, 144.165143108, 52.8047758561, 7.91638377093))


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
                self.parents = [self.parent1, self.parent2]
 #               self.tempArray[replacer]=individual.individual(self.cars[self.parent1].values[0],self.cars[self.parent2].values[1], self.cars[self.parent1].values[2], self.cars[self.parent2].values[3], self.cars[self.parent1].values[4], self.cars[self.parent2].values[5], self.cars[self.parent1].values[6], self.cars[self.parent2].values[7],self.cars[self.parent1].values[8],self.cars[self.parent2].values[9],self.cars[self.parent1].values[10],self.cars[self.parent2].values[11],self.cars[self.parent1].values[12], self.cars[self.parent2].values[13] )
                self.tempArray[replacer]=individual.individual(self.cars[self.parents[random.randint(0,1)]].values[0],self.cars[self.parents[random.randint(0,1)]].values[1], self.cars[self.parents[random.randint(0,1)]].values[2], self.cars[self.parents[random.randint(0,1)]].values[3], self.cars[self.parents[random.randint(0,1)]].values[4], self.cars[self.parents[random.randint(0,1)]].values[5], self.cars[self.parents[random.randint(0,1)]].values[6], self.cars[self.parents[random.randint(0,1)]].values[7],self.cars[self.parents[random.randint(0,1)]].values[8],self.cars[self.parents[random.randint(0,1)]].values[9],self.cars[self.parents[random.randint(0,1)]].values[10],self.cars[self.parents[random.randint(0,1)]].values[11],self.cars[self.parents[random.randint(0,1)]].values[12], self.cars[self.parents[random.randint(0,1)]].values[13] )

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
        print "run; "+str(self.runval)+" ;generation; "+str(self.currentIteration)+" ;fittest at; "+str(self.returnFittest())+" ;its fitness; "+str(self.returnFittestFitness())
        print "it's values:  "+str(self.returnFittestValues())
        print "pop avg fitn: "+str(self.returnAvgFitness())
        print "fitnessarray: "+str(self.fitArray)
        print "number of invalids: "+str(self.invalid)
        print"\n\n"
        bashCommand = "killall torcs-bin"
        os.system(bashCommand)
        print "killed old torcs processes"

        f = open("debugline_alpine1_better_modSA_final.csv","a")
        f.write("run; "+str(self.runval)+" ;generation; "+str(self.currentIteration)+" ;fittest at; "+str(self.returnFittest())+" ;its fitness; "+str(self.returnFittestFitness())+"; number of invalids;"+str(self.invalid)+"\n")
        f.close

        f = open("alpine1_better_modSA_final.csv","a") #opens file with name of "test.txt"
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
