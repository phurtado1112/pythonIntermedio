### List Comprenhension ###

my_original_list = [25, 34, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]
print(my_list)

print('=======================================')

my_new_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_new_original_list)

my_range = [i for i in range(8)]
print(my_range)

my_new_range = range(8)
print(my_new_range)

my_new_list = [i for i in my_range]
print(my_new_list)

print('=======================================')

my_list_suma = [i + 1 for i in my_new_range]
print(my_list_suma)

my_list_resta = [i - 1 for i in my_new_range]
print(my_list_resta)

my_list_multiplica_por_dos = [i * 2 for i in my_new_range]
print(my_list_multiplica_por_dos)

my_list_multiplica_por_si_misma = [i * i for i in my_new_range]
print(my_list_multiplica_por_si_misma)

def sum_five(number):
  return number + 5

my_list_suma_cinco = [sum_five(i) for i in my_new_range]
print(my_list_suma_cinco)