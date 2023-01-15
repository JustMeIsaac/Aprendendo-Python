# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:43:20 2023

@author: Ronnã Isaac
"""

'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao 
bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a 
aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do 
sindicato laboral, chegou-se a seguinte forma de cálculo:
    
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito 
baixo, recebem este valor mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, 
impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um 
número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de 
acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; 

A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. 
Os valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''
def parar(arg):                #função para quando digitar 0
    if arg == '0':      
        print('Voce digitou 0 para parar!')
        print('\n')
        return True
    else:
        return False

#################################################################

salarios= list()
while True:
    print('Informe o valor do salário(em R$)')
    
    try:            
        n = (input('Adicione um (escreva 0 para parar): \n \n'))   
        d= parar(n)                   
        if d == True:               
            print('Encerrando inserção... \n')
            break  
        n=float(n)
        if n<=0:
            print('\033[31mINSIRA APENAS VALORES VALIDOS \033[m \n')
            continue
        else:
            salarios.append(n)
            print('Adicionado com Sucesso')
    except ValueError:
        print('\033[31mValor INVÁLIDO! Digite apenas valores válidos!\033[m \n')
        
#################################################################

print('Projeção de gastos com Abono')
print('='*28, '\n')
print('Salários: \n')

w= int(0) #w vai servir para contar quantos salarios foram, preferi usar uma variavel pois é mais maleavel que o len(salarios)
for i in salarios:
    w+=1
    print('Salário %d : R$ %d' %(w,i))
  
#################################################################

print('\n')
print('Salário - Abono')

#################################################################

tabon=list()
vmin=0
for i in salarios:
    if i>500: #piso de salário(valor minimo) será 500 reais, ou seja, se for o minimo o valor do abono será determinado R$100
        abon= (i*0.2)
    else:
        abon=int(100)
        vmin+=1
        
    tabon.append(abon)
    print('R$ %d -'.ljust(2) %(i),' R$  %d' %(abon))
    
#################################################################

print('\n')
print('Foram processados %d colaboradores' %(w))
print('Total gasto com abonos: R$ %d' %(sum(tabon)))
print('Valor mínimo pago a %d colaboradores' %(vmin))
print('Maior valor de abono pago: R$ %d' %(max(tabon)))


