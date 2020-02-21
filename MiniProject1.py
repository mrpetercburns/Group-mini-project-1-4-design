# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:53:37 2020

@author: amand
"""

import random
import pandas as pd

df = pd.read_csv('miniqbank.csv')


engineering_bank = df[df['category'] == 'Engineering for Dummies']
rosenberg_bank = df[df['category'] == 'Rosenberg Wisdom']
ru_bank = df[df['category'] == 'R-U-RAH-RAH']
new_jersey_bank = df[df['category'] == 'NeW jErSeY']
old_shows_bank = df[df['category'] == 'Old TV Shows']
sports_bank = df[df['category'] == 'Sports']
#players = int(input('How many players?:')

#def determine_players(players):   
#    if players in range(2,5):
#       return players
#   else:
#       print('Incorrent amount of players. Please enter a number between 2 and 4')
#       players = int(input('How many players?:'))


def determine_color():
    #randint must be changed when we use hardware to detect color
    #all color names below are subject to change based on what colors are on the die
    my_rand = random.randint(1,6)
    if my_rand == 1:
        color = 'blue'
    elif my_rand == 2:
        color = 'red'
    elif my_rand == 3:
        color = 'green'
    elif my_rand == 4:
        color = 'yellow'
    elif my_rand == 5:
        color = 'white'
    else: 
        color = 'black'
    return color


def determine_category(colore):
##all color names below are subject to change based on what colors are on the die
    if colore == 'blue':
        category = 'Engineering for Dummies'
    elif colore == 'red':
        category = 'Rosenberg Wisdom'
    elif colore == 'green':
        category = 'R-U-RAH-RAH'
    elif colore == 'yellow':
        category = 'NeW jErSeY'
    elif colore == 'white':
        category = 'Old TV Shows'
    else:
        category = 'Sports'
    print(category)
    return category
    
def get_correct_bank(category, engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank):
    if category == 'Engineering for Dummies':
        #return random question from engineering bank
        return engineering_bank
    elif category == 'Rosenberg Wisdom':
         #return random question from rosenberg bank
        return rosenberg_bank
    elif category == 'R-U-RAH-RAH':
         #return random question from RU bank
        return ru_bank
    elif category == 'NeW jErSeY':
         #return random question from NJ bank
        return new_jersey_bank
    elif category == 'Old TV Shows':
         #return random question from TV bank
        return old_shows_bank
    else: 
        #return random question from Sports bank
        return sports_bank
        
    
def select_question(correct_bank):
    question = correct_bank.sample(n=1)
    return question

def display_q(question):
    print(question['question'].iloc[0]) #change this
    return

#def whose_turn():        
#    return player

def get_guess():
    guess = input('Answer here:')
    return guess

def check_answer(user_guess, question):
    answer = question['answer'].iloc[0]
    simple_answer = answer.lower()
    simple_guess = user_guess.lower()
    if simple_guess == simple_answer:
        return True
    else:
        return False
   
def give_feedback(valid):
    if valid:
        print('Correct!')
    else:
        print('Incorrect')
        
def remove_question(my_bank, my_q):
    my_bank = my_bank[my_bank.index != my_q.index[0]]
    return my_bank

##def keep_score():
#    #finish this
###    return sad
#        
def play_single_turn():
    color = determine_color()
    category = determine_category(color)
    my_bank = get_correct_bank(category,engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank)
    my_q = select_question(my_bank)

    display_q(my_q)
    the_guess = get_guess()
    valid = check_answer(the_guess,my_q)
    give_feedback(valid)
    remove_question(my_bank,my_q)
    return valid

#def categorize_score(valid):
#    #here's where we would identify who to allocate points to and for what category
i=0
while i < 1:
    points = 0
    score = play_single_turn()
    if score:
        points += 1
    i += 1
