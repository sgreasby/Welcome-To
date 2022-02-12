#!/usr/bin/env python
###########################################################
"Welcome To... Card Drawing Program"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2021 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/Welcome-To"
__maintainer__ = "Steven Greasby"
###########################################################

import sys
import numpy as np
import random

solo = False
advanced = False
stack_cnt = 3
pass_ids = ["a","b","c"]
pass_idx = stack_cnt

usage = ("Usage: %s [-solo|--advanced]\n")

# Cards have front (number) and back (effect)
# Effects are:
effect_dict = {
    "S": "Surveyor",     # Build a fence between 2 houses
    "E": "Estate Agent", # Increase scoring of completed estates one step
    "L": "Landscaper",   # Add one park to the street where number is placed
    "P": "Pool",         # Complete pool on house where number is placed & increase pool value
    "T": "Temp Agency",  # Ajust present house value +/- 2 (min 0, max 17)
    "B": "Bis"           # Duplicate the number of an adjacent house, a fence cannot divide houses
    }
effect_len=12
cards = [
    [1,"S"],[1,"E"],[1,"L"],
    [2,"S"],[2,"L"],[2,"E"],
    [3,"S"],[3,"P"],[3,"T"],[3,"B"],
    [4,"P"],[4,"T"],[4,"B"],[4,"P"],[4,"E"],
    [5,"S"],[5,"S"],[5,"P"],[5,"P"],[5,"E"],[5,"E"],
    [6,"S"],[6,"S"],[6,"P"],[6,"T"],[6,"B"],[6,"L"],[6,"E"],
    [7,"S"],[7,"P"],[7,"T"],[7,"B"],[7,"L"],[7,"L"],[7,"E"],[7,"E"],
    [8,"S"],[8,"S"],[8,"P"],[8,"T"],[8,"B"],[8,"L"],[8,"L"],[8,"E"],[8,"E"],
    [9,"S"],[9,"P"],[9,"T"],[9,"B"],[9,"L"],[9,"L"],[9,"E"],[9,"E"],
    [10,"S"],[10,"S"],[10,"P"],[10,"T"],[10,"B"],[10,"L"],[10,"E"],
    [11,"S"],[11,"S"],[11,"L"],[11,"L"],[11,"E"],[11,"E"],
    [12,"P"],[12,"T"],[12,"B"],[12,"L"],[12,"E"],
    [13,"S"],[13,"P"],[13,"T"],[13,"B"],
    [14,"S"],[14,"L"],[14,"E"],
    [15,"S"],[15,"L"],[15,"E"]
    ]

#print( len(cards))

####################################################################
# This function reads cards into stacks
# Parameter: init - set True to shuffle deck
# Return: True if there are cards remaining in deck, False otherwise
# Note: The global variables are only used here but declared outside
# The scope of the function to allow them to be static.
####################################################################
card_num = 0
number = [0]*stack_cnt
effect = [0]*stack_cnt
prev_effect = [0]*stack_cnt
def read_stacks(init):
    global card_num
    global number
    global effect
    global prev_effect
    global pass_idx

    if init:
        card_num = 0
        random.shuffle(cards)
        if not advanced:
            print("")
        if solo or advanced:
            return

    else:
        # Print Headings
        if solo:
            print("%s  %s" % ("Number", "Effect"))
            print("%s  %s" % ("="*len("Number"), "="*effect_len))
        elif advanced:
            print("")
            print("%s  %s  %s" % ("Pass", "Number", "Effect"))
            print("%s  %s  %s" % ("="*len("Pass"), "="*len("Number"), "="*effect_len))
        else:
            print("%s  %s  %s" % ("Number", "Effect".ljust(effect_len), "Preview"))
            print("%s  %s  %s" % ("="*len("Number"), "="*effect_len, "="*effect_len))

    # Populate stacks
    for stack_num in range(stack_cnt):
        if advanced and stack_num==0 and pass_idx < stack_cnt:
            # If playing advanced game, put passed card on stack 0
            number[0] = number[pass_idx]
            effect[0] = effect[pass_idx]
        else: # Not playing advanced game or no cards passed yet
            # Only the normal game (non-solo, non-advanced) uses the effect from the previous card
            if not solo and not advanced:
                prev_effect[stack_num] = effect[stack_num]

            # Read the next card
            number[stack_num] = cards[card_num][0]
            effect[stack_num] = cards[card_num][1]
            card_num += 1

            # If playing to solo game and the solo card comes up, indicate it and read another card
            if solo and effect[stack_num] == "solo":
                print( "################ SOLO ####################")
                number[stack_num] = cards[card_num+stack_num][0]
                effect[stack_num] = cards[card_num+stack_num][1]
                card_num += 1
        
            # Use the effect dictionary to get the effect name from its code
            try:
                effect[stack_num] = effect_dict[effect[stack_num]]
            except:
                print("Card %d has invalid prev_effect %s" % (number[stack_num],effect[stack_num]))
                sys.exit()

        if not init:
            # Print the card data for the given game mode
            if solo:
                print("%6d  %s" % (number[stack_num], effect[stack_num]))
            elif advanced:
                print("   %s  %6d  %s" % (pass_ids[stack_num], number[stack_num], effect[stack_num]))
            else:
                print("%6d  %s  %s" % (number[stack_num], prev_effect[stack_num].ljust(effect_len), effect[stack_num]))
    
    if not init:
        print("\n%d cards remaining" % (len(cards)-card_num))

    # Return value indicates if there are are enough cards for another draw
    if advanced:
        return card_num+stack_cnt-1 <= len(cards)
    else:    
        return card_num+stack_cnt <= len(cards)

# Parse Arguments
if len( sys.argv ) == 1:
    pass
elif len( sys.argv ) == 2:
    if (sys.argv[1] == "--solo"):
        solo = True
    elif (sys.argv[1] == "--advanced"):
        advanced = True
    else:
        print( usage % sys.argv[0] )
        sys.exit()
else:
    print( usage % sys.argv[0] )
    sys.exit()

# Initialize Stacks
read_stacks(True)

# If playing solo mode, shuffle "solo" card into bottom half of deck
if solo:
    top = cards[:int((len(cards)+1)/2)]
    bottom = cards[int((len(cards)+1)/2):]
    bottom += [[0,"solo"]]
    random.shuffle(bottom)
    cards = top + bottom

# While there are cards to draw into each stack
while read_stacks(False):
    valid_input = False

    # Prompt user for what to do next, based on the game mode and validate their response
    while not valid_input:
        if advanced:
            cmd = input('Enter card to pass (a,b,c), s to reshuffle, or q to quit\n')
            for pass_idx,pass_id in enumerate(pass_ids):
                if cmd == pass_id:
                    valid_input = True
                    break
        else:
            cmd = input('Tap ENTER for next cards, s to shuffle, or q to quit\n')
            if cmd == "":
                valid_input = True

        if cmd == "s":
            valid_input = True
            read_stacks(True)
        elif cmd == "q":
            valid_input = True
            print("Bye!")
            sys.exit()

        if not valid_input:
            print("Invalid Input")

