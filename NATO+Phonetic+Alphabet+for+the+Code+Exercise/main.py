# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


FILE_PATH = "D:/Python/100 days Python Challenge/Intermediate/day 30/NATO+Phonetic+Alphabet+for+the+Code+Exercise/nato_phonetic_alphabet.csv"

data = pandas.read_csv(FILE_PATH)
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phanetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError as key_erro :
        print(f"No such kind of key:{key_erro}")
        generate_phanetic()
    except TypeError as type_error :
        print(f"Only letters are allowed {type_error}")
    else:
        print(output_list)

generate_phanetic()
  
