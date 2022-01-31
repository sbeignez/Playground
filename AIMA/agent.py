from xmlrpc.client import boolean


class Agent():
    ''' Generic Agent
    '''
    pass

class ProblemSolvingAgent(Agent):
    ''' Agent that use Atomic representation
    '''
    pass

class PlanningAgent(Agent):
    ''' Agent that use factored or structured states
    '''
    pass


class State():
    def __init__(self, data, name=""):
        self.data = data
        self.name = name
    def __repr__(self):
        return f"S:{self.data}{self.name}"
    def __lt__(self, other):
        return self.data < other.data

class Action():
    def __init__(self, name=""):
        self.name = name
    def __repr__(self):
        return f"A:{self.name}"

class Problem():

    def __init__(self):
        pass

    def states(self) -> list[State]:
        return NotImplementedError

    def initial_state(self) -> State:
        return NotImplementedError

    def is_goal_states(self, state: State) -> boolean:
        return state in self.goal_states()

    def goal_states(self) -> list[State]:
        return NotImplementedError

    def actions(self, state: State) -> list[Action]:
        '''
        return:
            set of actions that are available/applicable in state s
        '''
        return NotImplementedError

    def result(state: State, action: Action) -> State:
        ''' Transition model
        Successor function: Succ() when deterministic
        Transition function: T(state, action) -> state'
            a sample action in possible states according probability.
        '''
        return NotImplementedError

    def action_cost(state_from: State,
            action: Action,
            state_to: State) -> int:

        ''' Action Cost Function
        '''

        return NotImplementedError



