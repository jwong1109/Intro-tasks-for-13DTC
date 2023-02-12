"""Intro task 3
Count the number of 'e's in a string
"""

count = 0
sentence = input("Enter your sentence: ")

for char in sentence:
    if char == "e":
        count += 1
print(f"The character 'e' appears in the sentence '{sentence}' {count} times.")
