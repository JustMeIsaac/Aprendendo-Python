# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 22:48:41 2023

@author: Ronnã Isaac
"""
'''
Exercício 2: Escreva um programa que categorize cada mensagem de
e-mail de acordo com o dia em que a mensagem foi enviada. Para
isso, procure por linhas que comecem com “From”, depois procure pela
terceira palavra e mantenha uma contagem de ocorrência para cada dia
da semana. No final do programa, mostre em tela o conteúdo do seu
dicionário (a ordem não interessa).
linha exemplo:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Exemplo de código:
python dow.py
Enter a file name: mbox-short.txt
{'Sex': 20, 'Qui': 6, 'Sab': 1}

(Ou seja, contar quantos emails foram recebidos em cada dia)


exemplo explicado:

From cwen@iupui.edu Fri Jan  4 11:37:30 2008

procurar por linhas que comecem com FROM (ou seja, todos os emaisl recebidos), depois
pegar a terceira palavra(ou seja, o dia da semana)e registrar quantos emais foram recebidos
 nesse dia(ou seja, quantas linhas tem a terceira plavra igual).
                                                                         
'''

import os

    
while True:
    try:
        #fname = input('Digite o nome do arquivo (ex: mbox.txt) : ')
        fname = ('mbox.txt')
        fhand=open(fname)
        print('Arquivo encontrado:', fname, '\n')
        if fname == ('mbox.txt'):
            if os.path.exists('mbox.txt'):
                print('')           
        break       
    except :
        print('O arquivo', fname, 'nao pode ser encontrado')
        break

dic= {'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0,'Fri':0, 'Sat':0, 'Sun':0 } #cria um dicionario com cada chave para um dia da semana, com valores iniciais de 0
contador = 0 #contar quantos começam com From
for linha in fhand:
    palavras = linha.split() 
    if len(palavras) == 0 : #se a quantidades de palavras na linha for 0, não faz nada e continua
        continue
    if palavras[0] != 'From' : # se a primeira palavra da linha (palavras[0]) não for From, ignora e continua
        continue
    else:                       #senão, o contador recebe mais um(porque achou o From) e mostra a segunda palavra da linha (palavras[1])
        contador+= 1            #a partir de agora, toda vez que uma linha começar com 'From', ele vai verificar se a terceira palavra é algun dos dias da semana, e adicionar +1 no valor correspondente a chave do dicionario
        if palavras[2]== 'Mon':
            dic['Mon']= dic.get('Mon',0)+1  
        if palavras[2]== 'Tue':
            dic['Tue']= dic.get('Tue',0)+1  
        if palavras[2]== 'Wed':
            dic['Wed']= dic.get('Wed',0)+1  
        if palavras[2]== 'Thu':
            dic['Thu']= dic.get('Thu',0)+1  
        if palavras[2]== 'Fri':
            dic['Fri']= dic.get('Fri',0)+1
        if palavras[2]== 'Sat':
            dic['Sat']= dic.get('Sat',0)+1
        if palavras[2]== 'Sun':
            dic['Sun']= dic.get('Sun',0)+1
               
print(dic)
print('\n')
print('O numero de emails recebidos foi:', contador)










