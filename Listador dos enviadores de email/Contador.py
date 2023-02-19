# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 22:45:56 2023

@author: Ronnã Isaac
"""

'''
Exercício 3: Escreva um programa que leia um registro de mensagens,
construa um histograma, utilizando um dicionário, para contar quantas
mensagens chegaram em cada endereço de email e mostre em tela o
dicionário.
Enter a file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

'''

fhand= open('mbox.txt')

contador = 0 #contar quantos começam com From
enviador= dict()


for linha in fhand: #para cada linha no texto
    palavras= linha.split() #palavras = lista de cada uma das palavras da linha

    if len(palavras)==0:
        continue
    if palavras[0]!= 'From':
        continue
    else:
        contador+= 1
        if palavras[1] not in enviador: #se o item 2 de cada linha da lista de palavras (ou seja, o email) não estiver no dicionário
            enviador[palavras[1]]=1     #ele cria uma nova chave usando o nome 'do item 2 de cada linha da lista de palavras' com valor inicial de 1
        else:
            enviador[palavras[1]]+=1  #senão, ele apenas soma 1 ao já exixtente (isso será feito para cada uma das chaves)

     
print('\nO numero de emails recebidos foi:', contador)
print('\n\nVoce recebeu emails de:',enviador) 




