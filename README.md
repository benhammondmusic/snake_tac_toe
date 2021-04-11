# Snake-Tac-Toe

> Command line Tic-Tac-Toe game written in Python in 2 hours as a group project

![Screen grab of command line game play](snake_tac_toe.gif)

## Tech

- Python

## Classes

We were required to implement classes in this Python coding exercises, so our group started by brainstorming the various entities present in a game of Tic Tac Toe, and which of those would be best represented by a class, and which would be better represented as properties of a class instance. The two classes we decided on were:

- `Game`: would represent rounds of the game, and would keep track of who's turn it was, which squares were filled, etc
- `GamePiece`: would represent the objects filling each square on the `Game`'s `gameboard[]` list.

## Tricky Bits

### Checking for Win

The logic behind win a "win" relies on iterating over an array of all possible win conditions, and checking the current state of the board against each. We struggled getting these checks to work, until we finally isolated the bug: we were comparing the string `'O'` or `'X'` to the _**object**_ `GamePiece`, rather than the string _**property**_`GamePiece.mark` as we intended.

### Checking for Tie

Another issue with the logic involved the tie condition; there were two ways we discussed that could check for a tie:

- Track total played pieces, and if it reaches 9 and there's no winner, it's a tie
- Scan for empty spaces; once there are none left (and no winner), it's a tie
