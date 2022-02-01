from locale import ABDAY_1
import pygame
import random

class Env:
    pass

class TicTacToe(Env):
    
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.player = self.players[0]
        self.agent = Agent()

    def reset(self):
        pass

    def step(self, row, col):
        obs, reward, done, info = None, 0, False, {}
        
        #update model
        self.board[row][col] = self.player

        if self.is_win():
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


    def is_win(self):
        b = self.board
        # print("is_win rows", [sum( 1 if b[r][c] == self.player else 0 for c in range(3)) for r in range(3)])
        # print("is_win cols", [sum( 1 if b[r][c] == self.player else 0 for r in range(3)) for c in range(3)])
        win = max(
            [sum( 1 if b[r][c] == self.player else 0 for c in range(3)) for r in range(3)] +
            [sum( 1 if b[r][c] == self.player else 0 for r in range(3)) for c in range(3)] +
            [sum( [1 if b[i][i] == self.player else 0 for i in range(3)] )] +
            [sum( [1 if b[i][2-i] == self.player else 0 for i in range(3)] )] 
        )
        return win == 3

    def is_valid_action(self, row, col):
        return self.board[row][col] == " "

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
        i = self.players.index(self.player)     
        self.player = self.players[(i+1) % len(self.players)]

    def start(self):
        print("")
        print("== TIC TAC TOE ==")
        self.display()

        done = False

        while not done:

            move = False
            while not move:

                if self.player == "X":    
                    m = input(f"[{self.player}] plays: ")
                else:
                    m = self.agent.next_move(self.board)
                    print(f"[{self.player}] plays: {m}")

                is_valid_cell, m_row, m_col = TicTacToe.cell_to_rowcol(m)
                if is_valid_cell:
                    if self.is_valid_action(m_row, m_col):
                        move = True
                    else:
                        print_alert("INVALID CELL")
                        print_alert(m + " is occupied")
                        print_alert("Try again")
                else:
                    print_alert("INVALID INPUT")
                    print_alert("Valid: A1, b2, C3...")
                    print_alert("Try again")
            
            _, reward, done, _ = self.step(m_row, m_col)


            self.display()

            if done:
                print("")
                print("+---------------+")                
                print(f"| Player {self.player} wins |")
                print("+---------------+")
                print("")

            self.next_player()

def print_alert(s):
    print("   <<< "+ s.center(25) + " >>>")


class Agent:
    
    def __init__(self):
        pass

    def next_move(self, board):

        cells = [ (r,c) for r in range(3) for c in range(3)] 
        moves = [ TicTacToe.rowcol_to_cell(row, col) for row, col in cells if board[row][col] == " "]
        
        # print(len(moves), moves)

        move = random.choice(moves)
        return move


 


env = TicTacToe()
env.start()
