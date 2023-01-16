# -*- coding: utf-8 -*-

'''

Exercício 1: Faça o download de uma cópia do arquivo
www.py4e.com/code3/words.txt
Escreva um programa que leia as palavras em words.txt e as armazena
como chaves em um dicionário. Não importa quais são os valores. Então,
você pode usar o operador in como uma maneira rápida de verificar se
uma string está no dicionário.

explicacao: abrir um arquivo, ler todas as palavras nele. registrar cada palavra como uma chave no dicionario
Cada chave vai receber um valor, não importa qual seja. Depois, procurar usando a chave se existe esse valor 
dentro do dicionario


'''

#*usar a funçao para ler o texto, separar cada palavra, verificando se já existe ou nao
#*e registrar como uma chave no dicionario, o valor da chave não importa.

#Farei de forma simples, sem laços de repetição nem nada para procurar por nome o arquivo words.txt, apenas abrir direto.
#para fazer isso, vou usar as funções para separar as palavras e veridicar se já existem ou não e registra-las numa lista,
#como foi no exercicio de validador de Ips, depois usarei o resultado para registrar chaves no dicionario. Os valores 
#das chaves não importam, então serão o proprio nome da chave 


def retorna_lista(arq): #essa função separa cada palavra no arquivo e coloca numa lista, e la na frente manda os valores para uma outra variavel
    lista = []
    for linha in arq:
        palavras = linha.split()
        lista.extend(palavras)
    return lista

def palavras_ordenadas(nlista): #depois, essa funcao recebe a nova variavel e ordena as palavras, e coloca numa nova variavel
    tam = len(nlista)
    listaFinal = []
    for i in range(tam):
        contador = nlista.count(nlista[i])
        if contador == 1:
            listaFinal.append(nlista[i])
        elif contador > 1:
            ocorrencia = listaFinal.count(nlista[i])
            if ocorrencia == 0:
                listaFinal.append(nlista[i])
        contador = 0
    listaFinal.sort()
    return listaFinal

texto = open('words.txt')          
novaLista = retorna_lista(texto)
listaordenada = palavras_ordenadas(novaLista)
print('\n\n Numero de palavras:', len(listaordenada))
#cada palavra da lista 'listaordenada' será uma chave quando registrar no dicionario

#################################################################

#Feito os passos anteriores, separado cada palavra e etc, agora está tudo preparado para inserir no dicionario:

dicionario= dict()
for palavra in listaordenada:
    if palavra not in dicionario: #se ainda não houver uma chave com o nome do item 'palavra' na 'listaordenada', ele registra uma nova chave com o mesmo valor do item palavra
        dicionario[palavra]= palavra
    else:
        dicionario[palavra]=0 #0 para não inserir nada, já que a chave já foi registrada

print(dicionario)

#agora, preciso do sistema para procurar as chaves dentro do dicionario


procurar= input('Digite a palavra que quer procurar: \n')

if procurar in dicionario:
    print('\n\nPalavra encontrada:', dicionario[procurar])
else:
    print('\n\nPalavra não encontrada')
