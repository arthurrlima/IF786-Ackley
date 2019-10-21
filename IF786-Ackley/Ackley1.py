import random
import statistics
import numpy as np
import math

U = np.random.uniform
N = np.random.normal

def gen_init(qtd):
    a = -1500
    b = 1500
    chromosome = []
    solution = []

    for k in range(qtd):
        for n in range(qtd):
            chromosome.append(random.randrange(a, b)/100)
        
        passoMutacao = statistics.stdev(chromosome)
        solution.append(list(chromosome))
        chromosome.clear()

    return solution, passoMutacao

def fitnessFunc(self, chromosome):
	firstSum = 0.0
	secondSum = 0.0
	for c in chromosome:
		firstSum += c**2.0
		secondSum += math.cos(2.0*math.pi*c)
	n = float(len(chromosome))
	return(-20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e)

def uniform(chromosomes):
    prob = 1/5
    upper = 15.0
    lower = -15.0
    to_mutate = U(0, 1, chromosomes.shape) < prob
    
    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            if to_mutate[i, j]:
                aux = chromosomes[i, j] + (U(0, 1) - 0.5) * 0.5 * (upper[i, j] - lower[i, j])
                while (lower[i, j] > aux or upper [i, j] < aux):
                    aux = chromosomes[i, j] + (U(0, 1) - 0.5) * 0.5 * (upper[i, j] - lower[i, j])
                chromosomes[i, j] = aux
    return chromosomes

def gaussian(chromosomes):
    prob = 1/5
    upper = 15.0
    lower = -15.0
    sigma = statistics.stdev(chromosomes)
    to_mutate = U(0, 1, chromosomes.shape) < prob
    tau = 1 / np.sqrt(len(chromosomes))

    for i in range(len(chromosomes)):
        for j in range(len(chromosomes[i])):
            if to_mutate[i, j]:
                sigma = sigma * np.exp(tau * N(0,1))
                chromosomes[i, j] = chromosomes[i, j] + sigma * N(0,1)

    chromosomes = np.maximum.reduce([chromosomes, lower])
    chromosomes = np.minimum.reduce([chromosomes, upper])

    return chromosomes, sigma

def parent_selec(solution):
   select = np.random.randint(0, 200, 2)

   parents = []

   parents.append(solution[select[0]])
   parents.append(solution[select[1]])

   return parents


#intermediario local
def recomb(parentslist):

    parent1 = parentslist[0]
    parent2 = parentslist[1]
    filho = []

    for n in range(30):
        filho.append((parent1[n] + parent2[n])/2)
    
    return filho


#seleção 30 pais, 200 filhos
def survivors():
    survs = []
    #organizar e tirar os piores 30 pais
    #organizar e adicionar os 30 melhores filhos

    
    
    return survs
