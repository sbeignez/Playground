from data_structures import *
from agent import *

class Move(Action):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        s = ""
        if self.x == 1: s = "RIGHT"
        if self.x == -1: s = "LEFT_"
        if self.y == 1: s = "UP___"
        if self.y == -1: s = "DOWN_"
        return f"A:{s}"

class Cell(State):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x < other.x or self.y < other.y
    def __repr__(self):
        return f"C[{self.x},{self.y}]"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

class GridProblem(Problem):

    def __init__(self):
        self.rows = 8
        self.cols = 8
        self._initial_state = Cell(2,2)
        self._goal_states = [Cell(8,8)]

    def states(self) -> list[State]:
        return [ Cell(x,y) for y in range(1, self.rows +1) for x in range(1, self.cols+1)]

    def initial_state(self) -> State:
        return self._initial_state

    def is_goal_states(self, state: State) -> boolean:
        return state in self.goal_states()

    def goal_states(self) -> list[State]:
        return self._goal_states

    def actions(self, state: State) -> list[Action]:
        actions = []
        if state.x != 1: actions.append(Move(-1,0))
        if state.x != self.cols: actions.append(Move(1,0))
        if state.y != 1: actions.append(Move(0,-1))
        if state.y != self.rows: actions.append(Move(0,1))
        return actions

    def result(self, state: State, action: Action) -> State:
        new_state = Cell( state.x + action.x, state.y + action.y )
        return new_state

    def action_cost(self, state_from: State,
            action: Action,
            state_to: State) -> int:
        return abs(state_from.x - state_to.x) + abs(state_from.y - state_to.y)


if __name__ == '__main__': 
    print("="*40)

    P = GridProblem()
    print("initial", P.initial_state())
    print("goal", P.goal_states())
    print("is_goal", P.is_goal_states(Cell(1,2)))
    print("is_goal", P.is_goal_states(Cell(4,4)))
    print("states", P.states()[:5])
    print("actions", P.actions(Cell(1,2)))
    print("results", P.result( Cell(1,2), Move(0,1)))
    print("cost", P.action_cost(Cell(1,2), Move(0,1), Cell(2,2)))

    print(Move(1,0))
