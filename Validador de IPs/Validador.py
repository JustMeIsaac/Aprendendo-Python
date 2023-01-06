# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 06:27:28 2023

@author: Ronnã Isaac
"""
#Ajuda de resolução: https://www.youtube.com/watch?v=OP5cruGz8t4

   
import os

#funcao validadora de ips
def validador(ipstr):
    partes = ipstr.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit(): #isdigit é se não é digito de valor numérico
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
        
    return True


if os.path.exists("1ista.txt"):
    ips = open("1ista.txt", "r")
    listaips = ips.read().split("\n")
    
    ipsvalidos = []
    ipsinvalidos = []
    
    for ip in listaips:
        if validador(ip) == True:
            ipsvalidos.append(ip)
        else:
            ipsinvalidos.append(ip)
    
    if len(ipsvalidos) > 0 or len(ipsinvalidos) > 0:
        arquivo_relatorio = open("resposta.txt", "wt")
        
        if len(ipsvalidos) > 0:
            arquivo_relatorio.write("[Endereços válidos:]\n")
            for valido in ipsvalidos:
                arquivo_relatorio.write(valido+"\n")
        
        if len(ipsinvalidos) > 0:
            arquivo_relatorio.write("\n[Endereços inválidos:]\n")
            for invalido in ipsinvalidos:
                arquivo_relatorio.write(invalido+"\n")
        
        arquivo_relatorio.close()
else:
    print("O arquivo 1ista.txt não pôde ser encontrado")


if os.path.exists("resposta.txt"):
    arq = open('resposta.txt')
    relatorio = arq.read() 
    print((relatorio))
