
# Project speficiation

This TicTacToe game is design to be an application for playing TicTacToe against an AI opponent.

## Algorithm design

The idea is to create a MiniMax algorithm, which is an AI applied in two players game, such as TicTacToe. In specific, MiniMax is an algorithm that searches game trees and assumes that the players make alternate moves. Besides MiniMax, an Alpha-Beta pruning, an optimization technique for the Mini-Max algorithm, is implemented to the project. With the Alpha-Beta pruning, we are able to calculate the correct minimax decision without looking at every node in the game tree. This will reduce the computation time and allow us to search the game tree faster.

#### Time Complexity

As MiniMax performs DFS (Depth-First-Search), the time complecity is O(b^m). Ideally, with the help of Alpha-Beta pruning, the algorithm could adapt a time complecity of O(b^m/2) if DFS is applied to the left side of the tree. However, if DFS is applied to the right side of the tree, the time complexity will stay as O(b^m). In other words, the time complexity is dependent on the order in which each node is examined.

#### Space Complexity

The space complexity of the algorithm is O(bm) such as in DFS.

## Program input and output

The program will have a simple graphical user interface including a Main Menu and Game Menu. In the Main Menu, the user can choose the size of the game grid (3x3 or 25x25) and start the game. In the Game Menu, the user will see the game grid and by clicking a desired square, a cross is placed to the game grid. After this the AI player will make its own move and place a zero to the desired square. When game is over, the user can choose to play a new game or go back to the main menu.

## Programming and documentation language

In this project, Python is being used as a programming language and English is being used as a documentation language.

## Degree programme

Bachelor's in Computer Science

## Sources

https://www.javatpoint.com/mini-max-algorithm-in-ai

https://www.javatpoint.com/ai-alpha-beta-pruning



