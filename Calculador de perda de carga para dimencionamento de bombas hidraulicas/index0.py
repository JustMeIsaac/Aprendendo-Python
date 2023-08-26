# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 00:01:23 2023

@author: Ronnã Isaac
"""

'''
Calculador de perda de carga para dimencionamento de bombas hidraulicas
Contexto:
    
Os estudantes de engenharia civil de uma universidade precisam de uma ferramenta
para resolução de problemas de posicionamento de bombas hidraulicas
e dimencionamento de tubulações. Para isso, é necessário uma ferramenta que calcule
automaticamente as perdas de carga nos sistemas.

dados:
massa especifica agua (p): 1000 kg/m3
viscosidade tubulação (u):  10(-6) m2/s

Vazão fluido (Q): 16 l/s  (tendo a vazão tem-se a velocidade de escoamento)
diametro tubulacao (o): 4"" (ou 0.1016m)
comprimento linear da tubulacao (L): 500m
viscosidade agua (u): 0.000001
    
'''

import numpy

print('\n')

########
o = 4  #Diametro tubulacao em polegadas
Q = 16 #Vazao em L/s
L= 500 #Comprimento tubulacao em m

e= float(0.0001524)  #viscosidade do aço galvanizado em m
u = (10**(-6))   #viscosidade da agua no caso do exercicio
########
print('\nDados:\n')
#Convertendo as unidades para o SI
diametro= (o*0.0254) #de polegada para m
print('Diametro:',diametro)
        
area= (3.14*(diametro**2))/4  
print('Area:',round(area, 4))  

vazao = (Q*0.001)  #de l/s para m3/s
print('Vazao:',vazao)   

velocidade = (vazao/area) #em m/s
print('Velocidade:',round(velocidade, 4))


#calcular numero deRe (no caso usa-se a seguinte formula)
re = ((velocidade*diametro)/u)
print('Numero de RE:', round(re, 4),'\n')

#formula de swamee#
#dividi em partes para facilitar a escrita dos parenteses e expoentes
parte1= (64/re)**8

parte2= numpy.log (((e/3.7*diametro)+(5.74/re)))
parte3= ((2500/re)**6)
parte4= (parte2 - parte3)
parte5= (9.5* (parte4**(-16)))

parte6= (parte1+parte5)**(0.125)

'''
#caso queira fazer de forma mais direta (o resultado é o mesmo)
parte4= (numpy.log (((e/3.7*diametro)+(5.74/re))-((2500/re)**6)) )
parte3= (9.5*((parte2)**(-16)))     
f= (parte1+parte3)**(0.125)
'''

f= parte6
print('o valor aproximado de f é', round(f, 4))
#print('\n',f)
hf= f*(L/diametro)*((velocidade**2)/(2*9.98))
print('A perda de carga foi de',round(hf, 2), 'metros')




