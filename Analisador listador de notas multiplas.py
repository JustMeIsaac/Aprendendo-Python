# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:57:30 2023

@author: Ronnã Isaac
"""

''' 
EXERCICIO: 
Escreva um programa que lê repetitivamente números até
que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
soma total, a quantidade e a média dos números digitados. Se o usuário
digitar qualquer coisa que não seja um número, detecte o erro usando
o trye o except e mostre na tela uma mensagem de erro e pule para o
próximo número.

obs: farei apenas a soma das notas e a quantidade de notas por razões pragmaticas
'''


print('.............................BEM VINDO A ESTA APLICAÇÃO.............................')



def aba(ab):                #função para quando digitar pronto
    if ab == 'pronto':      #preferi usar uma função definida por mim para ficar mais facil depois
        print('Voce digitou pronto!')
        print('\n')
        return True
    else:
        return False
      
notas=list()                #crio a variavel notas do tipo lista vazia

while True:
    try:            #esse try e o except vao servir para saber se o valor que será digitado é um numero inteiro, nao aceitando outro, com exceção do comando #pronto#
        n = (input('Adicione uma nota (escreva pronto para parar): \n '))   #
        d= aba(n)                   #aqui d recebe a funcao com n de variavel
        if d == True:               #aqui ele valida se a funcao (que agora é a variavel d) retorna TRUE
            print('Encerrando inserção...')#ou seja, se digitar true, d vai ser true e ele vai encerrar o loop do while
            break   
        else:                       #se não retornar TRUE ele vai continuar com os proximos comandos depois dos else
            int(n)                  #aqui n recebe o tipo inteiro, precisa fazer isso pois posteriormente vamos somar os valores e para isso tem que ser inteiro
            notas.append(n) #notas.append(n) significa que ele vai adicionar um item na lista(n que foi digitado)
            continue        #ele adiciona e continua, posteriormente adicionando mais itens enquanto a funcao aba retornar FALSE
    except ValueError:
        print('\033[31mValor INVÁLIDO! Digite apenas números inteiros!\033[m')


print('As notas digitadas foram: ', notas)
print('A quantidade de notas inseridas foram: ',len(notas))
print('\n')


#vou explicar os seguintes passos tudo de uma vez:
somanotas=0
for i in notas:
    i=int(i)
    somanotas= somanotas+i

print(somanotas)   

'''
somanotas=0 comecei criando uma variavel que futuramente receberá o valor da soma das notas, como ainda não 
ha nada, ela é 0

for i in notas:   isso significa: #para cada item na lista notas#


i=int(i)
somanotas= somanotas+i

o item deve receber o valor dele mesmo convertido em integer
lembre-se que la atraz na hora de inserir o numero nos garantimos que seria integer, mas
ele armazena na lista como string

depois de i ser convertido, realizamos a soma

somanotas= somanotas+i
'''

