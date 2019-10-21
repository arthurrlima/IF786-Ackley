import random
import statistics
import numpy as np
import math
from function import Ackley

U = np.random.uniform
N = np.random.normal
f_ackley = Ackley().f_x

def gen_init(qtd):

    cromossome = []
    solution = []

    for n in range(qtd):
        cromossome.clear()
        for k in range(30):
            cromossome.append(U(-15, 15))

        solution.append(list(cromossome))
    
    return solution

def fitnessFunc(cromossome):
        return abs(f_ackley(cromossome))



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
    to_mutate = U(0, 1, len(chromosomes)) < prob
    tau = 1 / np.sqrt(len(chromosomes))

    for i in range(len(chromosomes)):
            if to_mutate[i]:
                sigma = sigma * np.exp(tau * N(0,1))
                chromosomes[i] = chromosomes[i] + sigma * N(0,1)
                if chromosomes[i] > 15:
                    chromosomes[i] = 15
                elif chromosomes[i] < -15:
                    chromosomes[i] = -15
                

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
def survivors(population, children):
    
    fitnesspop = []
    fitnesschild = []

    for chromosomes in population:
        fitnesspop.append(fitnessFunc(chromosomes))
    
    for chromosomes in children:
        fitnesschild.append(fitnessFunc(chromosomes))

    #tira os piores 30 pais
    for n in range(30):
        del(population[fitnesspop.index(max(fitnesspop))])
        del(fitnesspop[fitnesspop.index(max(fitnesspop))])

    #adiciona os 30 melhores filhos
    for k in range(30):
        population.append(children[fitnesschild.index(min(fitnesschild))])

        del(children[fitnesschild.index(min(fitnesschild))])
        del(fitnesschild[fitnesschild.index(min(fitnesschild))])

    return population


#começo da execução

population = gen_init(200)
tries = 0

while True:
    tries += 1
    lista_fitness = []

    for c in population:
        lista_fitness.append(fitnessFunc(c))
   
    
    fitnessmax = max(lista_fitness)
    fitnessmin = min(lista_fitness)
    

    index_ftns = lista_fitness.index(fitnessmin)
    bool_fit = math.isclose(round(fitnessmin*100)/100, 0)

    if(bool_fit):
        print("encontrada solução: ", population[index_ftns])
        print("tentativa n*: ", tries)
        print("Media = ", statistics.mean(lista_fitness))
        break
        
    
    if(tries == 30000):
        print("limite de tentativas estourado, população não convergiu")
        print("Media = ", statistics.mean(lista_fitness))
        print("Desvio Padrão = ", statistics.stdev(lista_fitness))
        break

    if(math.isclose(round(statistics.mean(lista_fitness)*100)/100, 0)):
        print("População Convergiu, fitness min = ", fitnessmin)
        print("Media = ", statistics.mean(lista_fitness))
        print("Desvio Padrão = ", statistics.stdev(lista_fitness))
        break
    
    prole =[]

    while len(prole) < 200:
        selecao_pais = parent_selec(population)
        prole.append(recomb(selecao_pais))

    population_temp = []
    
    for cromo in population:
        mutade, sigma = gaussian(cromo)
        population_temp.append(mutade)

    
    for counter in range(200):
        if fitnessFunc(population_temp[counter]) < fitnessFunc(population[counter]):
            population[counter] = population_temp[counter]
    

    population = survivors(population, prole)
    
    

