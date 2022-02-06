
---
# 3. SEARCH

AGENT (Problem Solving ~)
- update_state(state, percept)
- formulate_goal(state)
- formulate_problem(state, goal)
- search(problem)


PROBLEM
- actions(state) -> [action]
- result(state, action) -> state
- goal_test(state) -> bool
- path_cost(c, state_from, action, state_to) -> ? 
- value(state) -> int

PROBLEM
> GRAPH PROBLEM
> > 

InstrumentedProblem(Problem)
  Wrapper around class Problem, to keep statistics


DATA STRUCTURES
- Node
    - data
        - state
        - parent
        - action
        - path_cost
        - depth
    - functions
        - expand()
        - child_node()
        - solution()
        - path()

- GRAPH
(for problems)

---
# 5. GAME

AGENTS
1.1 Search algos
1.2 Players

GAMES
2.1 Game
"""A game is similar to a problem, but it has a utility for each state and a terminal test instead of a path cost and a goal test. """
- actions(state) -> [action], list of legal actions
- result(state, move) -> state
- utility(state, player) -> int
- terminal_test(state) -> bool
- to_move(state) -> player

- display(state)
- play_game(players)

DATA STRUCTURE
- GameState = namedtuple('GameState', 'to_move, utility, board, moves')
    - to_move: player
    - utility: int
    - board: dict{ (x,y) : "O or X" }
    - moves: list of moves
- action

2.2 TicTacToe(Game)
- ...
- compute_utility(board, move, player)
- k_in_row(board, move, player, delta_x_y) # helper func for is_win(state)

---
# x. RL


ENVIRONMENT ~PROBLEM/GAME

AGENT
