# solitaire
![image](https://i.ibb.co/0jxzvd7/solitaire.png)

# How to play
The rest of this file assumes you already know how to play [Klondike solitaire](https://en.wikipedia.org/wiki/Klondike_\(solitaire\)).

### Running
To start, simply run the file `solitaire.py` with a Python 3 interpreter.

Or play on the web at https://solitaire.theohenson.repl.run.

### The game board
When started, the seven columns of cards are displayed at the top.

The four foundations (where stacks of suits go) are located under the columns.

Below the four foundations is the rest of the deck, with one card exposed.

### Cards
Cards' names consist of two letters, the first being the first letter of their suit, and the second representing the type of the card.

Face-down cards are shown with two hyphens.

### Commands

The game is controlled via typed commands.

Under all the cards will be a prompt to enter said commands (shown as `solitaire> `).

#### To move a card from one column to another, run:

  `<source column #> <source row #> <destination column #>`

  For example:

  `3 4 2`: attempts to move the card in the `3`rd column that is `4` cards down, to the `2`nd column.
  
#### To move a card from a column to its suit's foundations, run:
  
  `a <source column #>`
  
  For example:
  
  `a 3`: attempts to move the card at the bottom of the `3`rd column to its suit's foundation.
 
#### To refer to the card on the top of the deck, use `0`

  For example:
  
  `0 5`: attempts to move the card on top of the deck to the bottom of column `5`.
  
  `a 0`: attempts to move the card on top of the deck to its suit's foundation.

#### To draw one new card press enter 

# License
All files are licensed under the MIT License.
