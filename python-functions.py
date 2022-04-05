#  1 

from math import prod


def sum_to(num):
  sum = 0
  for n in range(1, num+1):
    sum += n
  return sum
print(sum_to(10))

sum_to(6)  # returns 21
sum_to(10) # returns 55


#  2

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
print(largest([1, 2, 3, 4, 0]))

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231


#  3

def occurances(string, letter):
  return string.count(letter)
print(occurances('fleep floop', 'ee'))

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0


#  4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
print(product(-1, 4))

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0