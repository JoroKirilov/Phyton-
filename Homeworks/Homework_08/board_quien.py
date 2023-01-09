def solve_eight_queens(board, col):
  if col == 8:
    # All queens have been placed on the board, so we have a solution
    return True

  for row in range(8):
    # Check if it is safe to place a queen at this position
    if is_safe(board, row, col):
      # Place the queen and recursively search for a solution
      board[row][col] = 1
      if solve_eight_queens(board, col+1):
        return True
      # Backtrack and try a different position for this queen
      board[row][col] = 0

  # No solution was found
  return False

def is_safe(board, row, col):
  # Check if there is a queen on the same row
  for c in range(col):
    if board[row][c] == 1:
      return False

  # Check if there is a queen on the same diagonal
  for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[r][c] == 1:
      return False
  for r, c in zip(range(row, 8, 1), range(col, -1, -1)):
    if board[r][c] == 1:
      return False

  return True

# Initialize the board to an empty state
board = [[0 for _ in range(8)] for _ in range(8)]

# Solve the eight queens problem
if solve_eight_queens(board, 0):
  for row in board:
    print(row)
else:
  print("No solution found")