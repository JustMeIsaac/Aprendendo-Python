# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 00:10:50 2023

@author: Ronnã Isaac
"""
'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa 
dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de 
cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de 
identificação do mouse o tipo de defeito: necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma 
identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
    
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%



Explicação: ele analisa um numero n de mouses. Para cada um, ele vai digitar um numero que indica qual o defeito.
É importante lembrar que podem haver mais de um defeito em cada mouse, mas não farei isso pois
o exercicio não especificou, e a forma como deve se dar a execucao não permite isso
    
'''

def aba(ab):                #função para quando digitar 0
    if ab == '0':      
        print('Voce digitou 0 para parar!')
        print('\n')
        return True
    else:
        return False

print('Bem vindo a esta aplicação \n')
problemas= list()

while True:
    print('Identifique abaixo qual foi o problema: (digite 0 para encerrar) \n')
    print(' 1- necessita da esfera \n 2- necessita de limpeza \n 3- necessita troca do cabo ou conector \n 4- quebrado ou inutilizado')
    try:            
        n = (input('Adicione um (escreva 0 para parar): \n '))   #
        d= aba(n)                   
        if d == True:               
            print('Encerrando inserção...')
            break  
        n=int(n)
        if n>4 or n<1:
            print('\033[31mINSIRA APENAS VALORES VALIDOS (1,2,3,4)\033[m \n')
            continue
        else:
            problemas.append(n)
            print('Adicionado com Sucesso')
    except ValueError:
        print('\033[31mValor INVÁLIDO! Digite apenas valores válidos!\033[m \n')

print('A lista gerada foi:',problemas)

contadorp1=0
contadorp2=0
contadorp3=0
contadorp4=0

for i in problemas:
    if i==1:
        contadorp1+=1
        continue
    elif i==2:
        contadorp2+=1
        continue
    elif i==3:
        contadorp3+=1
        continue
    elif i==4:
        contadorp4+=1
        continue

print('A quantidade de problemas identificados foi:', len(problemas))


qtd=0
for i in problemas:
    qtd+=1

print('\n')
print('Quantidade de mouses:', qtd)
print('\n')
print('Situação', ' '*35, 'Quantidade', ' '*10, 'Percentual')
print('1- Necessita da esfera',' '*30, contadorp1, ' '*16,(contadorp1*100)/qtd,'%')
print('2- Necessita de limpeza',' '*29, contadorp2, ' '*16,(contadorp2*100)/qtd,'%')
print('3- Necessita troca do cabo ou conector',' '*14, contadorp3, ' '*16,(contadorp3*100)/qtd,'%')
print('4- Quebrado ou inutilizado',' '*26, contadorp4, ' '*16,(contadorp4*100)/qtd,'%')


