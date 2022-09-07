# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:45:35 2022

@author: user
"""

import random

def display_guessed(word, guesses):
    """
    Check if any char in word appears in the guesses  list,
    if char appears, then added to a list, else a hyphen is added
    """
    out = []
    for char in word:
        if char in guesses:
            out.append(char)
        else:
            out.append('-')
    return ''.join(out)
            
def main():
    """
    Main function that generates a random word from a list of words
    It then displays the word in hyphens
    After a user makes a char guess, the char is searched from the word 
    where if the char is not present, a strike is added
    if quess is quit, the program terminates
    if guess in word, then the word is displayeds with chars replaced
    """
    
    strikes = 0
    words = ['python', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    
    print("Hangman game in Pythonm")
    
    guesses = []
    d_word = display_guessed(word, guesses)
    print()
    print("The word is: " + d_word)

    while True:
        guess = input("Guess character? [or quit to stop]: ")
        if guess.lower() == "quit":
            print("You quit, Bye!")
            break
        else:
            guess = guess.lower()
            guesses.append(guess)
            
        if guess.lower() not in word:
            strikes += 1
            print("Wrong entry . Right word " + word)
            if strikes == 5:
                print("You lose")
                break
        print("Letters guessed so far: " + ''.join(guesses))
        d_word = display_guessed(word, guesses)
        
        if d_word == word:
            print("You win!")
            break
        else:
            print("The word is: " + d_word)
            
main()

