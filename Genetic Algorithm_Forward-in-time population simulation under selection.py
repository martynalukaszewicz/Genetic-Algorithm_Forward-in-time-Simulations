#!/usr/bin/env python
# coding: utf-8


import random
import copy
import math

Ls=[0,1,2,7,10,15,17,22,28,29]    ## position on genome of loci under selection
s=[0.02,0.007,-0.008,0.001,-0.005,0.002,0.05,0.01,0.01,-0.005]   ## selection coefficient at each selected locus
a=['A','G','G','T','C','C','A','C','C','T']  ## DNA molecule selected at each locus
ngen=30                ## number of non-overlapping generations
cross_comp=[20,20,20,20,20,20,20,20,15,10,5,5,5,5,5,5,5,8,9,10,15,20,20,20,20,20,20,20,20,20]
## cross_comp[j] a chance of crossover in %, where j is the position on the genome

genome_length=30 ## genome length, genome_length=len(cross_comp)
pop_size = 40  ## population size, kept constant

class indiv:
    def __init__(self):  ## generates new individual 'object'
        self.fitness=0
        self.genome=[]
        for i in range(genome_length):  
            self.genome.append(random.choice('ATGC'))  ## changed from random.uniform()
    def calc_fitness(self):
        self.fitness=0
        for k in range(len(Ls)):  ## k=0:(len(Ls)-1)
            self.fitness=self.fitness+(self.genome[Ls[k]]==a[k])*s[k]
        self.fitness=self.fitness+len(Ls)
          
    def print(self):  ## remove comments to see genomes of each individual per population per generation
        print(self.genome)
        print("Fitness = " + str(self.fitness))
        print(str(self.fitness))
    def mutate(self): ## new function to mutate a genetic value
        position = random.randint(0,len(self.genome)-1) ## mutation position on the genome 
        self.genome[position] = random.choice('ATGC') ## mutate at chosen position
        self.calc_fitness()
        
class population:
    def __init__(self):
        self.avg_fitness = 0 
        self.pop = []
        for i in range(pop_size):
            self.pop.append(indiv())
            
    def reproduction(self):
        temp=population()
        for i in range(pop_size):
            winner=self.selectWinner() ## need to create selectWinner() fn
            temp.pop[i]=copy.deepcopy(self.pop[winner])
        for i in range(pop_size):
            self.pop[i]=copy.deepcopy(temp.pop[i])
            self.pop[i].mutate()  ## mutate the new individuals
        self.crossover()
        self.calc_fitness()
    def crossover(self):
        for i in range(0,pop_size,2):
            for j in range(len(self.pop[i].genome)):  ## need to add this loop for varying crossover rates
                if(random.randint(0,100)<cross_comp[j]):  ## chance of crossover at each position 
                    # swap values
                    temp=self.pop[i].genome[j]
                    self.pop[i].genome[j]=self.pop[i+1].genome[j]
                    self.pop[i+1].genome[j]=temp
                ## if(random.randint(0,100)<101):  ## 100% chance   
                ##    print(j)
            self.pop[i].print()
            self.pop[i+1].print()
            print()
            print()  
    
    def selectWinner(self):
        winner=random.randrange(0,pop_size-1)
        bestFit=self.pop[winner].fitness
        for i in range(2):
            temp=random.randint(0,pop_size-1)
            if(self.pop[temp].fitness>bestFit):
                winner=temp
                bestFit=self.pop[temp].fitness
        return winner
             
    def calc_fitness(self):  ## calcu
        self.avg_fitness = 0
        for z in self.pop:
            z.calc_fitness()
            self.avg_fitness = self.avg_fitness + z.fitness # calculate the average fitness of the population
        self.avg_fitness = self.avg_fitness / (pop_size)  ## sum of fitnesses divided by population size
    def print(self): # new function to print entire populations
        for z in self.pop:
            z.print()
        print("Avg. Fit = " + str(self.avg_fitness))
        
p1=population()
for i in range(ngen):  ## number of generations
    p1.reproduction()
    print(p1.avg_fitness)  ## print average fitness of population per generation
p1.print()


