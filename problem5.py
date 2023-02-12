"""Intro task 5
Character to be found in a sentence
"""

numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
num_to_find = 353

if num_to_find in numbers:
    id_num_to_find = numbers.index(num_to_find)
    numbers[id_num_to_find] = 53

print(numbers)
