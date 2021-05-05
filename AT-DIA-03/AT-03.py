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
date_object = datetime.strptime('Jul 1 2014 2:43PM', '%Y %W %w')

# 4. Escreva um programa Python para subtrair cinco dias da data atual.


# 5. Escreva um programa Python para converter string de carimbo de data / hora em Unix  epoch.
print(
      datetime.)

# 6. Escreva um programa python para retornar hoje em unix epoch.


# 7. Escreva um programa Python para imprimir nos próximos 5 dias a partir de hoje.


# 8. Escreva um programa Python para obter o número da semana.


# 9. Escreva um programa Python para encontrar a data da primeira segunda-feira de uma determinada semana.

# 10. Escreva um programa Python para selecionar todos os domingos de um ano específico.


# 11. Escreva um programa Python para obter os dias entre duas datas.


# 12. Que dia será daqui a 876 dias? Crie um programa python para responder essa pergunta.


# 13. Que dia foi 876 dias atrás? Crie um programa python para responder essa pergunta.


# 14. Escreva um programa Python para ler um arquivo de texto inteiro. Arquivo anexo cv000_29590.txt

### Atenção com os comandos de read, pq eles movem o cursor para o fim, e os comandos seguintes,
#### Não funcionam

# 15. Crie um programa Python que receba um numero "N" do usuario e apresente as "N"
# primeiras linhas do arquivo lido no exercicio anterior


# 16. Escreva um programa Python para ler um arquivo linha por linha e armazená-lo em uma lista.
# Ao final apresente as linhas 3 e 6

# 17. Escreva uma função em Python que recebe um arquivo de texto como entrada e 
# retorna o número de palavras no texto. Utilize o arquivo do exercicio anterior.


# 18. Escreva uma função Python que recebe uma lista e retorna uma nova lista 
# com elementos exclusivos da primeira lista.
lista_teste = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,8,7,6,5,3,9,8,2,1,9,7,3,5,6,8,4,21,4,5,6,9,7,4,23,8,7,5]


# 19. Escreva um programa Python para criar uma função que receba um argumento,
#  e esse argumento será multiplicado por um número desconhecido dado. E crie 
# 4 exemplos


# 20. Escreva um programa Python para descobrir se uma determinada string começa 
# com um determinado caractere usando Lambda.


# 21. Faça alteração no resultado do exercicio anterior para que o caractere seja
# entrado pelo usuario.
