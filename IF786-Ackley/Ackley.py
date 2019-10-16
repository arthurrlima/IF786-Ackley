import math
import random
import statistics
import numpy as np

N = np.random.normal
U = np.random.uniform

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
        
        passoMutacao = statistics.stdev(chromosome)
        chromosome.insert(0, passoMutacao)
        solution.append(list(chromosome))
        chromosome.clear()

    return(solution)

# Vi no slide que a seleção de pais é aleatoria e uniforme
def selecaoPais(alist):
    parents = []
    first = random.randint(0,29)
    second = random.randint(0,29)
    parents.append(alist[first])
    parents.append(alist[second])

    return (parents)

def Normal(alist):
    normalvet = []
    passo = statistics.stdev(alist)
    for n in range(len(alist)):
        normalvet.append((1/passo*math.sqrt(2*math.pi)) * (math.e**(alist[n]/2*(passo**2))))
        
    return (normalvet)


def mutationpass(alist):
    passo = []
    c = 0.9
    distNormal = Normal(alist)
    for n in range(len(alist)):
        passo.append(statistics.stdev(alist[n]))
    for n in range(len(alist)):
        if(distNormal> 1/5):
            passo[n] = passo[n]/c
        elif(distNormal < 1/5):
            passo[n] = passo[n]*c
        else:
            passo[n] = passo[n]

    return (passo)

##função da mutação vai ser pra um cromossomo por vez com o mesmo desvio padrão
## depois atualiza pela regra do sucesso(define exploit ou explore)
def mutation(alist):
    escolhido = random.randint(0, 29)
    muted = alist[escolhido]
    print(muted)
    t = math.sqrt(1/len(alist))
    print(t)
    passoMutacao = statistics.stdev(muted)
    print(passoMutacao)
    passoMuted = passoMutacao * (math.exp(t * N(0, 1)))
    print(passoMuted)
    muted.insert(0, passoMuted)
    for n in range(1, len(alist)):
        muted[n] = (muted[n] + N(0, passoMuted))
        if(muted[n] > 30):
            muted[n] = (muted[n] - N(0, passoMuted))
        if(muted[n] < -30):
            muted[n] = (muted[n] - N(0, passoMuted))
    return (muted)


## seleção de pais distribuição uniforme, u = numero de filhos, y = numero de pais (u, y)
## 2 pais, recombinação por amostragem, mistura as informações

#substituição geracional, filhos substituem os pais

#função da probabilidade 


geracaoI = gen_init(30)
print (mutation(geracaoI))