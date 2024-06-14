### Higher Order Functions ###

from functools import reduce


def sum_one(value):
  return value + 1

def sum_two_values_and_one(first_value, second_value):
  return first_value + second_value + 1


print(sum_one(6))

print(sum_two_values_and_one(2, 3))

print('++++++++++++++++++++++++++++++++++++++++++++')

def sum_two_values_and_add_one(first_value, second_value):
  return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(2, 3))

print('++++++++++++++++++++++++++++++++++++++++++++')

def sum_two_values_and_add_value(first_value, second_value, f_sum):
  return f_sum(first_value + second_value)

def sum_five(value):
  return value + 5

print(sum_two_values_and_add_value(2, 3, sum_one))

print(sum_two_values_and_add_value(2, 3, sum_five))

print('================================================')

### Closures ###

def sum_ten(original_value):
  def add_value(value):
    return value + 10 + original_value
  return add_value

add_closure = sum_ten(1)

print(add_closure(5))

print(sum_ten(1)(5))

print('================================================')

### Built-in Higher Order Functions ###

## Map ##

numbers = [2, 5, 10, 21]

def multiply_by_two(number):
  return number * 2

print(map(multiply_by_two, numbers))

print(list(map(multiply_by_two, numbers)))

print(list(map(lambda number: number * 2, numbers)))

print('++++++++++++++++++++++++++++++++++++++++++++++++++')

## Filter ##

numbers = [2, 5, 10, 21, 3, 30]

def filter_graeter_than_ten(number):
  if number > 10:
    return True
  else:
    return False
  
print(list(filter(filter_graeter_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

print('++++++++++++++++++++++++++++++++++++++++++++++++++')

## Reduce ##

numbers = [2, 5, 10, 21, 3, 30]

def sum_two_value(first_value, second_value):
  return first_value + second_value

print(reduce(sum_two_value, numbers))