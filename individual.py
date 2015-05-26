__author__ = 'max'
class individual(object):
    def __init__(self,p0, p1, p2, p3, p4, p5, p6, p7, p8):
        self.parameters =[]
        self.values = []
        self.parameters.append(''+str(p0)+'')
        self.parameters.append(""+str(p1)+"")
        self.parameters.append(""+str(p2)+"")
        self.parameters.append(""+str(p3)+"")
        self.parameters.append(""+str(p4)+"")
        self.parameters.append(""+str(p5)+"")
        self.parameters.append(""+str(p6)+"")
        self.parameters.append(""+str(p7)+"")
        self.parameters.append(""+str(p8)+"")
        self.values.append(p0)
        self.values.append(p1)
        self.values.append(p2)
        self.values.append(p3)
        self.values.append(p4)
        self.values.append(p5)
        self.values.append(p6)
        self.values.append(p7)
        self.values.append(p8)
    def getParameters(self):
        return self.parameters


    '''
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
            self.cars.append(individual.individual('162.013620623', '0.0689187178712', '23.4453697172', '0.302216184698', '42.9518949117', '0.339221849058', '0.852102375975', '19.535787977', '0.149008993859'))
        self.tournamentSize=sp
        self.crossoverChance = cross
        self.debug=0
        self.mutationChance = mut'''
