
# Project speficiation

This TicTacToe game is designed to be an application for playing TicTacToe against an AI opponent.

## Algorithm and Data Structure design

The idea is to create a MiniMax algorithm, which is an decision-making AI applied in two players game, such as TicTacToe. In specific, MiniMax is a backtracking algorithm that searches game trees (nested data structures) and assumes that the players make alternate moves, and therefore this algorithm is suitable for this specific project.

Besides MiniMax, an Alpha-Beta pruning, an optimization technique for the Mini-Max algorithm, is implemented to the project. With the Alpha-Beta pruning, we are able to calculate the correct minimax decision without looking at every node in the game tree. This will reduce the computation time and allow us to search the game tree faster.

#### Time Complexity

As MiniMax performs DFS (Depth-First-Search), the time complecity is O(b^m). Ideally, with the help of Alpha-Beta pruning, the algorithm could adapt a time complecity of O(b^m/2) if DFS is applied to the left side of the tree. However, if DFS is applied to the right side of the tree, the time complexity will stay as O(b^m). In other words, the time complexity is dependent on the order in which each node is examined.

#### Space Complexity

The space complexity of the algorithm is O(bm) such as in DFS.

## Program input and iutput

The program will have a simple graphical user interface. The user will see the 25x25 game grid and by clicking a desired square, a cross is placed to the game grid. Based on the input given by the user, the AI player will make its own move (output) by placing a zero to the desired square. The user will see AI player's output and continues with new input. This continues until either human or AI has won the game. When the game is over, the player can choose to play a new game or end the game.

## Programming and documentation language

In this project, Python is being used as a programming language and English is being used as a documentation language.

## Degree programme

Bachelor's in Computer Science

## Sources

https://www.javatpoint.com/mini-max-algorithm-in-ai

https://www.javatpoint.com/ai-alpha-beta-pruning

https://towardsdatascience.com/how-a-chess-playing-computer-thinks-about-its-next-move-8f028bd0e7b1




