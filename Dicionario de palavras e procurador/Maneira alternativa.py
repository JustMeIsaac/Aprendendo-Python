# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:56:47 2023

@author: Ronnã Isaac
"""

#Esse sistema funciona de forma parecida, mas usa o atributo .get . Não separa as palavras
#verificando se elas já existem. Ele armazena cada palavra como uma chave no dicionário
#e registra o valor como 1, se a chave ja tiver sido registrada o valor recebe +1.
#dessa forma, é possivel contar quantas vezes repete

def retorna_lista(arq): #essa função separa cada palavra no arquivo e coloca numa lista, e la na frente manda os valores para uma outra variavel
    lista = []
    for linha in arq:
        palavras = linha.split()
        lista.extend(palavras)
    return lista


texto = open('words.txt')          
novaLista = retorna_lista(texto)
print('\n\n Numero de palavras:', len(novaLista))

da= retorna_lista(novaLista)
dic= dict()
for i in da:
    dic[i]= dic.get(i,0)+1
print(dic)


print(dic['programs'])

