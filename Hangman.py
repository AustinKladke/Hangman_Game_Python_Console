# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 01:54:54 2022

@author: akladke
"""

import random
from string import ascii_lowercase

########################
# Hangman logic script
########################

# Pick random word from text file
word_lst = []
with open("words.txt") as file:
    for word in file:
        word_lst.append(word)
# Randomly choose secret word from list of words
chosen_word = random.choice(word_lst).strip()

# Both of these lists should be the same length
# Used to keep track of letters in chosen word and for replacing underscores
# in chosen word print out when player guesses a word correctly
chosen_word_letters = []
chosen_word_underscores = []
for letter in chosen_word:
    chosen_word_letters.append(letter)
    chosen_word_underscores.append("_")

# Start game
print("****************** Hangman v1.0 ******************")
print("\n")

# Ask user what mode they want to play in: Easy, Medium or Hard
# Easy = 10 guesses
# Medium = 8 guesses
# Hard = 6 guesses
mode = ""
while mode not in ["Easy", "Medium", "Hard"]:
    mode = input("Choose Easy, Medium or Hard mode. Easy = 10 guesses, Medium = 8 guesses, Hard = 6 guesses\nSelect game mode: ")
if mode == "Easy":
    guesses_left = 10
if mode == "Medium":
    guesses_left = 8
if mode == "Hard":
    guesses_left = 6
    
# Variable that keeps track of max number of guesses
max_guesses_left = guesses_left

# Keep track of letters that have been guessed
guessed_letters = []
guessed_letters_dict = {} # {letter: # of times guessed}

# Loop until no more guesses are left (i.e. player loses) or until player
# guesses all of the letters correctly and wins
turn = 0
while guesses_left > 0:
    #print("Max guesses left: {}".format(max_guesses_left))
    if guesses_left == max_guesses_left and turn == 0:
        print("Secret word to guess: {}".format(" ".join(chosen_word_underscores)))
        print("No letters have been guessed yet")
    elif guesses_left == max_guesses_left:
        print("Secret word to guess: {}".format(" ".join(chosen_word_underscores)))
        print("Letters that have been guessed already: {}".format("".join(guessed_letters)))
        print("Guesses left: {}".format(guesses_left))
    elif guesses_left < max_guesses_left:
        print("Secret word to guess: {}".format(" ".join(chosen_word_underscores)))
        print("Letters that have been guessed already: {}".format("".join(guessed_letters)))
        print("Guesses left: {}".format(guesses_left))
        
        
    ################
    # Fix bug that decrements score by 1 even if letter has been guessed already
    # but is not in the word
    ################
    
    # Ask player to guess a letter, only let player make guesses that are
    # lowercase letters
    player_guess = "PLACEHOLDER"
    while player_guess not in ascii_lowercase and player_guess not in guessed_letters:
        player_guess = input("Guess a letter (a-z): ")
    if player_guess not in guessed_letters:
        guessed_letters.append(player_guess)
    if player_guess not in guessed_letters_dict:
        guessed_letters_dict[player_guess] = 1
    else:
        guessed_letters_dict[player_guess] += 1
        
    # See if letter is in secret word or not
    # If letter is in secret word, replace any letters in chosen_word_underscores
    # with letters in chosen_word_letters so that "Secret word to guess"
    # is updated for the user when the next turn occurs
    if player_guess in chosen_word:
        print("{} is in secret word".format(player_guess))
        for letter in range(len(chosen_word_letters)):
            if chosen_word_letters[letter] == player_guess:
                chosen_word_underscores[letter] = player_guess
    
    # If letter is not in secret word, let the player know this and then
    # decrement guesses left by 1
    if player_guess not in chosen_word and guessed_letters_dict[player_guess] <= 1:
        print("{} is not in secret word".format(player_guess))
        guesses_left -= 1

    # If all letters have been guessed correctly, exit out of the while loop
    # and let the player know that he won
    if chosen_word_letters == chosen_word_underscores:
        print("\nYou guessed the word correctly!!! The secret word is {}".format(chosen_word))
        break
    
    # If guesses_left = 0, exit out of the while loop and let the player
    # know that they lost
    if guesses_left == 0:
        print("\nYou lost! The secret word was {}".format(chosen_word))
        break
    
    turn += 1

print("\n****************** End of game ******************")


