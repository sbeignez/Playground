import copy
import random
import math
import time
from tictactoe_ui import UI
from tictactoe_agents import *
from collections import namedtuple

class Env:
    pass

State = namedtuple('State', 'board, player, utility')

class TicTacToe(Env):

    BOARD_EMPTY = " "
    BOARD_X = "X"
    BOARD_O = "O"

    PLAYERS = [BOARD_X,  BOARD_O]
    AGENTS = {
        BOARD_X : [HumanAgent()][0],
        BOARD_O : [RandomAgent(), MinimaxAgent()][1],
    }
    
    def __init__(self, m=3, n=3, k=3):

        self.cols = m
        self.rows = n
        self.k = k

        self.board = [[TicTacToe.BOARD_EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self.initial_state = State(board= self.board, player= TicTacToe.PLAYERS[random.randint(0,1)], utility= 0)

        self.display_mode = ["Text", "GUI"][0]

        if self.display_mode == "GUI":
            self.ui = UI(theme=["default","pacman", "mario"][2])

    def reset(self):
        pass

    def step(self, row, col):
        obs, reward, done, info = None, 0, False, {}
        
        #update model
        self.board[row][col] = self.player[0]

        if self.check_win(self.player[0]):
            reward = 1 # or -1
            done = True
        elif TicTacToe.is_draw(State(self.board, self.player[0], 0)):
            reward = 0
            done = True

        return self.board, reward, done, info



    def display(self, state):
        if self.display_mode == "GUI":
            self.ui.draw_ui(self, state)
        else:
            self.display_text(state)

    def display_text(self, state):
        print("")
        print("  +" + "-"*11 + "+")
        for i, row in enumerate(state.board):
            print(str(3-i) + " | " + " | ".join(row) + " |")
            print("  +" + "-"*11 + "+")
        print("    A   B   C  ")
        print("")

    def check_win(self, player_mark):
        b = self.board
        win = max(
            [sum( 1 if b[r][c] == player_mark else 0 for c in range(3)) for r in range(3)] +
            [sum( 1 if b[r][c] == player_mark else 0 for r in range(3)) for c in range(3)] +
            [sum( [1 if b[i][i] == player_mark else 0 for i in range(3)] )] +
            [sum( [1 if b[i][2-i] == player_mark else 0 for i in range(3)] )] 
        )
        return win == 3



    def is_valid_action(self, action) -> bool:
        row, col = action
        if row is not None and col is not None and row >= 0 and row <= 2 and col >= 0 and col <= 2:
            return self.board[row][col] == TicTacToe.BOARD_EMPTY
        else:
            return False
            

    def cell_to_rowcol(self, cell):
        if not cell:
            return None
        print(cell)
        cell = cell.upper()
        if len(cell) == 2 and cell[0] in ["A", "B", "C"] and cell[1] in ["1", "2", "3"]:
            row = ["3", "2", "1"].index(cell[1])
            col = ["A", "B", "C"].index(cell[0])
            return (row, col)
        else:
            return None

    def rowcol_to_cell(self, action):
        if action != (None, None):
            row, col = action
            return chr(ord("A") + col) + str(3-row)
        

    def start(self):

        state = self.initial_state

        print("")
        print("== TIC TAC TOE ==")
        self.display(state)

        done = False
        while not state.utility:

            print(f"Player [{state.player}] Turn")
            action = self.AGENTS[state.player].next_move(self, state)

            print(f"  Player [{state.player}] played: {self.rowcol_to_cell(action)}")

            state = self.result(state, action)
            self.display(state)


        if self.is_draw(state):
            print("")
            print( "+---------------+")                
            print(f"|  Draw game!   |")
            print( "+---------------+")
            print("")
        else:
            print("")
            print("+---------------+")                
            print(f"| Player {state.player} loose |")
            print("+---------------+")
            print("")


            

        time.sleep(2)

    def result(self, state, action) -> State:
        new_board = copy.deepcopy(state.board)
        new_board[action[0]][action[1]] = state.player
        new_state = State(board = new_board, player = self.other_player(state.player), utility = self.utility(new_board, state.player) )
        return new_state

    # player switch 
    def other_player(self, player):
        return self.BOARD_O if player == self.BOARD_X else self.BOARD_X

    def next_player(self):
        # i = self.players.index(self.player)     
        self.player = [p for p in self.players if p is not self.player][0]


    # ACTIONS 
    # action: (x, y) 
    def actions(self, state) -> list[State]:
        cells = [ (r,c) for r in range(3) for c in range(3)] 
        actions = [ (row, col) for row, col in cells if state.board[row][col] == " "]
        random.shuffle(actions)
        return actions

    def utility(self, board, player) -> int:
        another_state = State(board, player, None)
        if self.is_terminal(another_state):
            if self.is_win(another_state):
                return 1
            if self.is_lose(another_state):
                return -1
            if self.is_draw(another_state):
                return 0
        else:
            print("ERROR: utility called on non-terminal state")
            return None

    def is_terminal(self, state) -> bool:
        return self.is_win(state) or self.is_lose(state) or self.is_draw(state)
        # self.actions(state) == []

    def is_win(self, state) -> bool:
        win = max(
            [sum( 1 if state.board[r][c] == state.player else 0 for c in range(3)) for r in range(3)] +
            [sum( 1 if state.board[r][c] == state.player else 0 for r in range(3)) for c in range(3)] +
            [sum( [1 if state.board[i][i] == state.player else 0 for i in range(3)] )] +
            [sum( [1 if state.board[i][2-i] == state.player else 0 for i in range(3)] )] 
        )
        return win == 3

    def is_lose(self, state) -> bool:
        return self.is_win( State(state.board, self.other_player(state.player), state.utility) )

    def is_draw(self, state) -> bool:
        return not any( [ self.BOARD_EMPTY in row for row in state.board] )

    def printme(state):
        print("  +" + "-"*11 + "+")
        for i, row in enumerate(state.board):
            print(str(3-i) + " | " + " | ".join(row) + " |")
            print("  +" + "-"*11 + "+")
        print("    A   B   C  ")





if __name__ == "__main__":
    game = TicTacToe()
    game.start()




