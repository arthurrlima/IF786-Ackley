from random import randint
from random import shuffle
import math
import random
import itertools
import string
import matplotlib.pyplot as plt
import numpy as np
import statistics

#func geracao_zero OK
def geracao_zero(qtd):
    separador = ""
    bitMap = ['000','001','010','011','100','101','110','111']
    bitList = []
    
    for n in range(qtd):
        random.shuffle(bitMap)
        x = itertools.permutations(bitMap)
        strBit = separador.join(next(x))
        bitList.append(strBit)
    
    return(bitList)    
        
#recebe string de bits, cria lista de int, retorna n colisoes
def checkcolisao(string):
    colisao = 0
    rainhas = []
    
    #preenchendo lista com as posições das rainhas
    for k in range(0, 24, 3):
        rainha = int(string[k:k+3], 2)
        rainhas.append(rainha)

    #percorrendo rainhas
    #calculo de colisoes OK 
    for idx in range(len(rainhas)):
        aux = 0

        for chk in range(idx,len(rainhas)):
          
            if rainhas[chk] == rainhas[idx]+aux and idx != chk:
                colisao += 1

            elif rainhas[chk] == rainhas[idx]-aux and idx != chk:
                colisao += 1
            
            elif rainhas[chk] == rainhas[idx] and idx != chk:
                colisao += 1
            aux +=1

    return(colisao)      
    
#recebe lista de string, passa string pro calculo de colisão, retorna lista dos fitness da população
#calculo de fitness OK
def fitness(list):
    ftnslist = []
    
    for n in range(len(list)):
        stringbit = list[n]
        ftns = 1/(1+checkcolisao(stringbit))
        ftnslist.append(ftns)

    return(ftnslist)


#seleção de pais OK
def pais(list):
    ftnspais = []
    pais = []
   
    ftnspais = fitness(list)

    #encontro os dois maiores da lista e defino os pais

    pais.append(list[ftnspais.index(max(ftnspais))])
    ftnspais[ftnspais.index(max(ftnspais))] = 0

    #repito pro segundo pai
    pais.append(list[ftnspais.index(max(ftnspais))])
    return(pais)

#recombinação double cross point OK
def recombinacao(list):
    filhos = []
    parent1 = list[0]
    parent2 = list[1]
    
    crossPoint1 = random.randrange(0, 18, 3)
    crossPoint2 = random.randrange(crossPoint1+3, 21, 3)

    temp_child1 = parent1[:crossPoint1] + parent2[crossPoint1:crossPoint2] + parent1[crossPoint2:]
    temp_child2 = parent2[:crossPoint1] + parent1[crossPoint1:crossPoint2] + parent2[crossPoint2:]

    list.append(temp_child1)
    list.append(temp_child2)

    return(list)

#mutação OK
def mutacao(list):
    mutado = [] 
    mutacaoList = []
    separador = ""
    escSeparado = []
    escolhido = random.choice(list)
    #separa a string de bits num array com 8 posições
    for n in range(0, 24, 3):
        escSeparado.append(escolhido[n:n+3])

    #pontos onde a mutação pode ocorrer 
    #esses valores foram os melhores q eu testei, não tentei fazer por fitness
    xnumber1 = random.randrange(1, 4)
    xnumber2 = random.randrange(xnumber1+2, 7)

    #separa as partes que não serão mutacionadas
    parte1 = escSeparado[:xnumber1]
    parte2 = escSeparado[xnumber2:]

    #faz a mutação na outra parte
    mutacao = escSeparado[xnumber1:xnumber2]
    random.shuffle(mutacao)

    #junta tudo no novo array 
    mutado = parte1 + mutacao + parte2

    #junta os elementos do array em um novo individuo e retorna a população deletando o escolhido
    mutado = separador.join(mutado)
    del(list[list.index(escolhido)])
    
    list.append(mutado)

    return (list)
 
#metodo ok
def sobreviventes(list):
    ftnspop = fitness(list)
    
    while(len(list) > 100):
            del(list[ftnspop.index(min(ftnspop))])
            del(ftnspop[ftnspop.index(min(ftnspop))])
                 
    return (list)

#começo da execução
ctd_solucao = 0

x = []
y = []

plt.xlabel('x - iterations')
plt.ylabel('y - fitness medio')
plt.title('8 Queens Evolution')

population = geracao_zero(100)
tries = 0

while True:
    tries += 1
    x.append(tries)
    lista_fitness = fitness(population)
    fitnessmax = max(lista_fitness)
    fitnessmin = min(lista_fitness)
    y.append(statistics.mean(lista_fitness))

    

    index_ftns = lista_fitness.index(fitnessmax)
    bool_fit = math.isclose(fitnessmax, 1)

    if(bool_fit):
        ctd_solucao += 1
        #print("encontrada solução: ", population[index_ftns])
        #print("tentativa n*: ", tries)
        #print("Media = ", statistics.mean(lista_fitness))
        
        
    if(tries == 10000):
        print("limite de tentativas estourado")
        print("Media = ", statistics.mean(lista_fitness))
        print("Desvio Padrão = ", statistics.stdev(lista_fitness))
        print(ctd_solucao)

        print( max(lista_fitness))

        break

    if(math.isclose(fitnessmin, 1)):
        print("convergiu na ttv: ", tries)
        
        break
        
    
    selecao_pais = pais(population)

    chance_recomb = randint(1, 100)
    chance_mut = randint(1, 100)

    if(chance_recomb <= 90):
        prole = recombinacao(selecao_pais)

        if(chance_mut <= 60):
            prole = mutacao(prole)

        population = population + prole
    
    elif(chance_mut <= 60):
        population = mutacao(population)
    
    population = sobreviventes(population)