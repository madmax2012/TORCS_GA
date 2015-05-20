def evaluate(self):
        for ind in range(len(self.pop)):
            self.pop[ind].express()

        nproc = self.nr_processes

        times = []
        batches = len(self.pop)/nproc+1
        batch_ranges = range(batches)
        for batch in batch_ranges:
            if batch is not batch_ranges[-1]:
                indivs = [a_+(nproc*batch) for a_ in range(nproc)]
            else:
                indivs = [a_+(nproc*batch) for a_ in range(len(self.pop)%nproc)]
            # Start parallel evaluation
            results = pprocess.Map(limit=nproc, reuse=1)
            parallel_function = results.manage(pprocess.MakeReusable(self.fitfun))
            [parallel_function(self.pop[ind].phenotype, (ind-nproc*batch)) for ind in indivs];
            times.extend(results[0:nproc])

        for ind in range(len(self.pop)):
            times[ind] = float(times[ind])
            if times[ind] < 1:
                self.pop[ind].fitness = 0
            else:
                self.pop[ind].fitness = 1./ (1. + times[ind])
            self.pop[ind].raw_fitness = times[ind]
