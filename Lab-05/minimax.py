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