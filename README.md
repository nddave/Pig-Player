# Pig-Player

![alt tag](https://raw.githubusercontent.com/nddave/Pig-Player/master/Pig%20Player.png)

Using dynamic programming and randomness, this program computes the most optimal strategy for two-player Pig game. It specifies, for any given score, the optimal turn total to roll until.

# What is Pig?

[Pig](https://en.wikipedia.org/wiki/Pig_(dice_game)) is a dice game for two players. The players take turns rolling a six-sided die. On each turn, the current player rolls, adding up the total of the rolls. The player can stop rolling at any time; when the current player ends the turn voluntarily then the current turn total is added to the player's score. However, if the current player rolls a 1 then the turn is over with no points gained. The first player to a predetermined target (often 100) wins the game.

# Getting started

The program takes in the following inputs:

* T, the score needed to win the game (argv 1)
* p1, the current score of player 1   (argv 2)
* p2, the current score of player 2   (argv 3)

And gives out the following outputs:

* wins(∞, p1, p2), the expected number of wins for player 1 when the score is p1 to p2, assuming optimal play
* the optimal turn total to roll until

Therefore, the following command:

> python pig_solver.py 100 22 0

will give the following output:

> 197 iterations
> 0.6940984814532153 19

# License information ![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

Program is created by [Nirman Dave](http://www.nirmandave.com) as a form of assignment for *Data Structures and Algorithms 1 COSC201* course at *Amherst College, Amherst MA* under *Professor James Glenn*.
