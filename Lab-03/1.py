import heapq  # to get minimum value from queue

class Node:  
    def __init__(self, state, parent, move, cost_g, cost_h):  
        self.state = state    #current state
        self.parent = parent   
        self.move = move  
        self.cost_g = cost_g  
        self.cost_h = cost_h  
        self.cost_f = cost_g + cost_h    #heusristic function


    def __lt__(self, other):  
        return self.cost_f < other.cost_f  

def manhattan_distance(current_state, target_state):  
    total_distance = 0  
    for number in range(1, 9):  
        current_pos = current_state.index(number)  
        target_pos = target_state.index(number)  
        current_row, current_col = divmod(current_pos, 3)  
        target_row, target_col = divmod(target_pos, 3)  
        total_distance += abs(current_row - target_row) + abs(current_col - target_col)  
    return total_distance  

def generate_successors(node, target_state):  
    successors = []  
    empty_pos = node.state.index(0)  
    row, col = divmod(empty_pos, 3)  

    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for move in possible_moves:  
        new_row, new_col = row + move[0], col + move[1]  
        if 0 <= new_row < 3 and 0 <= new_col < 3:  
            new_index = new_row * 3 + new_col  
            new_state = node.state[:]  
            new_state[empty_pos], new_state[new_index] = new_state[new_index], new_state[empty_pos]  
            h_cost = manhattan_distance(new_state, target_state)  
            successor_node = Node(new_state, node, move, node.cost_g + 1, h_cost)  
            successors.append(successor_node)  
    return successors  


def a_star_search(start_state, target_state):  
    open_set = []  
    closed_set = set()  

    start_node = Node(start_state, None, None, 0, manhattan_distance(start_state, target_state))  
    heapq.heappush(open_set, start_node)  

    while open_set:  
        current_node = heapq.heappop(open_set)  

        if current_node.state == target_state:  
            path = []  
            while current_node.parent:  
                path.append(current_node)  
                current_node = current_node.parent  
            return path[::-1]  

        closed_set.add(tuple(current_node.state))  

        for successor in generate_successors(current_node, target_state):  
            if tuple(successor.state) in closed_set:  
                continue  
            heapq.heappush(open_set, successor)  

    return None  