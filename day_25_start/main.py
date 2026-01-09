# new_list = [new_item for item in list if test]
new_list = [n + 1 for n in numbers]

name = 'Angela'

letters_list = [letter for letter in name]

even_list = [n * 2 for n in range(1, 5)]

names = ['Alex', 'Beth', 'Caroline', 'Dave', "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) <= 5]

LONG_names = [name.upper() for name in names if len(name) >= 5]

