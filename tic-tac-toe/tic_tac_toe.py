import re
import random as r

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    symbol_to_check = ""
    over=False
    board_check = self.board
    if(self.turn == _PLAYER):
      symbol_to_check = _PLAYER_SYMBOL

    else:
      symbol_to_check = _MACHINE_SYMBOL
    
    if board_check[0] == symbol_to_check and board_check[4] == symbol_to_check and board_check[8] == symbol_to_check:
      over=True
    elif board_check[0] == symbol_to_check and board_check[1] == symbol_to_check and board_check[2] == symbol_to_check:
      over=True
    elif board_check[0] == symbol_to_check and board_check[3] == symbol_to_check and board_check[6] == symbol_to_check:
      over=True
    elif board_check[1] == symbol_to_check and board_check[4] == symbol_to_check and board_check[7] == symbol_to_check:
      over=True
    elif board_check[2] == symbol_to_check and board_check[4] == symbol_to_check and board_check[6] == symbol_to_check:
      over=True
    elif board_check[2] == symbol_to_check and board_check[5] == symbol_to_check and board_check[8] == symbol_to_check:
      over=True
    elif board_check[3] == symbol_to_check and board_check[4] == symbol_to_check and board_check[5] == symbol_to_check:
      over=True
    elif board_check[6] == symbol_to_check and board_check[7] == symbol_to_check and board_check[8] == symbol_to_check:
      over=True
    return over

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    play = r.randint(0,len(self.board)-1)
    while self.board[play] != None:
      play = r.randint(0,len(self.board))
    
    self.board[play] = _MACHINE_SYMBOL



  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    print(self.turn + " Wins")
