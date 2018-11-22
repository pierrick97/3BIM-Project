from __future__ import print_function

try:
  input = raw_input
except NameError:
  pass



def draw_board_C_style(game_state):
  """
  C-style implementation of draw_board,
  using nested loops
  """ 
  size = len(game_state)
  for row in range(size):
    for col in range(size):
      print(" ---", end='')
    print(" \n", end='')
    for col in range(size):
      print("| ", end='')
      if game_state[row][col] == 0:
        print(" ", end='')
      else:
        print(game_state[row][col], end='')
      print(" ", end='')
    print("|\n", end='')
  for col in range(size):
      print(" ---", end='')
  print("\n", end='')


def draw_board_Python_style(game_state): 
  """
  A more Pythonic implementation of draw_board,
  using list repetitions and list comprehesions
  to get a more compact code than the C-style code
  """ 
  size = len(game_state)
  for row in range(size):
    print(" ---" * size) # in Python, the * operator works on strings and allows for string repetition
    rowstrlist = [" " if val==0 else str(val) for val in game_state[row]] # this is a list comprehension (typical Python !)
    rowstr = "| " + " | ".join(rowstrlist)  + " |"
    print(rowstr)
  print(" ---" * size)


def draw_board(game_state):
  """
  Parameters passed in data mode: game_state
  Parameters passed in data/result mode: [none]
  Parameters passed in result mode: [none]
  Preconditions: game_state is a list of list of integers 
                 comprised between 0 and 2. All nested
                 lists must have the same length, which 
                 must also be the length of the main list.
  Postconditions: A grid representing the game state
                  is drawn on the screen. 
  Example: If game_state == [[2, 0, 1, 0], [0, 0, 2, 0], [1, 1, 1, 0], [2, 0, 0, 0]],
           then the following grid will be drawn:
           --- --- --- ---
          | 2 |   | 1 |   |
           --- --- --- ---
          |   |   | 2 |   |
           --- --- --- ---
          | 1 | 1 | 1 |   |
           --- --- --- ---
          | 2 |   |   |   |
            --- --- --- ---
  Result: [none]
  """
  draw_board_Python_style(game_state)


def grid_full(game_state):
  """
  Parameters passed in data mode: game_state
  Parameters passed in data/result mode: [none]
  Parameters passed in result mode: [none]
  Preconditions: game_state is a list of list of integers 
                 comprised between 0 and 2. All nested
                 lists must have the same length, which 
                 must also be the length of the main list.
  Postconditions: [none] 
  Result: True if none of the nested lists in game_state contains 0, 
          False otherwise (i.e. if there is at least one 0 in one
          of the nested lists).
  """
  size = len(game_state)
  for row in range(size):
    if 0 in game_state[row]:
      return False
  return True



def check_winner(game_state):
  """
  Parameters passed in data mode: game_state
  Parameters passed in data/result mode: [none]
  Parameters passed in result mode: [none]
  Preconditions: game_state is a list of list of integers 
                 comprised between 0 and 2. All nested
                 lists must have the same length N, which 
                 must also be the length of the main list.
  Postconditions: [none] 
  Result: 1 if Player 1 has won, 2 if Player 2 has won, 0 if 
          no one has won yet. Player X has won if he or she 
          occupies a whole row (one of the nested list is 
          entirely made up of X), or a whole column (the i-th
          element of each nested list is X, for some i in 0..N-1),
          or a whole diagonal.
  """
  size = len(game_state)
  winner = 0

  # Check each row
  for row in range(size):
    myset = set(game_state[row])
    if (len(myset) == 1 and game_state[row][0] != 0):
      winner = game_state[row][0] 
      return winner

  # Check each column
  for col in range(size):
    myset = set()
    for row in range(size):
      myset.add(game_state[row][col])
    if (len(myset) == 1 and game_state[0][col] != 0):
      winner = game_state[0][col] 
      return winner

  # Check NW-SE diagonal
  row = 0
  col = 0
  myset = set()
  while row < size:
    myset.add(game_state[row][col])
    row = row + 1
    col = col + 1
  if (len(myset) == 1 and game_state[0][0] != 0):
      winner = game_state[0][0] 
      return winner

  # Check SW-NE diagonal
  row = size-1
  col = 0
  myset = set()
  while col < size:
    myset.add(game_state[row][col])
    row = row - 1
    col = col + 1
  if (len(myset) == 1 and game_state[size-1][0] != 0):
      winner = game_state[size-1][0] 
      return winner

  return winner


    if __name__ == "__main__":
  size = int(input("Board size ? "))
  game_state = [ [0 for j in range(size)] for i in range(size) ] 
  draw_board(game_state)

  current_player = 1
  while not grid_full(game_state):
    illegal_move = True
    while illegal_move:
      user_input = input("Player " + str(current_player) + ", please type the coordinates of your move (0-" + str(size-1) + " 0-" + str(size-1) +"):")
      words = user_input.split()
      x = int(words[0])
      y = int(words[1])
      if (game_state[x][y] == 0):
        illegal_move = False
        game_state[x][y] = current_player
      else:
        print("Illegal move, sorry!")
    draw_board(game_state)
    winner = check_winner(game_state)
    if (winner != 0):
      print("Player", winner, "has won!") 
      break   
    if (current_player == 1) :
      current_player = 2
    else:
      current_player = 1
  if (grid_full(game_state)):
    print("End of game, no winner.")


