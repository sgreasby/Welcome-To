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
expert = False
stack_cnt = 3
pass_ids = ["a","b","c"]
pass_idx = stack_cnt

usage = ("Usage: %s [-solo|--expert]\n")

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
construction_cards = [
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

#print( len(construction_cards))

plan1_cards = [
    ["Six 1-house estates",8,4],
    ["Four 2-house estates",8,4],
    ["Three 3-house estates",8,4],
    ["Two 4-house estates",6,3],
    ["Two 5-house estates",8,4],
    ["Two 6-house estates",10,6],
    # Advanced cards
    ["First and last house on every street",7,4],
    ["Seven temp agencies used", 6,3],
    ["Five Bis houses built", 6,3],
    ["Top street complete",6,3],
    ["Bottom street complete",8,4]
    ]

plan2_cards = [
    ["Three 1-house estates and one 6-house estate",11,6],
    ["One 5-house estate and two 2-house estates",10,6],
    ["Two 3-house estates and one 4-house estate",12,7],
    ["One 3-house estate and one 6-house estate",8,4],
    ["One 4-house estate and one 5-house estate",9,5],
    ["One 4-house estate and three 1-house estates",9,5],
    # Advanced cards
    ["All parks built on two streets",7,4],
    ["All pools built on two streets",7,4],
    ["One roundabout, all pools, and all parks built on one street",10,5],
    ["All pools and all parks built on middle street",8,3],
    ["All pools and all parks built on bottom street",10,5]
    ]

plan3_cards = [
    ["One 1-house estate, one 2-house estate, and one 6-house estate",12,7],
    ["One 1-house estate, one 4-house estate, and one 5-house estate",13,7],
    ["One 3-house estate and one 4-house estate",7,3],
    ["One 2-house estate and one 5-house estate",7,3],
    ["One 1-house estate, two 2-house estate, and one 3-house estate",11,6],
    ["One 2-house estate, one 3-house estate, and one 5-house estate",13,7]
    ]

basic_plan_cnt = len(plan3_cards)


####################################################################
# This function reads construction_cards into stacks
# Parameter: init - set True to shuffle deck
# Return: True if there are construction_cards remaining in deck,
#         False otherwise
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
        random.shuffle(construction_cards)
        if not expert:
            print("")
        if solo or expert:
            return

    else:
        # Print Headings
        if solo:
            print("%s  %s" % ("Number", "Effect"))
            print("%s  %s" % ("="*len("Number"), "="*effect_len))
        elif expert:
            print("")
            print("%s  %s  %s" % ("Pass", "Number", "Effect"))
            print("%s  %s  %s" % ("="*len("Pass"), "="*len("Number"), "="*effect_len))
        else:
            print("%s  %s  %s" % ("Number", "Effect".ljust(effect_len), "Preview"))
            print("%s  %s  %s" % ("="*len("Number"), "="*effect_len, "="*effect_len))

    # Populate stacks
    for stack_num in range(stack_cnt):
        if expert and stack_num==0 and pass_idx < stack_cnt:
            # If playing expert game, put passed card on stack 0
            number[0] = number[pass_idx]
            effect[0] = effect[pass_idx]
        else: # Not playing expert game or no construction_cards passed yet
            # Only the normal game (non-solo, non-expert) uses the effect from the previous card
            if not solo and not expert:
                prev_effect[stack_num] = effect[stack_num]

            # Read the next card
            number[stack_num] = construction_cards[card_num][0]
            effect[stack_num] = construction_cards[card_num][1]
            card_num += 1

            # If playing to solo game and the solo card comes up, indicate it and read another card
            if solo and effect[stack_num] == "solo":
                print( "################ SOLO ####################")
                number[stack_num] = construction_cards[card_num+stack_num][0]
                effect[stack_num] = construction_cards[card_num+stack_num][1]
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
            elif expert:
                print("   %s  %6d  %s" % (pass_ids[stack_num], number[stack_num], effect[stack_num]))
            else:
                print("%6d  %s  %s" % (number[stack_num], prev_effect[stack_num].ljust(effect_len), effect[stack_num]))
    
    if not init:
        print("\n%d cards remaining" % (len(construction_cards)-card_num))

    # Return value indicates if there are are enough construction_cards for another draw
    if expert:
        return card_num+stack_cnt-1 <= len(construction_cards)
    else:    
        return card_num+stack_cnt <= len(construction_cards)

# Parse Arguments
if len( sys.argv ) == 1:
    pass
elif len( sys.argv ) == 2:
    if (sys.argv[1] == "--solo"):
        solo = True
    elif (sys.argv[1] == "--advanced"):
        advanced = True
    elif (sys.argv[1] == "--expert"):
        advanced = True
        expert = True
    else:
        print( usage % sys.argv[0] )
        sys.exit()
else:
    print( usage % sys.argv[0] )
    sys.exit()

# Initialize Stacks
read_stacks(True)

plans = [[]]*3
if advanced:
    plans[0] = random.choice(plan1_cards)
    plans[1] = random.choice(plan2_cards)
else:
    plans[0] = random.choice(plan1_cards[:basic_plan_cnt])
    plans[1] = random.choice(plan2_cards[:basic_plan_cnt])

plans[2] = random.choice(plan3_cards)

plan_txt_cnt =62
print("Plan  First  Others  Objective")
print("%s  %s  %s  %s" % ("="*len("Plan"),"="*len("First"),"="*len("Others"),"="*plan_txt_cnt))
for plan_num,plan in enumerate(plans):
    print("%4d  %5d  %6d  %s"%(plan_num+1,plan[1],plan[2],plan[0]))
print("")

# If playing solo mode, shuffle "solo" card into bottom half of deck
if solo:
    top = construction_cards[:int((len(construction_cards)+1)/2)]
    bottom = construction_cards[int((len(construction_cards)+1)/2):]
    bottom += [[0,"solo"]]
    random.shuffle(bottom)
    construction_cards = top + bottom

# While there are construction_cards to draw into each stack
while read_stacks(False):
    valid_input = False

    # Prompt user for what to do next, based on the game mode and validate their response
    while not valid_input:
        if expert:
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

