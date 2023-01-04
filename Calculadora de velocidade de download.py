# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:45:45 2023

@author: Ronnã Isaac
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:50:10 2023

@author: The sigma Isaac
"""

'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do 
arquivo usando este link (em minutos), supondo que a velocidade de download é constante e estável.
'''

import time

#neste exercicio usarei o modulo time para deixar a execução mais dinâmica

print('\n')
print('........................Calculadora de tempo de download.............................')
print('\n')

time.sleep(2)

#laços de repetição para garantir valores válidos, pois só pode aceitar dados do tipo float, não aceitando por exemplo strings
while True:
    tam = input('Qual o tamanho do arquivo que queres baixar? (em Mb) \n')
    try:
        tam = float(tam)
        time.sleep(1)
        break
    except ValueError:
        print('INSIRA UM VALOR DE TAMANHO VÁLIDO! \n')
        
while True:
    vel = input('Qual é a velocidade de download? (em MbpS) \n')
    try:
        vel = float(vel)
        #caso queiras limitar a velocidade de download, inclua esses comandos destacados e defina o valor na condicional:
        #if vel>1024:
           # print('Velocidade maior que o máximo suportado, tente novamente \n')
           # retunr False
        #else:
            #return True
        time.sleep(1)
        break
    except ValueError:
        print('INSIRA UM VALOR DE VELOCIDADE VÁLIDO! \n')
             
print('\n')      
time.sleep(1)
print('Calculando... \n')
time.sleep(1) 

#formula de calculo do tempo de download (resultado em segundos):
#Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = tempo em segundos.
#Exemplo: um arquivo de 15 MB, baixado a 10 Mb/s: 15 / (10/8) = 12 segundos.

temposeg = (tam / (vel/8))

#funcao para converter segundos em formatação
def calculotempo(seg):
    seg= seg % (24 * 3600)
    hora = seg // 3600
    seg %= 3600
    minuto= seg // 60
    seg %= 60
    
    return '%d:%02d:%02d' %(hora,minuto,seg)

time.sleep(1)        
print('O tempo estimado de download é:', calculotempo(temposeg)  )  




    






