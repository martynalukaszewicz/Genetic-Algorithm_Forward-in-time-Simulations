# Genetic-Algorithm_Forward-in-time-Simulations

# Genetic-Algorithm_Forward-in-time-simulation

## Abstract

This expample looks at scenario of an evolution of a population of constant size of 40 over 30 non-overlapping generations.
The probability of genome crossover per genome position of 2 parental genomes depends on the position on the genome.
The first case is more likely to be seen in biology where the crossover rates on the chromosome differ based on the position of genes on the chromosome. The results indicate that the maximum fitness is reached over short span of generations. Code written in Python.




## Genetic Algorithm:

Create list ‘Ls’ with indexes of genome positions of loci under selection, ex.: 
Ls= [0,1,2,7,10,15,17,22,28,29].
Create list ‘s’ with selection coefficients at selected loci, ex.: 
s= [0.02,0.007,-0.008,0.001,-0.005,0.002,0.05,0.01,0.01,-0.005].
Create list ‘a’ with DNA molecule selected at each locus out of possible ‘A T G C’, ex.: 
a= ['A','G','G','T','C','C','A','C','C','T'].
Specify number of generations described by ‘ngen’ variable, ex.: ngen=30. The model assumes non-overlapping generations.
Specify chance of crossover (%) at each locus described by ‘cross_comp’, ex.:
cross_comp=[20,20,20,20,20,20,20,20,15,10,5,5,5,5,5,5,5,8,9,10,15,20,20,20,20,20,20,20,20,20].
Specify genome length described by ‘genome_length’ variable, ex.: genome_length=30. The genome length must be the same as the length of the ‘cross_comp’ list.
Specify population size described by ‘pop_size’ variable, ex.: pop_size=40. The model assumes constant population size over generations.
Generate new individuals for the entire population, each individual is a list of length to the genome length. Each DNA molecule at each genome position is chosen with equal probabilities from ‘A T G C’ possible choices.
Calculate fitness of each individual:
-	If an individual has a DNA molecule specified by list ‘a’ at genome position specified by list ‘Ls’, an individual gets added a numerical value specified by list ‘s’ to its fitness, ex.:
An individual with ['C', 'A', 'T', 'A', 'C', 'C', 'T', 'G', 'A', 'C', 'T', 'C', 'T', 'C', 'T', 'A', 'T', 'A', 'C', 'C', 'C', 'A', 'T', 'A', 'T', 'C', 'C', 'T', 'A', 'T'] genome with highlighted positions under selection specified by “Ls’,‘s’, and ‘a’ above, has a fitness of 10 plus the sum of 0.05 and -0.005, so 10.045.
-	Otherwise an individual fitness is equal to the length of list ‘Ls’.
Pick a single position for each individual on a genome where the mutation occurs. The chosen DNA molecule in mutation is picked randomly from ‘A T G C’ possible choices with equal probabilities. NOTE: it is possible that chosen DNA molecule to which it is mutated is the same as before the mutation takes place. The model assumes that the probability of transversion (purine to pyrimidines and vice versa) is the same as transition (pyrimidine to pyrimidine, purine to purine).
Calculate relative fitness of an individual in a population, which is a fitness of an individual divided by sum of the fitnesses of individuals in the entire population.
Recalculate fitness of each individual after performing mutations.
Calculate average fitness of a population.
Define reproduction:
-	Select randomly from a population with equal probability a ‘winner’ that gets to reproduce for i=0,1,2,…,pop_size. If a generated individual ‘temp’ has a higher fitness than the ‘winner’, name the ‘temp’ individual a ‘winner’, keeping the higher fitness.
-	For the crossover, for every 2 individuals, the crossover is performed by swapping between the 2 genomes with probabilities of crossover described by ‘cross_comp’. 
Print fitness values of each individual in a population, followed by average population fitness, followed by fitness values of individuals in a population in next generation, followed by average fitness,…, up to the fitness of individuals in last generation, followed by average population fitness in that generation.
