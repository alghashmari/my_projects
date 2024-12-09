student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

# Load the NATO phonetic alphabet data
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        # Attempt to create the list without filtering
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        # Handle non-alphabetic characters
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # Prompt the user again
    else:
        # Successfully created the phonetic list
        print(output_list)

generate_phonetic()

