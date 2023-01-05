# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:49:04 2023

@author: Ronnã Isaac
"""
#creditos autorais: Gabriel Souto
#https://www.youtube.com/watch?v=fQ2RN0ec-nc
#https://github.com/gabrielsouto?tab=repositories


#uso de biblioteca os para manipulação de arquivos
import os

def bytes_to_mb(qntbytes):
    return str(round(qntbytes/1048576, 2)).replace('.', ',')


def porcentagem(espaco_usado, total):
    return str(round(espaco_usado*100/total,2)).replace('.', ',')


if os.path.exists("usuarios.txt"):             #Verificando se o arquivo usuarios existe
    
    usuarios_espacos_txt = open("usuarios.txt", "r") #parametro r significa que o arquivo está aberto para leitura
    usuarios_espacos = usuarios_espacos_txt.read().split("\n") #variavel da lista de usuarios. Cada usuario e especo ocupado é uma linha na lista
    
    if len(usuarios_espacos) > 0: #contar a quantidade de valores na lista para saber se é maior que 0, se for maior que 0 entao valida. se nao for é porque a lista está vazia
        arquivo_relatorio = open("relatorio.txt", "wt") #cria uma variavel que vai receber os valores de um arquivo recem-aberto chamado relatorio.txt. O 'wt' significa que vai abrir pra escrita (w) no formato texto(t)
        arquivo_relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")#
        arquivo_relatorio.write("-" * 72 + "\n")# write escreve essa formatacao no arquivo
        
        #cabeçalho (as colunas)
        arquivo_relatorio.write("Nr.".ljust(5)) #escreve essa linha no arquivo, ljust(5)), leftjust, alinha a direita com no maximo 5 caracteres
        arquivo_relatorio.write("Usuário".ljust(15))
        arquivo_relatorio.write("Espaço utilizado".ljust(21))
        arquivo_relatorio.write("% do uso".ljust(9) + "\n\n")
        
        espaco_total = 0 #variavel servivel para calcular o espaço total 
        
        #calculando o espaço total
        for usuario_espaco in usuarios_espacos: #usuario_espaco in usuarios_espacos, para cada espaco de um usuario individual no total de espaço de todos os usuarios
            espaco_total += int(usuario_espaco.split()[1]) #divide o item da lista. Item da lista: alexandre       456123789. split divide e pega o que esta na posicao 1(que é 456123789) como inteiro e soma na propria variavel
        
        for indice_usuario_espaco in range(len(usuarios_espacos)): #serve para definir o indice, ou seja o numero da linha. Ou seja, para cada linha. len(usuarios_espacos) vai retornar 6. então range(6)
#o ultimo comando vai servir para cada linha dessa lista. então definindo as formatações ele vai repetir o for indice_usuario_espaco i range(6) para cada linha
            usuario_espaco = usuarios_espacos[indice_usuario_espaco].split() #espaco de cada usuario = lista dos espacos de todos os usuario[indice do usuario(ou linha)].split() divide a variavel .split() onde tem os espacos em branco
            
            usuario = usuario_espaco[0] #a variavel usuario vai receber o primeiro valor: alexandre
            espaco = usuario_espaco[1] #a variavel espaco vai receber o segundo valor: 456123789(bytes do alexandre)
            
            #agora vai escrever os dados no arquivo
            #para os dados ficarem certinho, usa as mesmas formatacoes anteriores para o nr, usuario, espaco utilizando e % de uso
            arquivo_relatorio.write(str(indice_usuario_espaco+1).ljust(5)) #primeira coluna, é a posicao
            arquivo_relatorio.write(usuario.ljust(15))
            arquivo_relatorio.write(bytes_to_mb(int(espaco)).rjust(7)+" MB           ") #com a funcao de bytes_to_mb(qntbytes)
            arquivo_relatorio.write(porcentagem(int(espaco), espaco_total).rjust(7)+"%\n") #com a funcao de porcentagem(espaco_usado, total)
            
            #Informacoes finais
        arquivo_relatorio.write("\nEspaço total ocupado: " + bytes_to_mb(espaco_total) + " MB\n")
        arquivo_relatorio.write("Espaço médio ocupado: " + bytes_to_mb(espaco_total/len(usuarios_espacos)) + " MB")
        
        arquivo_relatorio.close()
else:
    print("O arquivo usuarios.txt não existe")

#para mostrar na interface:
arq = open('relatorio.txt')
relatorio = arq.read() 
print((relatorio))


