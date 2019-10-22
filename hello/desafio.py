import random
from math import fabs
from math import isclose

def geracao_zero(qtd):
    a = -2048
    b = 2048
    numeros = []
    for n in range(qtd):
        numeros.append(random.randrange(a, b)/1000)

    return numeros

def funct(x):
    fx = (100*((x-(x*x))*x)) + ((x-1)*(x-1))

    return fx

def fitness(list):
    fitness = []
    for n in list:
        fitness.append(funct(n))
    
    return fitness

def pais(list):
    pais = []
    ftnspais = fitness(list)
    absftns = abs(ftnspais)
   
    #encontro os dois maiores da lista e defino os pais
    pais.append(list[absftns.index(min(absftns))])
    absftns[absftns.index(min(absftns))] = 1500

    #repito pro segundo pai
    pais.append(list[absftns.index(min(absftns))])

    return pais

def xover(list):
    filho = (list[0]+list[1])/2
    return filho

def mutation(idvd):
    return idvd/2

def abs(list):
    abs = []
    for n in list:
        abs.append(fabs(n))
    
    return abs

def population(list, filho):
    population = []
    population = list


    ftpop = fitness(population)
    ftfilho = abs(fitness([filho]))

    i = ftpop.index(min(abs(ftpop)))

    ftpopmin = ftpop[i] *1000

    if ftpopmin << ftfilho[0]*1000:
        population[i] = filho

    return population


#iniciando 1a geração
populacao = geracao_zero(100)

solucao = False

#fitness 1a geração
for el in fitness(populacao):
    if isclose(el, 0):
        solucao = True
        print("solução encontrada", el)
        break
        



print(xover(pais(geracao_zero(100))))
print (fitness([xover(pais(geracao_zero(100)))]))



    