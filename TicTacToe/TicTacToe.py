import copy
import random
import math

class Env:
    pass

class TicTacToe(Env):

    BOARD_EMPTY = " "
    BOARD_X = "X"
    BOARD_O = "O"
    
    def __init__(self):
        self.board = [[TicTacToe.BOARD_EMPTY for _ in range(3)] for _ in range(3)]
        self.players = [
                (TicTacToe.BOARD_X, HumanAgent()),
                (TicTacToe.BOARD_O, BasicAgent()),
            ]
        self.player = self.players[0]

    def reset(self):
        pass

    def step(self, row, col):
        obs, reward, done, info = None, 0, False, {}
        
        #update model
        self.board[row][col] = self.player[0]

        if self.check_win(self.player[0]):
            reward = 1 # or -1
            done = True

        return self.board, reward, done, info



    def display(self):
        print("")
        print("  +" + "-"*11 + "+")
        for i, row in enumerate(self.board):
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



    def is_valid_action(self, row, col):
        return self.board[row][col] == TicTacToe.BOARD_EMPTY

    def cell_to_rowcol(cell):
        cell = cell.upper()
        if len(cell) == 2 and cell[0] in ["A", "B", "C"] and cell[1] in ["1", "2", "3"]:
            row = ["3", "2", "1"].index(cell[1])
            col = ["A", "B", "C"].index(cell[0])
            return True, row, col
        else:
            return False, None, None

    def rowcol_to_cell(row, col):
        return chr(ord("A") + col) + str(3-row)
        

    def next_player(self):
        # i = self.players.index(self.player)     
        self.player = [p for p in self.players if p is not self.player][0]

    def start(self):
        print("")
        print("== TIC TAC TOE ==")
        self.display()

        done = False

        while not done:

            if self.player[0] == TicTacToe.BOARD_X: 
                m = self.player[1].next_move(self)
            else:
                m = self.player[1].next_move(self)
                print(f"[{self.player[0]}] plays: {m}")

            is_valid_cell, m_row, m_col = TicTacToe.cell_to_rowcol(m)
            
            _, reward, done, _ = self.step(m_row, m_col)

            self.display()

            if done:
                print("")
                print("+---------------+")                
                print(f"| Player {self.player[0]} wins |")
                print("+---------------+")
                print("")

            self.next_player()

    ## GLOBAL PART

    def result(state, action):
        board, player = state
        _, row, col = TicTacToe.cell_to_rowcol(action)
        new_board = copy.deepcopy(board)
        new_board[row][col] = player
        new_state = (new_board, TicTacToe.other_player(player))
        return new_state

    def other_player(player):
        return TicTacToe.BOARD_O if player == TicTacToe.BOARD_X else TicTacToe.BOARD_X

    def actions(state):
        board, player = state
        cells = [ (r,c) for r in range(3) for c in range(3)] 
        actions = [ TicTacToe.rowcol_to_cell(row, col) for row, col in cells if board[row][col] == " "]
        return actions

    def utility(state, a_player):
        board, player = state
        another_state = (board, a_player)
        if TicTacToe.is_terminal(another_state):
            if TicTacToe.is_win(another_state):
                return 1
            if TicTacToe.is_lose(another_state):
                return -1
            if TicTacToe.is_draw(another_state):
                return 0
        else:
            print("ERROR: utility called on non-terminal state")
            return None

    def is_terminal(state):
        return TicTacToe.is_win(state) or TicTacToe.is_lose(state) or TicTacToe.is_draw(state)

    def is_win(state):
        b, player = state
        win = max(
            [sum( 1 if b[r][c] == player else 0 for c in range(3)) for r in range(3)] +
            [sum( 1 if b[r][c] == player else 0 for r in range(3)) for c in range(3)] +
            [sum( [1 if b[i][i] == player else 0 for i in range(3)] )] +
            [sum( [1 if b[i][2-i] == player else 0 for i in range(3)] )] 
        )
        return win == 3

    def is_lose(state):
        board, player = state
        return TicTacToe.is_win( (board, TicTacToe.other_player(player)) )

    def is_draw(state):
        board, player = state
        return not any( [ TicTacToe.BOARD_EMPTY in row for row in board] )

    def printme(state):
        board, player = state
        print("  +" + "-"*11 + "+")
        for i, row in enumerate(board):
            print(str(3-i) + " | " + " | ".join(row) + " |")
            print("  +" + "-"*11 + "+")
        print("    A   B   C  ")



def print_alert(s):
    print("   <<< "+ s.center(25) + " >>>")


class Agent:
    def __init__(self):
        pass

    def next_move(self, board):
        pass

class BasicAgent(Agent):
    
    def __init__(self):
        self.epsilon = 0.0
        pass

    def next_move(self, game):
        
        coin = random.uniform(0, 1)
        if coin < self.epsilon:
            moves = TicTacToe.actions((game.board, game.player[0]))
            move = random.choice(moves)
            print("random")
        else:
            state = copy.deepcopy(game.board), game.player[0]
            value, move = BasicAgent.minimax_search(game, state)
            print("minimax: " + str(value) + " " + move)
        return move

    def minimax_search(game, state):        
        value, move = BasicAgent.max_value(game, state)
        return value, move

    def max_value(game, state):
        if TicTacToe.is_terminal(state):
            # print("terminal max " + str(TicTacToe.utility(state, TicTacToe.BOARD_O)))
            return TicTacToe.utility(state, TicTacToe.BOARD_O), None
        v = -math.inf
        move = None
        # print(TicTacToe.actions(state))
        for action in TicTacToe.actions(state):
            v_child, a = BasicAgent.min_value(game, TicTacToe.result(state, action))
            if v_child > v:
                v = v_child
                move = action
        return v, move

    def min_value(game, state):
        if TicTacToe.is_terminal(state):      
            # print("terminal min " + str(TicTacToe.utility(state, TicTacToe.BOARD_O)))
            # TicTacToe.printme(state)
            return TicTacToe.utility(state, TicTacToe.BOARD_O), None
        v = math.inf
        move = None
        for action in TicTacToe.actions(state):
            v_child, _ = BasicAgent.max_value(game, TicTacToe.result(state, action))
            if v_child < v:
                v = v_child
                move = action
        return v, move
        

class HumanAgent(Agent):

    def __init__(self):
        pass

    def next_move(self, game):
        move = None
        while move is None:
            m = input("Your move: ")
            is_valid_cell, m_row, m_col = TicTacToe.cell_to_rowcol(m)
            if is_valid_cell:
                if game.is_valid_action(m_row, m_col):
                    move = m
                else:
                    print_alert("INVALID CELL")
                    print_alert(m + " is occupied")
                    print_alert("Try again")
            else:
                print_alert("INVALID INPUT")
                print_alert("Valid: A1, b2, C3...")
                print_alert("Try again")
        return move
 


env = TicTacToe()
env.start()



