Relatorio Otimização Função Ackley

Descrição do Algoritmo Implementado:

1)Descrição:

a)Representação da Solução: Lista de Listas, cada cromossomo com N = 30, valores gerador uniformimente entre -15 e 15. 
b)Função de Fitness: como queremos otimizar até o 0, usamos o resultado da função como fitness, sendo menor, até 0, melhor.
c)População: Inicialização por distribuição normal.
d)Processo de selecão dos pais: Por distribuição uniforme, selecionando 2 pais para gerar 1 filho por ponto local intermediario
gerando 200 filhos com 30 pais fixos. Seleção(30, 200)

e)Recombinação por ponto local intermediario
f)Mutação Gaussiana

g)Processo de seleção de sobreviventes: Seleção por ranking, filtrando os piores membros, 30 pais sairam e os melhor 30
dos 200 filhos entraram, seleção(30, 200) sob conjunto de filhos.

3)Descrição dos resultados experimentais:
  tomamos a liberade de considerar o minimo do fitness 0.00, pois estavamos chegando em resultados muito proximos mas a comparação
  por ex: de 0.009 com 0 dava falso. então só estamos considerando 2 casa decimais.
  
  Resultados: 
    1* Solução na geração 175 média 0.0093
    2* Solução na geração 191 média 0.0085
    3* Solução na geração 181 média 0.0094
    4* Solução na geração 182 média 0.0084
    5* Solução na geração 205 média 0.0086
    6* Solução na geração 186 média 0.0081
    7* Solução na geração 182 média 0.0082
    8* Solução na geração 191 média 0.0093
    9* Solução na geração 191 média 0.0079
    10* Solução na geração 192 média 0.0088
    11* Solução na geração 186 média 0.0080
    12* Solução na geração 193 média 0.0082
    13* Solução na geração 187 média 0.0080
    14* Solução na geração 175 média 0.0087
    15* Solução na geração 203 média 0.0079
    16* Solução na geração 200 média 0.0078
    17* Solução na geração 184 média 0.0087
    18* Solução na geração 189 média 0.0084
    19* Solução na geração 198 média 0.0084
    20* Solução na geração 186 média 0.0082
    21* Solução na geração 192 média 0.0084
    22* Solução na geração 208 média 0.0080
    23* Solução na geração 192 média 0.0083
    24* Solução na geração 179 média 0.0089
    25* Solução na geração 191 média 0.0077
    26* Solução na geração 194 média 0.0082
    27* Solução na geração 180 média 0.0086
    28* Solução na geração 191 média 0.0084
    29* Solução na geração 190 média 0.0081
    30* Solução na geração 205 média 0.0085
	
	.
    
     
