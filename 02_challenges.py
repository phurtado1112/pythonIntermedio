### Challenges ###

print('====================== FIZZ - BUZZ ========================')

"""
"FIZZ - BUZZ"

Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 """

def fizzbuzz():
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print('fizzbuzz')
    elif i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    else:
      print(i)

fizzbuzz()

print('====================== ANAGRAMA ========================')

"""
ANAGRAMA

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
 
"""

def is_anagram(word_one, word_two):
  print(word_one.lower())
  print(word_two.lower())
  print('++++++++++++++++++++++++++++++++++++++')
  print(sorted(word_one.lower()))
  print(sorted(word_two.lower()))
  print('++++++++++++++++++++++++++++++++++++++')

  if word_one.lower() == word_two.lower():
    return False
  return sorted(word_one.lower()) == sorted(word_two.lower())

compare = is_anagram('Amor', 'Roma')

print(compare)

print('////////////////////////////////////////////////')

compare = is_anagram('carro', 'orrac')

print(compare)

print('===================== FIBONACCI =========================')

"""
SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...

"""

def fibonacci():
  prev_value = 0
  next_value = 1

  for i in range(1, 51):
    # print(str(i) + '- ' + str(prev_value))
    print(f'{i} - {prev_value}')

    fib = prev_value + next_value

    prev_value = next_value

    next_value = fib


fibonacci()

print('====================== NÚMERO PRIMO ========================')

"""
NÚMERO PRIMO

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.

"""

def is_prime():
  for number in range(1, 101):
    if number >= 2:

      is_divisible = False

      for i in range(2, number):
        if number % i == 0:
          is_divisible = True
          break

      if not is_divisible:
        print(number)

is_prime()

print('====================== INVERTIR CADANA ========================')

"""
INVERTIR CADANA

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""

def reverse(text):
  reversed_text = ''
  text_len = len(text)

  for index in range(0, text_len):
    # print(f'el index es {index} de {len(text)}' )
    # print(text[index])
    reversed_text += text[text_len - index - 1]

  return reversed_text

print(reverse('Hola mundo'))