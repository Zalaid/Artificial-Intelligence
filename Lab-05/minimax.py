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