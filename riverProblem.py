"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem.
"""
from searchProblem import Search_problem, Arc
from searchGeneric import AStarSearcher
class River_problem(Search_problem):
    
    state = {
    #  state   x-side| river| y-side
    #  '0000' == 'grain,hen,fox,farmer'   
        'a' : '0000',
        'b' : '1010',
        'c' : '2020',
        'd' : '1020',
        'e' : '0020',
        'f' : '1021',
        'g' : '2022',
        'h' : '1012',
        'i' : '0002',
        'j' : '1102',
        'k' : '2202',
        'l' : '1202',
        'm' : '0202',
        'n' : '1212',
        'o' : '2222'
    }
    
    graph = {
        'a':'b',
        'b':'c',
        'c':'d',
        'd':'e',
        'e':'f',
        'f':'g',
        'g':'h',
        'h':'i',
        'i':'j',
        'j':'k',
        'k':'l',
        'l':'m',
        'm':'n',
        'n':'o'
    }
    cost = {
        'a':0,
        'b':3,
        'c':4,
        'd':2,
        'e':4,
        'f':3,
        'g':4,
        'h':2,
        'i':1,
        'j':3,
        'k':4,
        'l':3,
        'm':2,
        'n':3,
        'o':6
    }
    
    
    def start_node(self):
        """returns start node"""
        #TODO
        return self.state['a']
    
    def is_goal(self,node):
        """is True if node is a goal"""
        if node == self.state['o']:
            return self.state['o']
        #TODO
        return False

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        """"""  
        if node == self.state['a']:
            return ['b']
            
        elif node == self.state['o']:
            return ['n']  
        else:
            neigh = []
            for key in self.graph:
                if self.state[key] == node:
                    neigh.append(key)
                    for k, v in self.graph.items():
                        if v == key:
                            neigh.append(key)
                            break
                    break
        
            return neigh
        
        
    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        if n == 'o':
            return 0
        Check = False
        heuristic_value = 0
        for i in self.cost:
            if i == n:
                Check = True
            if (Check == True and not(i == n)):
                heuristic_value += self.cost[i]
                        
        return heuristic_value 
    
    
            