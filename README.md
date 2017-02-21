# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: 
The constraint here is that if we have naked twins, both values can only appear in the boxes of those twins. So in each unit, we look for naked twins and remove their values from the other boxes in same unit.
The constraint propagate from the two naked twin boxes to all the other boxes of the same unit.
The solution will be faster because there will be less possible values to test in the search
function.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: 
We already applied constraint propagation to solve the usual sudoku problem.
The only difference here is that the constraint is propagated to diagonals of the puzzle while is was before only propagated to horizontal, vertical and 3x3 boxes.
To implement this constraint extension, we add the two diagonals in the units list so that all the constrain propagation functions we already implemented also apply to those diagonal units

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.