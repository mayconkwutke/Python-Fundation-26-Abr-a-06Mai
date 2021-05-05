# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:17:10 2021

@author: Maycon
"""
import os
# Exercicio 1 - Escreva um programa python que escreva na tela o texto abaixo 
# com a saída de exemplo, usando somente 1 comando print:
##     Twinkle, twinkle, little star, How I wonder what you are! Up above the 
##     world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!
###
###Twinkle, twinkle, little star,
###     How I wonder what you are! 
###    		Up above the world so high,   		
###		    Like a diamond in the sky. 
###Twinkle, twinkle, little star, 
###     How I wonder what you are!
print("""Twinkle, twinkle, little star,
      How I wonder what you are!
          Up above the world so high,
              Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are!""")

# Exercicio 2 - Escreva um programa Python que aceite uma sequência de números ou strings 
# separados por vírgula do usuário e gere uma lista e uma tupla com esses números.
dados = ('Python.py', 'java.jar', 123, 24, 10)
lista = [dados]
ntupla = tuple(dados)
# Exercício 3 - Da lista de arquivos apresente somente as extensões. Ex: .java, .py, .cpp
listDir = ('./')
for l in os.listdir(listDir):
    print (l.split('.')[-1])

        
# Exercício 4 - Utilizando o código e a lista da atividade 3, crie um dicionario 
# agrupando os valores e retornando dicionarios onde a chave é a extensão e o valor
# é a quantidade de vezes que a extensão aparece.
diclista = dict()
for l in os.listdir(listDir):
        if (l.split('.')[-1]) not in diclista:
            diclista[l.split('.')[-1]] = 1
        else:
            diclista[l.split('.')[-1]] += 1
print (diclista)

# Exercício 5 - Escreva um programa Python que o usario precise entrar com um valor
# para obter a diferença entre um determinado número e 17, se o número for maior 
# que 17, retorne o dobro da diferença absoluta.
## Observação use a funcao int(valor) para converter o texto em inteiro
valor = input('Digite um valor: ')
if int(valor) <= 17:
    print (17 - int(valor))
else:
    print ((int(valor) - 17)*2)
# Exercício 6 - Escreva um programa Python para calcular a soma de três números
# entrados pelo usuário, se os valores forem iguais, retorne três vezes o valor da soma dos 3.
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
num3 = int(input('Digite o terceiro numero:'))
total = num1 + num2 + num3
if num1 == num2 and num1 == num3:
    print ([total]*3)
else:
    print (num1 + num2 + num3)
# Exercício 7 - Escreva um programa Python para concatenar todos os elementos 
# de uma lista em uma string, separando cada um com um hifen, e retorná-la. 
## Utilize a lista filenames
contact_string = str()
for file in os.listdir(listDir):
    contact_string += file + '-'
print (contact_string)

lista = ['Banana', 'maça', 123, 29, 'teste']
String = lista[0] + "-" + lista[1] + "-" + str(lista[2]) + "-" + str(lista[3]) + "-" + lista[4]
print (String)
# Exercício 8 - Crie um programa que fique recebendo numeros do usuario
# até que ele digite -1.
# Em seguida crie uma tupla com os valores de divisão de piso por 2 de cada valor.
## Obervação 1 : O numero de controle nao pode aparecer na tupla final
num = int()
lista_valores = list()
valor_piso = int()
while num != -1:
    num = int(input("Digite um numero:")) 
    if num > 0:
        valor_piso = num // 2
        lista_valores.append(valor_piso)
    else:
        print ('Fim da execução')
print (tuple(lista_valores))
print()
# Exercicio 10 - Imprime todos os números pares de uma determinada lista de 
# números na mesma ordem e interrompe a impressão se qualquer número que vier 
# depois de 237 na sequência.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print (x)        
# Exercicio 11 - Crie um dicionario que tem como chave seu primeiro nome,
# e os valores são outro dicionarios com as informações sobre:
# Idade, sobrenome, email e DDD
# Em seguida imprima na tela apresentando como textos:
dict_leo = {"nome":"Leonardo", "dados":{"Idade":35, "sobrenome":"Lacerda", "email":"leolacerdagaller@live.com","DDD":11}}
print("""
Ola eu sou o %s %s, tenho %i anos. Meu email é %s e meu DDD é %i
""" % (dict_leo["nome"], 
       dict_leo["dados"]["sobrenome"], 
       dict_leo["dados"]["Idade"], 
       dict_leo["dados"]["email"],
       dict_leo["dados"]["DDD"]) )


    