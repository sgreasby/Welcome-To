# Description
This repository contains a card drawing script for the tabletop game "Welcome To"

# Requirements
The scrip is compatible with Python 2 and Python 3.

# Usage
The script is executed from the command line as shown below.

## Normal Mode
`python welcometo.py`  

This mode first displays three city plan cards. It then displays construction cards as three numbers and three effects. Players select the number and effect of one row.
A preview of the upcoming effect is also displayed along with the number of cards remaining.
Players can reshuffle or quit at any time.

### Example Output
The city plan cards are displayed as follows:
<pre>Plan  First  Others  Objective
====  =====  ======  ==============================================================
   1      8       4  Six 1-house estates
   2      9       5  One 4-house estate and three 1-house estates
   3     11       6  One 1-house estate, two 2-house estate, and one 3-house estate
</pre>
Where the first column is the plan number, the second column is the point value for the first player to complete the plan, the third column is the point value for all other players, and the fourth column is the plans objective.

The construction cards are displayed as follows:
<pre>Number  Effect        Preview
======  ============  ============
    10  Estate Agent  Temp Agency
     4  Estate Agent  Pool
     8  Pool          Estate Agent

72 cards remaining
Tap ENTER for next cards, s to shuffle, or q to quit1</pre>

## Advanced Mode
`python welcometo.py --advanced`  

This mode is identical to normal mode but it uses the advanced city plan cards.

## Solo Mode
`python welcometo.py --solo</code>`

This mode first displays three city plan cards. It then displays construction cards as three numbers and three effects. Player selects the number from one row and the effect from another row.
The number of cards remaining is also displayed.
Player can reshuffle or quit at any time.

In this mode a "Solo" card is shuffled into the bottom half of the deck. When that card is drawn, it is displayed along with the other cards to tell player to flip the city plan cards.

### Example Output
The city plan cards are displayed as shown in normal mode.

The construction cards are displayed as follows:
<pre>Number  Effect
======  ============
     7  Temp Agency
     6  Landscaper
    11  Surveyor

73 cards remaining
Tap ENTER for next cards, s to shuffle, or q to quit</pre>

## Expert Mode
`python welcometo.py --expert`

This mode first displays three city plan cards. Expert mode uses the advanced city plan cards. Next it displays construction cards as three numbers and three effects. Players select the number from one row and the effect from another row.
Players then specify the unused card to be passed to the next player.
The number of cards remaining is also displayed.
Players can reshuffle or quit at any time.

### Example Output
The city plan cards are displayed as shown in normal mode.

The construction cards are displayed as follows:
<pre>Pass  Number  Effect
====  ======  ============
   a      13  Bis
   b       9  Landscaper
   c       1  Surveyor

74 cards remaining
Enter card to pass (a,b,c), s to reshuffle, or q to quit</pre>
