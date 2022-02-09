from collections import deque

class CSP():

    def __init__(self, variables, domain, constraints):
        self.variables = variables
        self.variables



class MapColoring(CSP):

    def __init__(self):
        self.variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
        self.domains = {
            "WA" : ["red", "green", ],
            "NT" : ["red", "green", "blue"],
            "Q"  : ["red", "green", "blue"],
            "NSW": ["red", "green", "blue"],
            "V"  : ["red", "green", "blue"],
            "SA" : [ "green", ],
            # "T"  : ["red", "green", "blue"],
        }
        self.constraints = {
            ("WA", "NT") : lambda x, y : x != y,
            ("NT", "WA") : lambda x, y : x != y,
            ("WA", "SA") : lambda x, y : x != y,
            ("SA", "WA") : lambda x, y : x != y,
            ("NT", "SA") : lambda x, y : x != y,
            ("SA", "NT") : lambda x, y : x != y,
            ("NT", "Q" ) : lambda x, y : x != y,
            ("Q" , "NT") : lambda x, y : x != y,
            ("SA", "Q" ) : lambda x, y : x != y,
            ("Q" , "SA") : lambda x, y : x != y,
            ("V", "SA" ) : lambda x, y : x != y,
            ("SA" , "V") : lambda x, y : x != y,
            ("Q", "NSW" ) : lambda x, y : x != y,
            ("NSW" , "Q") : lambda x, y : x != y,
            ("SA", "NSW" ) : lambda x, y : x != y,
            ("NSW" , "SA") : lambda x, y : x != y,
            ("V", "NSW" ) : lambda x, y : x != y,
            ("NSW" , "V") : lambda x, y : x != y,
        }

    def __repr__(self) -> str:
        s = ""
        for variable, domain in self.domains.items():
            s += f"{variable.ljust(4)} : {domain} \n"
        return s


class CSP_Solver():
    pass

class AC_3(CSP_Solver):
    
    def solve(self, csp):

        print(csp)

        queue = deque(csp.constraints.keys())
        # print("Q", queue)


        while queue:
            x_i, x_j = queue.popleft()
            # print("ARC: ", x_i, x_j)
            if self.revise(csp, x_i, x_j):

                if len(csp.domains[x_i]) == 0 :
                    return False

                # print("neighbors of:", x_i, "-", x_j, [ arc[1] for arc in csp.constraints if arc[0] == x_i and arc[1] != x_j ])
                for x_k in [ arc[1] for arc in csp.constraints if arc[0] == x_i and arc[1] != x_j ]:
                    queue.append((x_k, x_i))
                # print("Q", queue)
        return True
    
    def revise(self, csp, x_i, x_j):
        revised = False
        for value in csp.domains[x_i]:
            satisfied = not any([ csp.constraints[x_i, x_j](value, value_j) for value_j in csp.domains[x_j]])
            if satisfied:
                csp.domains[x_i].remove(value)
                revised = True
        return revised


csp = MapColoring()
solver = AC_3()

answer = solver.solve(csp)

print("="*10)
print(answer)
print(csp)


