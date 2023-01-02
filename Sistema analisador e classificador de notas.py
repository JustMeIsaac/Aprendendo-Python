# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 05:38:28 2023

@author: Opequenodev
"""

'''
Escreva um algoritmo capaz de receber o valor de uma nota
entre 0.0 e 1.0 e exiba a classificação segundo a tabela:

Classificação Nota:
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
'''


print('...............SISTEMA ANALISADOR VALIDADOR E CLASSIFICADOR DE NOTA (DEU TRABALHO FAZER)...........')


while True:  
    nome= (input('Informe seu nome: \n ') )
    try:
        str(nome)
        print('Olá', nome , ', bem vindo a esta aplicação \n \n')
        break
    except ValueError:
            print('Por favor, digite um nome válido')


print('Informe sua nota:')


#DEFININD0 A FUNCAO QUE VAI ANALISAR AS NOTAS:
    
def detnota(n):   
    if n>1.0 or n<0.0:
        print('Valor de nota invalido, insira algo entre 0.0 e 1.0')
        return False            #essa bosta precisa retornar FALSE pra la na 
                                #frente o while TRUE reconhecer que e falso e repetir o comando denovo
    else:
        print('Valor valido :D \n')
        return True             #essa bosta precisa retornar TRUE pra la na 
                                #frente o while TRUE reconhecer que e TRUE e continuar a execucao
                                
#FUNCAO DE COMPUTAR AS NOTAS

'''
Pontuação Nota
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

'''

def computa(c):
    if c>= 0.9:
        print('Classificação : A')
        
    elif c<0.9 and c>=0.8:
        print('Classificação : B')
        
    elif c<0.8 and c>=0.7:
        print('Classificação : C')
        
    elif c<0.7 and c>=0.6:
        print('Classificação : D')
        
    elif c<0.6:
        print('REPROVADO')

####################################EXECUÇÃO#####################

while True:         
    num=(input())   
    try:
        num=float(num)                           
        if detnota(num)== True:
               break 
    except ValueError:
        print("INSIRA UM VALOR VALIDO \n")
       
#COMECEI A FAZER ISSO AQUI 00:30 E JA SÃO 06:21 E SO AGORA CONSEGUI RESOLVER ESSA ULTIMA FUNCAO ACIMA :D
#01/01/2023 06:21
#RONNÃ ISAAC, O PEQUENO DEV        

print('Sua nota foi:' , num, '\n')


computa(num)

