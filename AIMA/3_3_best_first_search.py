import typing

import heapq

from agent import *
from data_structures import *
from problem_grid import *






def BestFirstSearch(problem: Problem, f) -> Node:

    node = TreeNode(problem.initial_state(), None, None, 0)
    frontier = [node]
    heapq.heapify(frontier)
    print("Frontier", frontier)
    reached = { problem.initial_state() : node }
    print("Reached", reached)

    while frontier:
        node = heapq.heappop(frontier)
        if problem.is_goal_states(node.state):
            return node
        else:
            for new_node in expand(problem, node):
                state = new_node.state
                if state not in reached or new_node.path_cost < reached[state].path_cost:
                    reached[state] = node
                    heapq.heappush(frontier, new_node)
    
    return "failure"


def expand(problem: Problem, node: Node) -> list[Node]:
    state = node.state
    cost = 0
    nodes = []
    for action in problem.actions(state):
        s_ = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, s_)
        new_node = TreeNode(state=s_, parent=node, action=action, path_cost=cost)
        nodes.append(new_node)
    return nodes



problem = GridProblem()
node= BestFirstSearch(problem, None)

print(Tree.path(node))
print(Tree.actions_sequence(node))





