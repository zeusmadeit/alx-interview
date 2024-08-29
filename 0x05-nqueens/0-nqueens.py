#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.

Usage: nqueens N
- If the user called the program with the wrong number
of arguments, print Usage: nqueens N, followed by a new line,
and exit with the status 1 where N must be an integer greater or equal to 4
- If N is not an integer, print N must be a number, followed by a new line,
and exit with the status 1
- If N is smaller than 4, print N must be at least 4, followed by a new line,
and exit with the status 1
- The program should print every possible solution to the problem One solution per line

Format: see example
You don't have to print the solutions in a specific order
You are only allowed to import the sys module
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]

    Args:
    board (List[List[int]]): The current state of the chessboard
    row (int): The row to check
    col (int): The column to check
    n (int): The size of the board

    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # If we get here, it's safe to place a queen
    return True


def solve_nqueens(n):
    """
    Solve the N Queens puzzle

    Args:
    n (int): The size of the board and number of queens

    Returns:
    List[List[List[int]]]: A list of all solutions, where each solution
                           is a list of queen positions [row, col]
    """
    # Initialize the board with zeros
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def solve(col):
        """
        Recursive helper function to solve the N Queens puzzle

        Args:
        col (int): The current column being processed

        Returns:
        None: Solutions are added to the 'solutions' list
        """
        # Base case: If all queens are placed, save the solution
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return
        
        # Try placing this queen in all rows of the current column
        for i in range(n):
            if is_safe(board, i, col, n):
                # Place the queen
                board[i][col] = 1
                # Recur to place rest of the queens
                solve(col + 1)
                # Backtrack
                board[i][col] = 0
    
    # Start solving from the first column
    solve(0)
    return solutions


def print_solutions(solutions):
    """
    Print all solutions in the required format

    Args:
    solutions (List[List[List[int]]]): List of all solutions

    Returns:
    None: Prints solutions to stdout
    """
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        # Try to convert the argument to an integer
        n = int(sys.argv[1])
    except ValueError:
        # If conversion fails, print error message and exit
        print("N must be a number")
        sys.exit(1)
    
    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve the puzzle and print the solutions
    solutions = solve_nqueens(n)
    print_solutions(solutions)
