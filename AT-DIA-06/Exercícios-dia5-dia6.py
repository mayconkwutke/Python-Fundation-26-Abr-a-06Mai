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

with open("texto_1.txt", "w") as f:
    f.write(texto_1)
    f.close()
print("Arquivo 1 gerado!")

with open("texto_2.txt", "w") as f:
    f.write(texto_2)
    f.close()
print("Arquivo 2 gerado!")

# Mostrando os arquivos no diretorio
from os import listdir
for file in listdir('.'):
    if file[0:5] == 'texto':
        print(file)
print()  
  
# 2 - Utilizando os arquivos de texto gerados no exercicio 1, crie uma lista 
# de caracteres únicos, presentes no texto.
lista_texto1 = []
for char in texto_1:
    if char != ' ':
        if char not in lista_texto1:
            lista_texto1.append(char)
print("lista_texto1",lista_texto1)  

lista_texto2 = []
for char in texto_2:
    if char != ' ':
        if char not in lista_texto2:
            lista_texto2.append(char)
print("lista_texto2", lista_texto2)  
print()
  
# 3 - Utilizando os arquivos criados no exercicio 1 crie um novo arquivo unindo 
# todas as palavras de ambos os textos. 
# Atenção, a união deve ser de forma intercalada, sendo uma palavra de cada texto.
lista_1 = texto_1.split(" ")
lista_2 = texto_2.split(" ")

lista_final = []
for word in zip(lista_1, lista_2):
    lista_final.append(word)

with open('texto_mix.txt',"w") as f:
    for i in lista_final:
       for x in range(len(i)):
           f.write(i[x])
           f.write(" ")
    f.close()
for file in listdir('.'):
    if file[0:5] == 'texto':
        print(file)
print() 

with open('texto_mix.txt','r') as f:
    print(f.read())
    f.close()
    
# 4 - Crie uma função em python que conta o numero de linhas de um texto que não 
# começam com a letra "b", maiusculo e minusculo.
## Utilize utilize os textos das variaveis do exercicio 1
print()
# 5 - Crie uma classe veiculo com velocidade maxima e autonomia como atributos
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print("modelX = ", modelX.max_speed, modelX.mileage)

# 6 - Crie uma classe onibus que herdara todas as variaveis e metódos da classe veículo
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("\nVehicle Name:", School_bus.name, 
      "Speed:", School_bus.max_speed, 
      "Mileage:", School_bus.mileage)

# 7 - Crie uma classe Bus que herda da classe Vehicle. Dê ao argumento de 
# capacidade de Bus.seating_capacity () um valor padrão de 50.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print("\nSchool_bus.seating_capacity = ", School_bus.seating_capacity())

# 8 - Defina a propriedade que deve ter o mesmo valor para todas as instâncias de classe
# Defina um atributo de classe “cor” com um valor padrão branco. 
# Ou seja, todos os veículos devem ser brancos.
class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print()
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
print()
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
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("\nTotal Bus fare is:", School_bus.fare())
print()
# 10 - Determine a qual classe um determinado objeto Bus pertence (verifique 
# o tipo de um objeto)
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(type(School_bus))
print()
# 11 - Escreva um programa Python para importar o módulo de array embutido e 
# exibir o namespace do referido módulo.
import array
for name in array.__dict__:
    print(name)
print()
# 12 - Escreva um programa Python para criar duas classes vazias, Student e 
# Marks. Agora crie algumas instâncias e verifique se são instâncias das referidas 
# classes ou não. Além disso, verifique se as referidas classes são subclasses 
# da classe de objeto embutida ou não.
class Student:
    pass 
class Marks:
    pass
 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 