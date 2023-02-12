"""Intro task 4
Character to be found in a sentence
"""


# Function to count character in string
def count_character(letter, to_find):
    number = 0
    for item in to_find:
        if item == letter:
            number += 1

    return number


# Main Routine
character = input("Enter the character to be found in the sentence: ")
sentence = input("Enter the sentence in which to search: ")
count = count_character(character, sentence)

print(f"The character appears in the sentence '{sentence}' {count} times!")
