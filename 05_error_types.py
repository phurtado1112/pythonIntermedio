### Error Types ###

## SyntaxError ##

# print '¡Hola comunidad!' # Error de sintacxis falta los paréntesis
print('¡Hola comunidad!') # Correcto

print('=========================================')

## NameError ##
variable = 'Mi variable de texto' # Comentar para ver el error

print(variable)

print('=========================================')

## IndexError ##

my_list = ['Python', 'Swift', 'Kotlin', 'Dart', 'JavaScript', 'PHP']

print(my_list[0])
print(my_list[4])
print(my_list[-2])
print(my_list[5])

# print(my_list[6]) # Descomentar para error

print('=========================================')

## ModuleNotFoundError ##

# import maths # Descomentar para error 

import math # Correcto

print('=========================================')

## AttributeError ##

# print(math.PI) # Descomentar para error

print(math.pi) # Correcto

print('=========================================')

## KeyError ##

my_dict = {'Nombre': 'Pablo', 'Apellido':'Hurtado', 'Edad': 60, 1:'Python'}

print(my_dict['Edad'])

# print(my_dict['Apelido']) # Descomentar para error
print(my_dict['Apellido']) # Correcto

print('=========================================')

## KeyError ##

# print(my_list['Nombre']) # Descomentar para error
# print(my_list['1']) # Descomentar para error
print(my_list[1]) # Correcto

print('=========================================')

## ImportError ##

# from math import PI # Descomentar para error
from math import pi

print(math.pi)

print('=========================================')

## ValueError ##

my_int = '10'
print(type(my_int))
print(my_int)

print('+++++++++++++++++++++++++++++++++++++++++')

my_int = '10'
my_int = int(my_int)
print(type(my_int))
print(my_int)

print('+++++++++++++++++++++++++++++++++++++++++')

# my_int = '10 Años' # Descomentar para error
# my_int = int(my_int)
# print(type(my_int))
# print(my_int)

print('=========================================')

## ZeroDivisionError ##

print(4/2)

# print(4/0) # Descomentar para error