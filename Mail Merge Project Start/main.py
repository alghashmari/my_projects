with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_template = letter.read()
    print(letter_template)

with open("Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
    cleaned_name = [name.strip() for name in name_list]
    print(cleaned_name)

for name in cleaned_name:
    new_letter = letter_template.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)