### Problem 1: Calculate Q from the Given Formula

import math

def calculate_Q(D_values):
    C = 50
    H = 30
    result = []
    for D in D_values:
        Q = math.sqrt((2 * C * D) / H)
        result.append(int(Q))
    return result

D_input = input("Enter comma-separated values for D: ")
D_values = [int(x) for x in D_input.split(",")]
result = calculate_Q(D_values)
print(",".join(map(str, result)))

### Problem 2: Generate a 2-Dimensional Array

def generate_2d_array(X, Y):
    array = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        array.append(row)
    return array

X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))

result = generate_2d_array(X, Y)
for row in result:
    print(row)

### Problem 3: Sort Words Alphabetically

def sort_words(input_sequence):
    words = input_sequence.split(",")
    words.sort()
    return ",".join(words)

input_sequence = input("Enter comma-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print(sorted_sequence)


### Problem 4: Remove Duplicates and Sort Words


def remove_duplicates_and_sort(input_sequence):
    words = input_sequence.split()
    unique_words = sorted(set(words))
    return " ".join(unique_words)

input_sequence = input("Enter whitespace-separated sequence of words: ")
sorted_unique_sequence = remove_duplicates_and_sort(input_sequence)
print(sorted_unique_sequence)

### Problem 5: Count Letters and Digits


def count_letters_and_digits(input_sentence):
    letters = sum(c.isalpha() for c in input_sentence)
    digits = sum(c.isdigit() for c in input_sentence)
    return letters, digits

input_sentence = input("Enter a sentence: ")
letters, digits = count_letters_and_digits(input_sentence)
print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")


### Problem 6: Validate Passwords

import re

def validate_password(password):
    if (6 <= len(password) <= 12 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[@$#]", password)):
        return True
    else:
        return False

def check_passwords(passwords):
    valid_passwords = []
    for password in passwords:
        if validate_password(password):
            valid_passwords.append(password)
    return valid_passwords

password_input = input("Enter comma-separated passwords to validate: ")
passwords = password_input.split(",")
valid_passwords = check_passwords(passwords)
print(",".join(valid_passwords))
