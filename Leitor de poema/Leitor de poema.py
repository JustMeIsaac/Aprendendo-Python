# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 20:06:56 2023

@author: Ronnã Isaac
"""

print('............ABRIR ARQUIVOS..............')

print('\n')
#testar se pode encontrar o arquivo):
while True:
    try:
        fname = input('Digite o nome do arquivo (ex: poema.txt) : ')
        fhand = open(fname)
        break
    except:
        print('O arquivo nao pode ser encontrado:', fname)
    

###################################################

#ler todo o conteudo do arquivo
print('\n')

#ler o conteudo de uma linha (deixar vazio para ler tudo)
inp = fhand.read() #read le e armazena todo o conteudo em inp
print((inp))




