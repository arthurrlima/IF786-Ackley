import math
import random

#fitness é a função, menor é melhor
def fitnessFunc(self, chromosome):

	firstSum = 0.0
	secondSum = 0.0
	for c in chromosome:
		firstSum += c**2.0
		secondSum += math.cos(2.0*math.pi*c)
	n = float(len(chromosome))
	return(-20.0*math.exp(-0.2*math.sqrt(firstSum/n)) - math.exp(secondSum/n) + 20 + math.e)

#lista de listas OK
def gen_init(qtd):
    a = -3000
    b = 3000
    chromosome = []
    solution = []

    for k in range(qtd):
        for n in range(qtd):
            chromosome.append(random.randrange(a, b)/100)
        
        solution.append(list(chromosome))
        chromosome.clear()
    
    return(solution)

def parent_selec(alist):
	parents = []
	
	#como vai ser feita a seleção dos pais?

	return(parents)
