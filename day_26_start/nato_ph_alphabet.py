import pandas

nato_abc = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:

nato_abc_dict = {rows.letter:rows.code for (index, rows) in nato_abc.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Type a word to know it in NATO alphabet:\n')
word_list = [nato_abc_dict[letter.upper()] for letter in word]
print(word_list)