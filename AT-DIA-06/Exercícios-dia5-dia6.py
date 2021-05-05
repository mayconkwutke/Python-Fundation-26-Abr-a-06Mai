#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:02:10 2021

@author: Maycon
@note: Exercicios do conteudo do dia 03 e 04
"""

# 1 - Crie umm arquivo de texto com a string abaixo:
texto_1 = """ Welcome to the Python Wiki, a user-editable compendium of knowledge
based around the Python programming language. Some pages are protected
against casual editing - see WikiEditingGuidelines for more information
about editing content."""

texto_2 = """Python is a great object-oriented, interpreted, and interactive
programming language. It is often compared (favorably of course :-) )
to Lisp, Tcl, Perl, Ruby, C#, Visual Basic, Visual Fox Pro, Scheme or Java...
and it's much more fun."""

arquivo = open('numero1.txt', 'w')
arquivo.write(texto_1 + "\n\n" + texto_2)

arquivo.close()

# 2 - Utilizando os arquivos de texto gerados no exercicio 1, crie uma lista 
# de caracteres únicos, presentes no texto.

# 3 - Utilizando os arquivos criados no exercicio 1 crie um novo arquivo unindo 
# todas as palavras de ambos os textos. 
# Atenção, a união deve ser de forma intercalada, sendo uma palavra de cada texto.

# 4 - Crie uma função em python que conta o numero de linhas de um texto que não 
# começam com a letra "b", maiusculo e minusculo.
## Utilize utilize os textos das variaveis do exercicio 1

# 5 - Crie uma classe veiculo com velocidade maxima e autonomia como atributos

# 6 - Crie uma classe onibus que herdara todas as variaveis e metódos da classe veículo

# 7 - Crie uma classe Bus que herda da classe Vehicle. Dê ao argumento de 
# capacidade de Bus.seating_capacity () um valor padrão de 50.

# 8 - Defina a propriedade que deve ter o mesmo valor para todas as instâncias de classe
# Defina um atributo de classe “cor” com um valor padrão branco. 
# Ou seja, todos os veículos devem ser brancos.

# 9 - 
"""
Crie uma classe filho Bus que herda da classe Vehicle. A cobrança de tarifa 
padrão de qualquer veículo é a capacidade de assentos * 100. Se o veículo for 
uma instância de ônibus, precisamos adicionar um extra de 10% na tarifa total 
como uma taxa de manutenção. Portanto, a tarifa total por exemplo de ônibus se 
tornará o valor final = tarifa total + 10% da tarifa total.

Observação: a capacidade do ônibus é 50. Portanto, o valor final da tarifa 
deve ser 5.500. Você precisa substituir o método fare () de uma classe 
Vehicle na classe Bus.
"""

# 10 - Determine a qual classe um determinado objeto Bus pertence (verifique o tipo de um objeto)

# 11 - Escreva um programa Python para importar o módulo de array embutido e 
# exibir o namespace do referido módulo.

# 12 - Escreva um programa Python para criar duas classes vazias, Student e 
# Marks. Agora crie algumas instâncias e verifique se são instâncias das referidas 
# classes ou não. Além disso, verifique se as referidas classes são subclasses 
# da classe de objeto embutida ou não.
