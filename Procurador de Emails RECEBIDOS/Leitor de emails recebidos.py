# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:26:24 2023

@author: Ronnã Isaac
"""

'''
Exercício 5: Escreva um programa que leia uma caixa de email, e quando
você encontrar uma linha que comece com “De”, você vai separar a linha
em palavras usando a função split. Nós estamos interessados em quem
envia a mensagem, que é a segunda palavra na linha que começa com
From.
De stephen.marquard@uct.ac.za Sáb Jan 5 09:14:16 2008
Você vai analisar a linha que começa com From e irá pôr para imprimir
na tela a segunda palavra (para cada linha do tipo), depois o programa
também deverá contar o número de linhas que começam com “De” e
imprimir em tela o valor final desse contador. Esse é um bom exemplo
da saída com algumas linhas removidas:
python fromcount.py
Digite o nome do arquivo: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word



Ou seja,procurar todas as linhas que começam com From(os emails recebidos), mostrar a 
segunda palavra(quem enviou) e contar quantas foram no final
'''


while True:
    try:
        fname = input('Digite o nome do arquivo (ex: mbox.txt) : ')
        fhand = open(fname)
        break
    except:
        print('O arquivo nao pode ser encontrado:', fname)

        
contador = 0 #contar quantos começam com From
for linha in fhand:
    palavras = linha.split() 
    if len(palavras) == 0 : #se a quantidades de palavras na linha for 0, não faz nada e continua
        continue
    if palavras[0] != 'From' : # se a primeira palavra da linha (palavras[0]) não for From, ignora e continua
        continue
    else:                       #senão, o contador recebe mais um(porque achou o From) e mostra a segunda palavra da linha (palavras[1])
        contador+= 1
    print(palavras[1])

   
print('\n')
print('O numero de emails recebidos foi:', contador)
