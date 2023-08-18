#!/usr/bin/env python3

def return_evens(sequence):
    even_numbers = [n for n in sequence if n % 2 == 0]
    return even_numbers

# Example usage
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Prints the list of even elements

def make_exclamation(sentence_list):
    exclaimed_sentence = [n+ "!" for n in sentence_list]
    return exclaimed_sentence