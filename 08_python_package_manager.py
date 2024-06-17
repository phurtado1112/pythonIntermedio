### Package Manager ###

## PIP https://pypi.org

# import pandas # No se puede porque no tenemos el paquete instalado

'''
 Comandos de pip

 pip --version

 pip install (el paquete)

 pip install --upgrade (el paquete)

 pip list

 pip unistall (el paquete)

 pip show (el paquete)
'''

import numpy

import mypackage.arithmetics

print(numpy.version.version)

import pandas

import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(response)
print(response.status_code)
print(response.json())

print('============================================================')

## Arithmetics Package
import mypackage

print(mypackage.arithmetics.sum_two_values(2, 3))

print('++++++++++++++++++++++++++++++++++++++++++++++++++++')

# Acceso directo al archivo arithmetics.py en el paquete mypackage
from mypackage import arithmetics

print(arithmetics.sum_two_values(3, 4))