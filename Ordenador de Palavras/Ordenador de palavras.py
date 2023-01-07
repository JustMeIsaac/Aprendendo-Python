# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:49:27 2023

@author: Ronnã Isaac
"""
'''
Exercicio 4: Baixe a copia do arquivo www.py4e.com/code3/romeo.txt.
Escreva um programa para abrir o arquivo chamado romeo.txt e leia-o linha por
linha. Para cada linha, separe-a em uma lista de palavras usando a função split.
Para cada palavra, cheque se esta palavra já existe na lista. Caso não exista,
adicione ela. Quando o programa terminar de verificar, ordene e imprima estas
palavras em ordem alfabética.**

Digite o nome do arquivo: romeo.txt

['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']


But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
'''

import os
import time

#ajuda de resolucao por https://github.com/somar07/Fundamentos-de-Python/blob/master/romeo.py:
def retorna_lista(arq):
    lista = []
    for linha in arq:
        palavras = linha.split()
        lista.extend(palavras)
    return lista

def palavras_ordenadas(nlista):
    tam = len(nlista)
    listaFinal = []
    for i in range(tam):
        contador = nlista.count(nlista[i])
        if contador == 1:
            listaFinal.append(nlista[i])
        elif contador > 1:
            ocorrencia = listaFinal.count(nlista[i])
            if ocorrencia == 0:
                listaFinal.append(nlista[i])
        contador = 0
    listaFinal.sort()
    return listaFinal


while True:
    try:
        fname = input('Digite o nome do arquivo (ex: romeo.txt) : ')
        fhand=open(fname)
        time.sleep(1)
        print('Arquivo encontrado:', fname, '\n')
        if fname == ('romeo.txt'):
            if os.path.exists('romeo.txt'):
                novaLista = retorna_lista(fhand)
                last = palavras_ordenadas(novaLista)
                time.sleep(1)
                print('As palavras são:',last)
        break       
    except :
        print('O arquivo', fname, 'nao pode ser encontrado')


        
