# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 23:11:11 2023

@author: Ronnã Isaac
"""
'''
Exercício 6: Reescreva o programa que solicita o usuário uma lista de
números e prints e imprime em tela o maior número e o menor número
quando o usuário digitar a palavra “feito”. Escreva um programa para
armazenar as entradas do usuário em uma lista e use as funções max()
e min() para computar o número máximo e o mínimo depois que o laço
for completo.
Digite um número: 6
Digite um número: 2
Digite um número: 9
Digite um número: 3
Digite um número: 5
Digite um número: feito
Máximo: 9.0
Mínimo: 2.0
'''






def aba(ab):                
    if ab == 'pronto':     
        print('Voce digitou pronto!')
        print('\n')
        return True
    else:
        return False

    
numeros=list()               

while True:
    try:            
        n = (input('Adicione uma nota (escreva pronto para parar): \n '))   #
        d= aba(n)                   
        if d == True:              
            print('Encerrando inserção...')
            break   
        else:                       
            int(n)                  
            numeros.append(n) 
            continue        
    except ValueError:
        print('\033[31mValor INVÁLIDO! Digite apenas números inteiros!\033[m')


print('Os valores digitados foram: ', numeros)
print('A quantidade de numeros inseridos foram: ',len(numeros))
print('\n')


print('O maximo valor digitado é: ',max(numeros))
print('O minimo valor digitado é: ',min(numeros))