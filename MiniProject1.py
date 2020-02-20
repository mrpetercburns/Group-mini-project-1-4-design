# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:53:37 2020

@author: amand
"""

from random import randint
import pandas as pd

df = pd.read_csv('miniqbank.csv')


engineering_bank = df[df['Category'] == 'Engineering for Dummies']
rosenberg_bank = df[df['Category'] == 'Rosenberg Wisdom']
ru_bank = df[df['Category'] == 'R-U-RAH-RAH']
new_jersey_bank = df[df['Category'] == 'NeW jErSeY']
old_shows_bank = df[df['Category'] == 'Old TV Shows']
sports_bank = df[df['Category'] == 'Sports']


def determine_color():
    #randint must be changed when we use hardware to detect color
    #all color names below are subject to change based on what colors are on the die
    my_rand = randint(1,6)
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

def determine_category(color):
#all color names below are subject to change based on what colors are on the die
    if color == 'blue':
        category = 'Engineering for Dummies'
    elif color == 'red':
        category = 'Rosenberg Wisdom'
    elif color == 'green':
        category = 'R-U-RAH-RAH'
    elif color == 'yellow':
        category = 'NeW jErSeY'
    elif color == 'white':
        category = 'Old TV Shows'
    else:
        category = 'Sports'
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
        return
    elif category == 'NeW jErSeY':
         #return random question from NJ bank
        return
    elif category == 'Old TV Shows':
         #return random question from TV bank
        return
    else: 
        #return random question from Sports bank
        return
        
#finish this above   
    
def select_question(correct_bank):
    question = correct_bank.sample(n=1)
    return question

def display_q(question):
    print(question['question'].iloc(0)) #change this
    return

def get_guess():
    guess = input('Answer here:')
    return guess

def check_answer(user_guess, question):
    answer = question['answer'].iloc()
    if user_guess == answer:
       return True
    else:
       return False
   
def give_feedback(valid):
    if valid:
        print('Correct!')
    else:
        print('Incorrect :()')
        
def remove_question(my_bank, my_q):
    my_bank = my_bank[my_bank.index != my_q.index[0]]
    return my_bank

#def keep_score():
    #finish this
#    return sad
        
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

i=0
while i < 3:
    points = 0
    score = play_single_turn()
    if score:
        points += 1
    i += 1
