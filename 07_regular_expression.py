### Regular Expressions ###

## match

import re

my_string = 'Esta es la lección 7: Lección de Expresiones Regulares'
my_other_string = 'Esta no es la lección 6: Manejo de Ficheros'

print(re.match('Esta es la lección', my_string))

print('**********************************************************')

print(re.match('Esta es la lección', my_other_string))

print('**********************************************************')

print(re.match('Expresiones Regulares', my_string))

print('**********************************************************')

match = re.match('esta es la lección', my_string, re.I)
print(match)
print(match.span())

start, end = match.span()
print(my_string[start:end])

print('====================== Search =====================')

## search

search = re.search('lección', my_string, re.I)

print(search)

start, end = search.span()
print(my_string[start:end])

print('====================== Findall =====================')

## findall

findall = re.findall('lección', my_string, re.I)
print(findall)

findall_1 = re.findall('e', my_string, re.I)
print(findall_1)

print('====================== Split =====================')

## split

print(re.split('\n', my_string))
print(re.split(':', my_string))

print('====================== Sub =====================')

## sub

print(re.sub('lección|Lección', 'LECCIÓN', my_string))

print(re.sub('[l|L]ección', 'LECCIÓN', my_string))

print(re.sub('Expresiones Regulares', 'RegEx', my_string))

print('//////////////////////// Patterns ///////////////////////////')

## Patterns in Regular Expression

pattern = r'[l|L]ección'

print(re.findall(pattern, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_1 = r'[l|L]ección|Expresiones'

print(re.findall(pattern_1, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_2 = r'[0-9]'

print(re.findall(pattern_2, my_string))
print(re.search(pattern_2, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_3 = r'[\d]' # Encuentra todos los número y no los caractéres

print(re.findall(pattern_3, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_3 = r'[\D]' # Encuentra todos los caractéres y no los número

print(re.findall(pattern_3, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_4 = r'[l].' # Encuentra todos los caractéres y no los número

print(re.findall(pattern_4, my_string))

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

pattern_5 = r'[l].*' # Encuentra todos los caractéres y no los número

print(re.findall(pattern_5, my_string))

print('//////////////////////// Email Validation ///////////////////////////')

## Email Validation with Regular Expression

email = 'phurtado1112@gmail.com'

def is_valid_email(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return print(re.match(pattern, email))

is_valid_email(email)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

def is_valid_email_1(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return print(re.search(pattern, email))

is_valid_email_1(email)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

def is_valid_email_2(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return print(re.findall(pattern, email))

is_valid_email_2(email)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

email_1 = 'phurtado1112@gmail'

def is_valid_email_2(email_1):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  return print(re.findall(pattern, email_1))

is_valid_email_2(email_1)

print('+++++++++++++++++++++++++++++++++++++++++++++++++')

email_2 = 'phurtado1112@gmail.com.ni'

def is_valid_email_2(email_2):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$'
  return print(re.findall(pattern, email_2))

is_valid_email_2(email_2)