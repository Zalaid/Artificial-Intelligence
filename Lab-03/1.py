import heapq  # to get minimum value from queue

class Node:  
    def __init__(self, state, parent, move, cost_g, cost_h):  
        self.state = state    #current state
        self.parent = parent   
        self.move = move  
        self.cost_g = cost_g  
        self.cost_h = cost_h  
        self.cost_f = cost_g + cost_h    #heusristic function