# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:26:46 2023

@author: Ronnã Isaac
"""

'''
Maneira alternativa. Semelhante a outra, ele usa IFs para descobrir as linhas onde a primeira palavra é FROM
Mas no else, em vez de usar outros IFs para descobrir qual foi o dia da semana (if palavras[2]== 'Sat':),
ele usa o prórpio dicionário para encontrar as chaves.
Essa função 'dici[palavra[2]]+=1' serve para adicionar +1 no valor da chave(cada dia da semana) 
onde ela já existe, ou seja, se ela não existir não vai adicionar nada, mas se existir vai adicionar, 
e por consequencia contar quantos existem igual aqueles. 

'''

fhand= open('mbox.txt')

contador = 0 #contar quantos começam com From
dici= {'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0,'Fri':0, 'Sat':0, 'Sun':0 }
for linha in fhand:
    palavra= linha.split()
    
    if len(palavra)==0:
        continue
    if palavra[0]!= 'From':
        continue
    else:
       dici[palavra[2]]+=1
       contador+= 1
       
print(dici)
print('O numero de emails recebidos foi:', contador)