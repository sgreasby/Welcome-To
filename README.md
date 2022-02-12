# Welcome To
Get more info about the theory at https://hadamardcodes.com

## Description
This repository contains a card drawing script for the tabletop game "Welcome To"

## Requirements
The scrip is compatible with Python 2 and Python 3.

## Usage
The script is executed from the command line as shown below.

### Normal Mode
`python welcometo.py`  

This mode displays three numbers and three effects. Players select the number and effect of one row.
A preview of the upcoming effect is also displayed along with the number of cards remaining.
Players can reshuffle or quit at any time.

####Example Output:

Number  Effect        Preview
======  ============  ============
    10  Estate Agent  Temp Agency
     4  Estate Agent  Pool
     8  Pool          Estate Agent

72 cards remaining
Tap ENTER for next cards, s to shuffle, or q to quit

### Solo Mode
`python welcometo.py --solo`  

This mode displays three numbers and three effects. Player selects the number from one row and the effect from another row.
The number of cards remaining is also displayed.
Player can reshuffle or quit at any time.

In this mode a "Solo" card is shuffled into the bottom half of the deck. When that card is drawn, it is displayed along with the other cards to tell player to flip the city plan cards.

####Example Output

Number  Effect
======  ============
     7  Temp Agency
     6  Landscaper
    11  Surveyor

73 cards remaining
Tap ENTER for next cards, s to shuffle, or q to quit

### Advanced Mode
`python welcometo.py --advanced`  

This mode displays three numbers and three effects. Players select the number from one row and the effect from another row.
Players then specify the unused card to be passed to the next player.
The number of cards remaining is also displayed.
Players can reshuffle or quit at any time.

####Example Output

Pass  Number  Effect
====  ======  ============
   a      13  Bis
   b       9  Landscaper
   c       1  Surveyor

74 cards remaining
Enter card to pass (a,b,c), s to reshuffle, or q to quit


