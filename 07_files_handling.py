### Files Handling ###

import os
## .txt file

text_file = open('./my_file.txt', 'r+', encoding='utf_8') # Leer y escribir
# text_file = open('./my_file.txt', 'r') # Leer
# texto = text_file.read()
# print(texto)
print('************** Text 0 *********************')
print(text_file.read())
# print(text_file.read(10))

print('**************** Text 1 *******************')
text_file_1 = open('./my_file.txt', 'r+', encoding='utf_8') # Leer y escribir

print(text_file_1.readline())
print(text_file_1.readline())

print('**************** Text 2 *******************')
text_file_2 = open('./my_file.txt', 'r+', encoding='utf_8') # Leer y escribir

# print(text_file_2.readlines())

for line in text_file_2.readlines():
  print(line)

print('**************** Text 3 *******************')
text_file_3 = open('./my_file.txt', 'r+', encoding='utf_8') # Leer y escribir

print(text_file_3.read())

text_file_3.write('\nAunque también me gustan Python y Java')

# for line in text_file_3.readlines():
#   print(line)

text_file_3.close()

# os.remove('./my_file.txt')

print('**************** file create *******************')

text_file_3 = open('./my_file1.txt', 'w+', encoding='utf_8')

text_file_3.write('Mi nombre es Pablo \nMi apellido es Hurtado \nMi edad es 60 años \ny mi lenguaje de programación favorito es PHP \nAunque también me gustan Python y Java')

text_file_3.read()

text_file_3.close()

print('======================== JSON Files ==============================')

## .json file

import json

json_file = open('file.json', 'w+', encoding='utf_8')

json_text = {
  'name':'Pablo', 
  'surname':'Hurtado', 
  'age':60, 
  'languages':['Python', 'PHP', 'Java'], 
  'website':'phdsystems.net'
  }

json.dump(json_text, json_file, indent=2)
# json_file.write(json_text)