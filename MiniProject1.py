# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:53:37 2020

@author: amand
"""

import random
import pandas as pd
import numpy as np

df = pd.read_csv('miniqbank.csv')


engineering_bank = df[df['category'] == 'Engineering For Dummies']
rosenberg_bank = df[df['category'] == 'Rosenberg Wisdom']
ru_bank = df[df['category'] == 'R-U-RAH-RAH']
new_jersey_bank = df[df['category'] == 'NeW jErSeY']
old_shows_bank = df[df['category'] == 'Old TV Shows']
sports_bank = df[df['category'] == 'Sports']
scorecard = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0]])

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
    print('The category is:',category)
    return category
    
def get_correct_bank(category, engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank):
    if category == 'Engineering for Dummies':
        return engineering_bank
    elif category == 'Rosenberg Wisdom':
        return rosenberg_bank
    elif category == 'R-U-RAH-RAH':
        return ru_bank
    elif category == 'NeW jErSeY':
        return new_jersey_bank
    elif category == 'Old TV Shows':
        return old_shows_bank
    else: 
        return sports_bank
        
    
def select_question(correct_bank):
    question = correct_bank.sample(n=1)
    return question

def determine_player():
    rand_turn = random.randint(1,2)
    if rand_turn == 1:
        player = 'Player 1'
    else:
        player = 'Player 2'
    print('It is', player, '\'s turn')
    return player

def display_q(question):
    print(question['question'].iloc[0]) #change this
    return

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

def keep_score(category, player, valid):
    global scorecard
    if valid:
        if category == 'Engineering for Dummies':
            if player == 'Player 1':
                scorecard[0,0] = scorecard[0,0] + 1
            else:
                scorecard[1,0] = scorecard[1,0] + 1
        elif category == 'Rosenberg Wisdom' :
            if player == 'Player 1':
                scorecard[0,1] = scorecard[0,1] + 1
            else:
                scorecard[1,1] = scorecard[1,1] + 1
        elif category == 'R-U-RAH-RAH':
            if player == 'Player 1':
                scorecard[0,2] = scorecard[0,2] + 1
            else:
                scorecard[1,2] = scorecard[1,2] + 1
        elif category == 'NeW jErSeY':
            if player == 'Player 1':
                scorecard[0,3] = scorecard[0,3] + 1
            else:
                scorecard[1,3] = scorecard[1,3] + 1
        elif category == 'Old TV Shows':
            if player == 'Player 1':
                scorecard[0,4] = scorecard[0,4] + 1
            else:
                scorecard[1,4] = scorecard[1,4] + 1
        else:
            if player == 'Player 1':
                scorecard[0,5] = scorecard[0,5] + 1
            else:
                scorecard[1,5] = scorecard[1,5] + 1
    else:
        scorecard = scorecard
    print(scorecard)
    return scorecard
            
       
def play_single_turn():
    color = determine_color()
    category = determine_category(color)
    my_bank = get_correct_bank(category,engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank)
    my_q = select_question(my_bank)

    player = determine_player()
    
    display_q(my_q)
    the_guess = get_guess()
    valid = check_answer(the_guess,my_q)
    give_feedback(valid)
    score = keep_score(category, player,valid)
    remove_question(my_bank,my_q)
    return valid

i=0
while i < 5:
    points = 0
    score = play_single_turn()
    i += 1
