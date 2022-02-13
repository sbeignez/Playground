
from hmac import trans_36
from tictactoe import TicTacToe
import random

class Board:

    def __init__(self,  m=3, n=3, k=3, list = []):
        self.cols = m
        self.rows = n

        if list:
            self.board = list
        else:
            self.board = [TicTacToe.BOARD_EMPTY for _ in range(self.cols  * self.rows)]

    def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.board == other.board
            else:
                return False

    def __hash__(self) -> int:
        return (str(self.board)).__hash__()

    def reset_random(self):
        self.board = [random.choice([TicTacToe.BOARD_EMPTY, TicTacToe.BOARD_X, TicTacToe.BOARD_O ]) for _ in range(self.cols  * self.rows)]

    def set_board(self, m=3, n=3, list = [] ):
        self.board = list
        self.cols = m
        self.row = n

    row1 = [0, 1, 2]
    row2 = [3, 4, 5]
    row3 = [6, 7, 8]
    col1 = [0, 3, 6]
    col2 = [1, 4, 7]
    col3 = [2, 5, 8]
    dia1 = [0, 4, 8]
    dia2 = [2, 4, 6]

    lines = [row1, row2, row3, col1, col2, col3, dia1, dia2]

    def check_win(self, player):
        for line in self.lines:
            if self.check_line(line, player):
                return True
        return False

    def check_line(self, line, player):
        for i in line:
            if self.board[i] != player:
                return False
        return True


    rot90 = { 0: 6, 1: 3, 2: 0, 3: 7, 4: 4, 5: 1, 6: 8, 7: 5, 8: 2 }
    symY =  { 0: 2, 1: 1, 2: 0, 3: 5, 4: 4, 5: 3, 6: 8, 7: 7, 8: 6 }
    transformations = { "rot90" : rot90, "symY" : symY}
    group = [ [], [rot90], [rot90, rot90], [rot90, rot90, rot90], [symY], [symY, rot90], [symY, rot90, rot90], [symY, rot90, rot90, rot90] ]

    # a, rotation 90  
    # b, symmetry on y axis  
    # $S_{sym} = { 1, a, a^2, a^3, b, b, ba, ba^2, ba^3}$

    def is_symmetric(board1, board2):
        return any( Board.transform(board1, t).board == board2.board for t in Board.group )

    def display_text(self):
        print("")
        print("  +" + "---+" * self.cols)
        i = 0
        for row in range(self.rows):
            print(str(row+1).rjust(2) + "|", end="")
            for col in range(self.cols):
                print(" " + self.board[i]+" |", end="")
                i += 1
            print("\n  +" + "---+" * self.cols)
        print("    A   B   C  ")
        print("")

    def transform_step(board, transformation):
        if not (board.rows == board.cols):
            return None
        b = [ board.board[transformation[i]] for i in range(len(board.board))]
        return Board(board.cols, board.rows, 3, b)

    def transform(board, transformations):
        # print("trans", end=", " )
        for t in transformations:
            board = Board.transform_step(board, t)
            # print(board.board)
        return board

    def group_boards(board):
        return set( Board.transform(board, trans_list) for trans_list in Board.group )




b = Board(3,3,3)
b.reset_random()
b.display_text()
c = Board.transform(b, [Board.rot90])
b.display_text()
c.display_text()

B = [ Board.transform(b, trans_list) for trans_list in Board.group ]
print("--"*10)
for b in B:
    b.display_text()

print("--"*10)
B[0].display_text()

x = Board.is_symmetric(b, B[2])
print(x)

print("--"*10)
x1 = Board(3,3,3,['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
x2 = Board(3,3,3,[' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
x3 = Board(3,3,3,[' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', ' '])
X = Board.group_boards(x1)
print("--"*10)
for b in X:
    b.display_text()