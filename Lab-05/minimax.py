class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state  

    def is_terminal(self, state):
        return self.check_for_winner(state) or self.check_for_draw(state)

    def utility(self,state):
        winner = self.check_for_winner(state)
        if winner == 'X':
            return 1 
        elif winner == 'O':
            return -1  
        else:
            return 0 
        

    def minimax(self, state, depth, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for child in self.get_possible_moves(state):
                eval = self.minimax(child, depth + 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.get_possible_moves(state):
                eval = self.minimax(child, depth + 1, True)
                min_eval = min(min_eval, eval)
            return min_eval
        
    def best_move(self, state):
        best_val = float('-inf')
        best_move = None
        for move in self.get_possible_moves(state):
            move_val = self.minimax(move, 0, False)  
            if move_val > best_val:
                best_val = move_val
                best_move = move
        return best_move
    

    def check_for_winner(self, state):
        for row in state:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]  
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] != ' ':
                return state[0][col] 
        if state[0][0] == state[1][1] == state[2][2] != ' ':
            return state[0][0] 
        if state[0][2] == state[1][1] == state[2][0] != ' ':
            return state[0][2]  
        return None  

    def check_for_draw(self, state):
        return all(cell != ' ' for row in state for cell in row)

    def get_possible_moves(self, state):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':  
                    new_state = [row[:] for row in state]  
                    new_state[i][j] = 'X' 
                    possible_moves.append(new_state)
        return possible_moves

if __name__ == "__main__":
    initial_state = [
        ['X', 'O', 'X'],
        [' ', 'O', ' '],
        [' ', ' ', ' ']
    ]

    minimax = Minimax(initial_state)
    best_move = minimax.best_move(initial_state)
    
    print("Best move for X:")
    for row in best_move:
        print(row)