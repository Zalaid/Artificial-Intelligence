import heapq  

class Node:  
    def __init__(self, state, parent, move, cost_g, cost_h):  
        self.state = state  
        self.parent = parent  
        self.move = move  
        self.cost_g = cost_g  
        self.cost_h = cost_h  
        self.cost_f = cost_g + cost_h  