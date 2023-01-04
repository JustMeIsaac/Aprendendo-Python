# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 23:42:38 2022

@author: Ronnã Isaac
"""
import time

print('\n')
print('... Sistema de converção de Temperaturas ...')
print('\n')

time.sleep(1)

'''
################################## Bloco de Fahrenheit para Celcius ##################################################
print('Fahrenheit para Celcius')
while True:
    fahr = input('Qual a temperatura em Fahrenheit? \n')
    try:
        fahr = float(fahr)
        time.sleep(1)
        break
    except ValueError:
        print('INSIRA UM VALOR DE TAMANHO VÁLIDO! \n')


def fahrcel(tcel):
    tcel = (fahr - 32.0) * 5.0 / 9.0
    print('A temperatura em celcuis é %d ' %tcel)

fahrcel(fahr)

'''

################################## Bloco de Celcius para Fahrenheit #################################################

print('Celcius para Fahrenheit')
print('\n')

while True:
    cel = input('Qual a temperatura em Celcius? \n')
    try:
        cel = float(cel)
        time.sleep(1)
        break
    except ValueError:
        print('INSIRA UM VALOR DE TAMANHO VÁLIDO! \n')


def celfahr(tfahr):
    #(0 °C × 9/5) + 32 = 32 °F
    tfahr = (cel* (9/5) +32)
    print('A temperatura em celcuis é %d graus' %tfahr)

celfahr(cel)

