import copy
import random
import math
import time
from tictactoe_ui import UI
# from tictactoe import State
# from tictactoe import State



class Agent:
    def __init__(self):
        self.name = None
        pass

    def next_move(self, state):
        pass

class RandomAgent(Agent):

    def __init__(self):
        super().__init__()

    def next_move(self, game, state) -> list[str]:
        if actions := game.actions(state):
            return random.choice(actions)
        else:
            return None

class CompositeAgent(Agent):

    def __init__(self, agents):
        super().__init__()
        self.agents = agents

    def next_move(self, game, state):
        self.epsilon = 0.1
        coin = random.uniform(0, 1)
        if coin < self.epsilon:
            pass
        print("Random move.")
        return random.choice(self.agents).next_move(state)

class MinimaxAgent(Agent):

    count = 0
    
    def __init__(self):
        super().__init__()
        self.name = "Minimax"

    def next_move(self, game, state):
        # state = copy.deepcopy(state.board), state.player
        value, move = MinimaxAgent.minimax_search(game, state)
        print("Minimax(" + str(value) + ") " + str(MinimaxAgent.count) + " ", end="")
        return move

    def minimax_search(game, state):
        MinimaxAgent.count = 0       
        value, move = MinimaxAgent.max_value(game, state)
        return value, move

    def max_value(game, state):
        if game.is_terminal(state):
            MinimaxAgent.count += 1
            return game.utility(state, game.BOARD_O), None
        v = -math.inf
        move = None
        for action in game.actions(state):
            v_child, a = MinimaxAgent.min_value(game, game.result(state, action))
            if v_child > v:
                v = v_child
                move = action
        return v, move

    def min_value(game, state): 
        if game.is_terminal(state):      
            MinimaxAgent.count += 1 
            return game.utility(state, game.BOARD_O), None
        v = math.inf
        move = None
        for action in game.actions(state):
            v_child, _ = MinimaxAgent.max_value(game, game.result(state, action))
            if v_child < v:
                v = v_child
                move = action
        return v, move

class ChanceMinimaxAgent(Agent):
    
    def __init__(self):
        self.epsilon = 0.05
        self.name = "ChanceMinimax"
        pass

    def next_move(self, game, state):
        # state = State(copy.deepcopy(state.board), state.player, state.utility)
        value, move, exp = ChanceMinimaxAgent.minimax_search(game, state)
        print(f"Max({value}) Exp({exp}) ", end="")
        # I pretend to think
        time.sleep(1)
        return move

    def minimax_search(game, state):        
        value, move, exp = ChanceMinimaxAgent.max_value(game, state)
        return value, move, exp

    def max_value(game, state):
        if game.is_terminal(state):
            return game.utility(state, game.BOARD_O), None, game.utility(state, game.BOARD_O)
        options = []
        for action in game.actions(state):
            v_child, a, exp = ChanceMinimaxAgent.min_value(game, game.result(state, action))
            options.append([v_child, action, exp])
        v, move, exp = ChanceMinimaxAgent.pick_best_action(options, max=True)
        return v, move, exp

    def min_value(game, state):
        if game.is_terminal(state):      
            return game.utility(state, game.BOARD_O), None, game.utility(state, game.BOARD_O)
        options = []
        for action in game.actions(state):
            v_child, a, exp = ChanceMinimaxAgent.max_value(game, game.result(state, action))
            options.append([v_child, action, exp])
        v, move, exp = ChanceMinimaxAgent.pick_best_action(options, max=False)
        return v, move, exp

    def pick_best_action(options, max): # -> v, action, exp
        # print(options)
        options.sort(key=lambda x: (x[0] , x[2]), reverse= not max)
        #print(max, options)
        v, action, _ = options[-1]
        exp = sum([x[2] for x in options]) / len(options)
        #print(v, action, exp)
        #input()
        return v, action, exp

class HumanAgent(Agent):

    def __init__(self):
        self.name = "Human"
        pass

    def next_move(self, game, state):
        move = None

        if game.display_mode == "Text":
            return self.input_move_text(game, state)
        elif game.display_mode == "GUI":
            return self.input_move_gui(game, state)
 
    def input_move_text(self, game, state):

        def print_alert(s):
            print("   <<< "+ s.center(25) + " >>>")

        move = None
        while move is None:
            m = input(f"Your move {state.player}? ")
            action = game.cell_to_rowcol(m)
            if action:
                if game.is_valid_action(action):
                    move = m
                else:
                    print_alert("INVALID CELL")
                    print_alert(m + " is occupied")
                    print_alert("Try again")
            else:
                print_alert("INVALID INPUT")
                print_alert("Valid: A1, b2, C3...")
                print_alert("Try again")
        return action

    def input_move_gui(self, game, state):
        action = None
        while action is None:
            cell = game.ui.get_cell()
            if game.is_valid_action(cell):
                action = cell
                print(game.rowcol_to_cell(action))
        return action


class BFS_Grapg(Agent):
    pass



