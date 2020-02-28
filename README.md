# solitaire
Solitaire in the terminal with python

# How to play
### Running
To start, simply run `python3 solitaire.py`

Or, play in browser at: https://solitaire.theohenson.repl.run/

### The game board
When started, the 7 columns of cards are displayed at the top.

The four (empty, if the program is just ran) piles where the stacks of suits go are under the columns.

Below the 4 piles, is the rest of the deck, with one card exposed.

### Cards
Cards' names consist of two letters, the first being the first letter of their suit, and the second being what type of card.

Face-down cards are representing with two hyphens.

I'm sure you can figure out how to interpret them.

### Commands
When explaining the commands, I assume already know how to play klondike solitaire.

#### To move a card from one column to another, run:

  `<source column #> <source row #> <destination column #>`

  For example:

  `3 4 2`: attempts to move the card in the `3`rd column that is `4` cards down, to the `2`nd column.
  
<hr>

#### To move a card from a column to its suit's pile, run:
  
  `a <source column #>`
  
  For example:
  
  `a 3`: attempts to move the card at the bottom of the `3`rd column to its suit's pile.
 
<hr>
  
#### To refer to the card on the top of the deck, use `0`

  For example:
  
  `0 5`: attempts to move the card on top of the deck to the bottom of column `5`
  
  `a 0`: attempts to move the card on top of the deck to its suit's pile

#### To draw a new card, simply press the enter key

# License
All files are licensed under the MIT License
