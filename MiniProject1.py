# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:01:54 2020

@author: amand
"""

import random
import pandas as pd
import numpy as np
import time

df = pd.read_csv('miniqbank.csv')


engineering_bank = df[df['category'] == 'Engineering For Dummies']
rosenberg_bank = df[df['category'] == 'Rosenberg Wisdom']
ru_bank = df[df['category'] == 'R-U-RAH-RAH']
new_jersey_bank = df[df['category'] == 'NeW jErSeY']
old_shows_bank = df[df['category'] == 'Old TV Shows']
sports_bank = df[df['category'] == 'Sports']
scorecard = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])

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
    elif colore == 'black':
        category = 'Sports'
    else:
        colore = colore        
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

def determine_player(num_player):
    if num_player == '4':
      fasest_player= input(print('press 1,2,3 or 4 then enter'))
    elif num_player == '3':
      fasest_player= input(print('press 1,2 or 3 then enter'))
    elif num_player == '2':
     fasest_player= input(print('press 1 or 2 then enter'))
    else:
      print ('number of player error from determine player')
    if fasest_player == '1':
        player = 'Player 1'
    elif fasest_player == '2':
        player = 'Player 2'
    elif fasest_player == '3':
        player = 'Player 3'
    elif fasest_player == '4' :
        player = 'Player 4'
    else:
        print('error fastest player')
    print('It is', player, '\'s turn')
    return player
    return fasest_player

def determine_new_player(fasest_player, num_player):
    if num_player == '4':
      fasest_player_2nd= input(print('press 1,2,3 or 4 then enter for second try'))
      while (fasest_player[-1] ==fasest_player_2nd):
        print('the same player cant try twice')
        fasest_player_2nd= input(print('press 1,2,3 or 4 then enter for second try'))
    elif num_player == '3':
      fasest_player_2nd= input(print('press 1,2 or 3 then enter for second try'))
      while (fasest_player[-1] ==fasest_player_2nd):
        print('the same player cant try twice')
        fasest_player_2nd= input(print('press 1,2 or 3 then enter for second try'))
    elif num_player == '2':
     fasest_player_2nd= input(print('press 1 or 2 then enter for second try'))
     while (fasest_player[-1] ==fasest_player_2nd):
        print('the same player cant try twice')
        fasest_player_2nd= input(print('press 1 or 2 then enter for second try'))
    else:
      print ('number of player error from determine player')
    
    if fasest_player_2nd == '1':
          newplayer = 'Player 1'
    elif fasest_player_2nd == '2':
          newplayer = 'Player 2'
    elif fasest_player_2nd == '3':
          newplayer = 'Player 3'
    elif fasest_player_2nd == '4' :
          newplayer = 'Player 4'
    else:
        print('error fastest player 2nd')
    print('It is now', newplayer,'\'s turn to answer')
    return newplayer

def display_q(question):
    print(question['question'].iloc[0]) 
    return

def get_guess():
    time.sleep(2)
    current = time.time()
    limit = current + 10
    guess = input('Answer here:')
    if time.time() < limit:
        guess = guess
    else:
        guess = 'Not valid'
        print('\nAnswer Not Accepted. Took too long to answer.')
        time.sleep(2)
    guess = guess.lower()
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
        print('\nCorrect!')
    else:
        print('\nIncorrect :( \n')
        
def remove_question(my_q):
    global df
    global engineering_bank
    global rosenberg_bank
    global ru_bank
    global new_jersey_bank
    global old_shows_bank
    global sports_bank
    df = df[df.index != my_q.index[0]]
    engineering_bank = df[df['category'] == 'Engineering For Dummies']
    rosenberg_bank = df[df['category'] == 'Rosenberg Wisdom']
    ru_bank = df[df['category'] == 'R-U-RAH-RAH']
    new_jersey_bank = df[df['category'] == 'NeW jErSeY']
    old_shows_bank = df[df['category'] == 'Old TV Shows']
    sports_bank = df[df['category'] == 'Sports']


def winning_points():
    global df
    global turn
    global scorecard

    i = 0
    player1sum,player1list = 0,scorecard[0]
    player2sum,player2list = 0,scorecard[1]
    player3sum,player3list = 0,scorecard[2]
    player4sum,player4list = 0,scorecard[3]

    #if player has answered every category
    if not 0 in player1list:
        print('player 1 wins!')
        turn = 62
    elif not 0 in player2list:
        print('player 2 wins!')
        turn = 62
    elif not 0 in player3list:
        print('player 3 wins!')
        turn = 62
    elif not 0 in player4list:
        print('player 4 wins!')
        turn = 62
    else:
        turn = turn
        
    while i < 6:
        player1sum += scorecard[0,i]
        player2sum += scorecard[1,i]
        player3sum += scorecard[2,i]
        player4sum += scorecard[3,i]
        i += 1
    # if there every question has been answered then max points win
    if len(df) == 1: 
        print('All questions have been answered!')
        if player1sum > player2sum and player1sum > player3sum and player1sum > player4sum:
            print('Player 1 wins!')
            turn = 62
        elif player2sum > player1sum and player2sum > player3sum and player2sum > player4sum:
            print('Player 2 wins!')
            turn = 62
        elif player3sum > player1sum and player3sum > player2sum and player3sum > player4sum:
            print('Player 3 wins!')
            turn = 62
        elif player4sum > player1sum and player4sum > player2sum and player4sum > player3sum:
            print('Player 4 wins!')
            turn = 62
        else:
            #if there is a tie, player with the most categories answered wins
            most_categories(player1list,player2list,player3list,player4list)
    else:
        turn = turn

def most_categories(player1list,player2list,player3list,player4list):
    global turn
    # the zeroes in the list are the categories unanswered
    p1_zeroes = np.count_nonzero(player1list==0)
    p2_zeroes = np.count_nonzero(player2list==0)
    p3_zeroes = np.count_nonzero(player3list==0)
    p4_zeroes = np.count_nonzero(player4list==0)
    if p1_zeroes < p2_zeroes and p1_zeroes < p3_zeroes and p1_zeroes < p4_zeroes:
        print('Player 1 wins!')
        turn = 62
    elif p2_zeroes < p1_zeroes and p2_zeroes < p3_zeroes and p2_zeroes < p4_zeroes:
        print('Player 2 wins!')
        turn = 62
    elif p3_zeroes < p1_zeroes and p3_zeroes < p2_zeroes and p3_zeroes < p4_zeroes:
        print('Player 3 wins!')
        turn = 62
    elif p4_zeroes < p1_zeroes and p4_zeroes < p2_zeroes and p4_zeroes < p3_zeroes:
        print('Player 4 wins!')
        turn = 62
    else:
        # if players have the same score and same unanswered categories
        # they break the tie
        tie_breaker(player1list,player2list,player3list,player4list)
    
def tie_breaker(player1,player2,player3,player4):
    
    global turn 
    playersname = ['Player 1','Player 2', 'Player 3','Player 4']
    playerscore = [player1,player2,player3,player4]
    highscore = np.amax(playerscore)
    # location vairable shows which players tied
    location = np.where(playerscore==highscore)[0] 
    n_way_tie = len(location)
    
    print('******************')
    print('***Tie Breaker!***')
    print('******************')
    print('there is a', n_way_tie, 'way tie!')
    print('the following order was chosen at random')
    
    if n_way_tie == 4:

        firstturn = playersname[random.randint(0,3)]
        playersname.remove(firstturn)
    
        secondturn = playersname[random.randint(0,2)]
        playersname.remove(secondturn)
        
        thirdturn = playersname[random.randint(0,1)]
        playersname.remove(thirdturn)
        
        fourthturn = playersname[0]
    
        print(firstturn,'goes first')
        print(secondturn, 'goes second')
        print(thirdturn, 'goes third')
        print(fourthturn,'goes fourth')
        orderofplayers = [firstturn,secondturn,thirdturn,fourthturn]
        mini_game(orderofplayers)     
        
    elif n_way_tie == 3:
        firstturn = playersname[random.randint(0,2)]
        playersname.remove(firstturn)   
        secondturn = playersname[random.randint(0,1)]
        playersname.remove(secondturn)       
        thirdturn = playersname[0]
        print(firstturn,'goes first')
        print(secondturn, 'goes second')
        print(thirdturn, 'goes third')
        orderofplayers = [firstturn,secondturn,thirdturn] 
        mini_game(orderofplayers)
        
    elif n_way_tie == 2:
        firstturn = playersname[random.randint[0,1]]
        playersname.remove(str(firstturn))
        print(firstturn,'goes first')
        secondturn = playersname[0]
        print(secondturn, 'goes second')
        orderofplayers = [firstturn,secondturn] 
        mini_game(orderofplayers)
        
    else:
        n_way_tie = n_way_tie
        
    return orderofplayers


def mini_game(tiebreakers):
# each player will answer the same question
    print('What does a rich man need that a poor person has?')
    answer = 'nothing'

# The random order makes it fair
# first player that answers question correctly wins
# if no players answer correctly, no one wins
    if len(tiebreakers) == 4:
        answer1 = input((tiebreakers[0])+'\'s answer:')
        answer1 = answer1.lower()
        if answer1 == answer:
            print(tiebreakers[0] + ' wins!')
        else:
            print('Incorrect!')
            answer2 = input(tiebreakers[1]+'\'s answer:')
            answer2 = answer2.lower()
            if answer2 == answer:
                print(tiebreakers[1]+'wins!')
            else:
                print('Incorrect!')
                answer3 = input(tiebreakers[2]+'\'s answer:')
                answer3 = answer3.lower()
                if answer3 == answer:
                    print(tiebreakers[2]+' wins!')
                else:
                    print('Incorrect!')
                    answer4 = input(tiebreakers[3]+'\'s answer:')
                    answer4 = answer4.lower()
                    if answer4 == answer:
                        print(tiebreakers[3]+' wins!')
                    else:
                        print('Incorrect!')
                        print('nobody wins!')
                        print('the correct answer is nothing!')
    elif len(tiebreakers) == 3:
        answer1 = input((tiebreakers[0])+'\'s answer:')
        answer1 = answer1.lower()
        if answer1 == answer:
            print(tiebreakers[0] + ' wins!')
        else:
            print('Incorrect!')
            answer2 = input(tiebreakers[1]+'\'s answer:')
            answer2 = answer2.lower()
            if answer2 == answer:
                print(tiebreakers[1]+'wins!')
            else:
                print('Incorrect!')
                answer3 = input(tiebreakers[2]+'\'s answer:')
                answer3 = answer3.lower()
                if answer3 == answer:
                    print(tiebreakers[2]+' wins!')
                else:
                    print('Incorrect!')
                    print('nobody wins!')
                    print('the correct answer is nothing!')
    elif len(tiebreakers) == 2:
        answer1 = input((tiebreakers[0])+'\'s answer:')
        answer1 = answer1.lower()
        if answer1 == answer:
            print(tiebreakers[0]+' wins!')
        else:
            print('Incorrect!')
            print(tiebreakers[1]+'\'s turn')
            answer2 = input(tiebreakers[1]+'\'s answer:')
            answer2 = answer2.lower()
            if answer2 == answer:
                print(tiebreakers[1]+' wins!' )
            else:
                print('nobody wins!')
                print('the correct answer is nothing!')
    else:
        tiebreakers = tiebreakers

def keep_score(category, player, valid):
    global scorecard
    if valid:
        if category == 'Engineering for Dummies':
            if player == 'Player 1':
                scorecard[0,0] = scorecard[0,0] + 1
            elif player == 'Player 2':
                scorecard[1,0] = scorecard[1,0] + 1
            elif player == 'Player 3':
                 scorecard[2,0] = scorecard[2,0] + 1
            else:
                 scorecard[3,0] = scorecard[3,0] + 1
               
        elif category == 'Rosenberg Wisdom' :
             if player == 'Player 1':
                scorecard[0,1] = scorecard[0,1] + 1
             elif player == 'Player 2':
                scorecard[1,1] = scorecard[1,1] + 1
             elif player == 'Player 3':
                 scorecard[2,1] = scorecard[2,1] + 1
             else:
                 scorecard[3,1] = scorecard[3,1] + 1
        elif category == 'R-U-RAH-RAH':
             if player == 'Player 1':
                scorecard[0,2] = scorecard[0,2] + 1
             elif player == 'Player 2':
                scorecard[1,2] = scorecard[1,2] + 1
             elif player == 'Player 3':
                 scorecard[2,2] = scorecard[2,2] + 1
             else:
                 scorecard[3,2] = scorecard[3,2] + 1
        elif category == 'NeW jErSeY':
             if player == 'Player 1':
                scorecard[0,3] = scorecard[0,3] + 1
             elif player == 'Player 2':
                scorecard[1,3] = scorecard[1,3] + 1
             elif player == 'Player 3':
                 scorecard[2,3] = scorecard[2,3] + 1
             else:
                 scorecard[3,3] = scorecard[3,3] + 1
        elif category == 'Old TV Shows':
             if player == 'Player 1':
                scorecard[0,4] = scorecard[0,4] + 1
             elif player == 'Player 2':
                scorecard[1,4] = scorecard[1,4] + 1
             elif player == 'Player 3':
                 scorecard[2,4] = scorecard[2,4] + 1
             else:
                 scorecard[3,4] = scorecard[3,4] + 1
        else:
             if player == 'Player 1':
                scorecard[0,5] = scorecard[0,5] + 1
             elif player == 'Player 2':
                scorecard[1,5] = scorecard[1,5] + 1
             elif player == 'Player 3':
                 scorecard[2,5] = scorecard[2,5] + 1
             else:
                 scorecard[3,5] = scorecard[3,5] + 1
    else:
        scorecard = scorecard
    print('\nLeaderboard:')
    print('Player1:',scorecard[0])
    print('Player2:',scorecard[1])
    print('Player3:',scorecard[2])
    print('Player4:',scorecard[3])
    return scorecard
            
       
def play_single_turn():
    global turn
    color = determine_color()
    category = determine_category(color)
    my_bank = get_correct_bank(category,engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank)
    stoploop = 0
    while my_bank.size == 0 and stoploop==0:
        color = determine_color()
        category = determine_category(color)
        my_bank = get_correct_bank(category,engineering_bank, rosenberg_bank, ru_bank, new_jersey_bank,old_shows_bank,sports_bank)
        if df.size == 0:
            stoploop = 1
        else:
            stoploop = 0
    my_q = select_question(my_bank)
    
    player = determine_player(num_player)
    
    display_q(my_q)
    print('------------------------------------')

    the_guess = get_guess()
    valid = check_answer(the_guess,my_q)
    give_feedback(valid)

    if not valid:
        newplayer = determine_new_player(player,num_player)
        display_q(my_q)
        the_guess = get_guess()
        valid = check_answer(the_guess,my_q)
        give_feedback(valid)
        keep_score(category, newplayer,valid)
        
    else:
        keep_score(category, player,valid)
    
    print('------------------------------------')
    print('      ')
    print('      ')
    winning_points()
    remove_question(my_q)
    return valid

turn=0
while turn < 60:
    points = 0
    print('*********************   TURN: ' + str(turn) + '   **********************')
    score = play_single_turn()
    turn += 1
