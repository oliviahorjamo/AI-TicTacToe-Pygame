# Week 5

[Hour reporting](https://github.com/riikkayoki/TicTacToe/blob/master/documentation/hour_reporting.md)

## What has happened during week 5

* Making the algorithm to work in 15x15 game board.
  => I changed the winning check conditions.
  => The minimax is now only looking for the neighbors of positions where the players have inserted a move.


## Problems

The code is showing 'index out of range' error when clicking the last row and column.


## Questions

I noticed that my algorithm is only working when 'isMaximizerPlayer' is set to false in minimax() and find_best_move() methods in ai_player.py file. I do not understand why. Are you able to answer that question?

## Next week

I will try to make the algorithm more faster and fix 'index out of range' problem.