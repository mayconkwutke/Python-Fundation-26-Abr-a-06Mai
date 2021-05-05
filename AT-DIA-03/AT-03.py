# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:52:29 2021

@author: Maycon
"""
from datetime import datetime, date
# 1. Escreva um script Python para exibir os vários formatos de data e hora - vá para o editor
data_atual = datetime.today()
# a) Data e hora atuais
print (data_atual.strftime("%d-%m-%Y %H:%M"))
# b) ano atual
print (data_atual.strftime("%Y"))
# c) Mês do ano
print (data_atual.strftime("%B"))
# d) Número da semana do ano
print (data_atual.strftime("%W"))
# e) Dia da semana da semana
print (data_atual.strftime("%w"))
# f) Dia do ano
print (data_atual.strftime("%j"))
# g) Dia do mês
print (data_atual.strftime("%d"))
# h) Dia da semana
print (data_atual.strftime("%A"))


# 2. Escreva um programa Python para determinar se um determinado ano é um ano bissexto.
ano = int(input("Digite o ano:"))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print ('Ano Bissexto')
else:
    print ('Não é bissexto')

# 3. Escreva um programa Python para converter uma string em data e hora.
## Formato de entrada Jul 1 2014 2:43PM
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

# 4. Escreva um programa Python para subtrair cinco dias da data atual.
dt = date.today() - timedelta(5)
print('Hoje :',date.today())
print('5 dias atrás :',dt)
print()

# 5. Escreva um programa Python para converter string de carimbo de data / hora em Unix  epoch.
import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1619731209")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

### Solução 2
### Criando o objeto de data (ano, mes, dia)
import time
data_teste = datetime.date(2020, 5, 2).timetuple()
data_teste2 = datetime.datetime.now().timetuple() # Retornando hoje
epoch = time.mktime(data_teste)
epoch2 = time.mktime(data_teste2)
print ("\nepoch: ", epoch)
print ("epoch2: ", epoch2)

# 6. Escreva um programa python para retornar hoje em unix epoch.
import time
print("Hoje em unix epoch", time.time())
print()

# 7. Escreva um programa Python para imprimir os próximos 5 dias a partir de hoje.
base = datetime.datetime.today()
print("Exercicio 7 ####")
print('Hoje : ', base)
for x in range(1, 6):
      print(base + datetime.timedelta(days=x))
print()

# 8. Escreva um programa Python para obter o número da semana.
import datetime
print("\nExercicio 8")
print("Estamos na semana %i do ano." % datetime.date.today().isocalendar()[1])
print()

# 9. Escreva um programa Python para encontrar a data da primeira segunda-feira 
## de uma determinada semana.
import time
print("Exercicio 9 #### ")
print(time.asctime(time.strptime('2021 32 1', '%Y %W %w')))
print()

# 10. Escreva um programa Python para selecionar todos os domingos de um ano específico.
""" DESAFIO """
from datetime import date, timedelta
def all_sundays(year):
       dt = date(year, 1, 1)
       dt += timedelta(days = 6 - dt.weekday())  
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)
          
for s in all_sundays(2021):
   print(s)
print()

# 11. Escreva um programa Python para obter os dias entre duas datas.
from datetime import date
a = date(2021,4,29)
b = date(2022,10,5)
print("\nExercicio 11 #### ")
print(b-a)
print(type(b-a))

# 12. Que dia será daqui a 876 dias? Crie um programa python para responder essa pergunta.
dt = date.today() + timedelta(876)
print("\nExercicio 12 #### ")
print('Hoje :',date.today())
print('876 dias no futuro :',dt)
print()

# 13. Que dia foi 876 dias atrás? Crie um programa python para responder essa pergunta.
dt = date.today() - timedelta(876)
print("Exercicio 13 ####")
print('Hoje :',date.today())
print('876 dias no passado :',dt)
print()

# 14. Escreva um programa Python para ler um arquivo de texto inteiro. Arquivo anexo cv000_29590.txt
print("Exercicio 14 ####")
txt = open('/home/leogaller/Documents/Freela/Trainning/Python-Fundamentals/Exercicios/cv000_29590.txt')
# print(txt.read()) 

# while True:
#     break

### Atenção com os comandos de read, pq eles movem o cursor para o fim, e os comandos seguintes,
#### Não funcionam

# 15. Crie um programa Python que receba um numero "N" do usuario e apresente as "N"
# primeiras linhas do arquivo lido no exercicio anterior
N = int(input("Quantidade de linhas: "))
print(txt.readlines(N))
print()

# 16. Escreva um programa Python para ler um arquivo linha por linha e armazená-lo em uma lista.
# Ao final apresente as linhas 3 e 6
arquivo_path = '/home/leogaller/Documents/Freela/Trainning/Python-Fundamentals/Dia-4/cv000_29590.txt'
with open(arquivo_path) as f:
    #Content_list is the list that contains the read lines.     
    content_list = f.readlines()

print('linha 3 :', content_list[2])
print('linha 6 :', content_list[5])

## Solução 2
f = open('cv000_29590.txt', 'r+')
str = f.readlines()
listaarq = list(str)
print (listaarq[2], listaarq[5])
f.close()

# 17. Escreva uma função em Python que recebe um arquivo de texto como entrada e 
# retorna o número de palavras no texto. Utilize o arquivo do exercicio anterior.
print("Exercicio 17 #### ")
def conta_palavras(arquivo_path):
   with open(arquivo_path) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
   
print("A quantidade de palavras no texto é = ", conta_palavras(arquivo_path))

### Solução 2
def numpalavras():
    arquivo = open('/home/leogaller/Documents/Freela/Trainning/Python-Fundamentals/Dia-4/cv000_29590.txt', 'r+')
    str2 = arquivo.read()
    larq = str2.split()
    arquivo.close()
    return len(larq)
    
print(numpalavras())

# 18. Escreva uma função Python que recebe uma lista e retorna uma nova lista 
# com elementos exclusivos da primeira lista.
print("\nExercicio 18 #### ")
lista_teste = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,8,7,6,5,3,9,8,2,1,9,7,3,5,6,8,4,21,4,5,6,9,7,4,23,8,7,5]
def unique(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print("Valores únicos: ", unique(lista_teste))

# 19. Escreva um programa Python para criar uma função que receba um argumento,
#  e esse argumento será multiplicado por um número desconhecido dado. E crie 
# 4 exemplos
print("\nExercicio 19 #### ")
def mult(n):
 return lambda x : x * n

result = mult(2)
print("15 * 2 =", result(15))

result = mult(3)
print("15 * 3 =", result(15))

result = mult(4)
print("15 * 4 =", result(15))

result = mult(5)
print("15 * 5 =", result(15))

# 20. Escreva um programa Python para descobrir se uma determinada string começa 
# com um determinado caractere usando Lambda.
print("\nExercicio 20 #### ")

starts_with_P = lambda x: True if x.startswith('P') else False
print(starts_with_P('Python'))

starts_with_j = lambda x: True if x.startswith('J') else False
print(starts_with_j('Java'))

# 21. Faça alteração no resultado do exercicio anterior para que o caractere seja
# entrado pelo usuario.
print("\nExercicio 21 #### ")
starts_with_P = lambda x: True if x.startswith(input('Entre o Caracter em maiusculo:')) else False
print(starts_with_P('Python'))
starts_with_j = lambda x: True if x.startswith(input('Entre o Caracter em maiusculo:')) else False
print(starts_with_j('Java'))