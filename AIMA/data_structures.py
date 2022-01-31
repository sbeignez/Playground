import typing
from agent import *


class Graph():
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        self.graph[node] = []
    def add_edge(self, node1, node2):
        self.graph[node1] = self.graph.get(node1, []) + [node2]
        self.graph[node2] = self.graph.get(node2, []) + [node1]

    def __repr__(self):
        s = f"{self.__class__.__name__} with {len(self.graph)} nodes"
        s += f"{[ str(k) + str(i) for k, i in self.graph.items()]}"
        return s


class Node():

    def __init__(self, state=None):
        self.state = state
    def __repr__(self):
        return f"({self.state})"


class TreeNode(Node):

    def __init__(self, state=None, parent=None,
            action=None, path_cost=0):
        self.state: State = state
        self.parent: Node = parent
        self.action: Action = action
        self.path_cost: int = path_cost

    def __repr__(self):
        return f"({self.state})"

    def __lt__(self, other):
        return self.state < other.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
    
    def __hash__(self):
        return hash(self.state)


class Tree(Graph):

    def __init__(self):
        self.root = None

    def add_node(self, node: 'TreeNode', parent: 'TreeNode' = None):
        if parent:
            node.parent = parent
        else:
            self.root = node

    def __repr__(self):
        s = "T"
        return s

    def path(node: TreeNode):

        if not node.parent:
            return [node]
        else:
            return Tree.path(node.parent) + [node]

    def actions_sequence(node: TreeNode):

        if not node.parent:
            return [""]
        else:
            return Tree.actions_sequence(node.parent) + [node.action]







if '__main__' == __name__:

    # TESTS

    g = Graph()
    n1 = Node("A")
    n2 = Node("B")
    n3 = Node("C")
    n4 = Node("D")

    print(g, n1, n2)

    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    g.add_node(n4)

    print(g)

    g.add_edge(n1, n2)
    g.add_edge(n2, n3)
    g.add_edge(n3, n4)
    g.add_edge(n2, n4)

    print(g)

    T = Tree()
    n1 = TreeNode(State("A", name="xx"), None, Action(), 0)
    n2 = TreeNode(State("B", name="xx"), None, Action(), 0)
    n3 = TreeNode(State("C", name="xx"), None, Action(), 0)
    n4 = TreeNode(State("D", name="xx"), None, Action(), 0)
    print(n1)
    T.add_node(n1)
    T.add_node(n2, n1)
    T.add_node(n3, n1)
    T.add_node(n4, n2)

    print(T)
    print(T.path(n4))
