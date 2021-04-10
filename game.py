import os

# class for the game itself
class Game:
    def __init__(self):
        self.current_turn = 'O'
        self.gameboard = [GamePiece(x) for x in range(9)]
        self.winner = None
        self.winning_states = [
            # horizontals
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            # diagonals
            [0, 4, 8],
            [2, 4, 6],
            # verticals
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8]
        ]
        # Loop turns until winner state is found
        while self.winner == None:
            # This will clear the terminal every time it loops
            os.system('clear')
            self.print_board()
            self.get_play()
            os.system('clear')
            self.print_board()
            self.check_winner()
            self.switch_turn()
        print(f'{self.winner} has won!!')
    def __str__(self):
        return str(self.gameboard)
    def switch_turn(self):
        if self.current_turn == 'O':
            self.current_turn = 'X'
        elif self.current_turn == 'X':
            self.current_turn = 'O'
        return
    def print_board(self):
        print(
            f" {self.gameboard[0]} | {self.gameboard[1]} | {self.gameboard[2]} \n - - - - - \n {self.gameboard[3]} | {self.gameboard[4]} | {self.gameboard[5]} \n - - - - - \n {self.gameboard[6]} | {self.gameboard[7]} | {self.gameboard[8]}"
        )
    def get_play(self):
        # Loop until valid play
        while True:
            print(f'Current Player: {self.current_turn}')
            play_index = input('Please input a square between 0-8: ')
            space = self.gameboard[int(play_index)]
            print(space)
            if space.mark == ' ':
                space.set_mark(self.current_turn)
                return
            else:
                print('This space has already been played')
    def check_winner(self):
        # check ALL of the win condition options
        for state in self.winning_states:
            # track number of unplayed spaces
            num_spaces = 0
            for obj in self.gameboard:
                if obj.mark == ' ':
                    num_spaces += 1
            # X win options        
            if self.gameboard[state[0]].mark == 'X' and self.gameboard[state[
                    1]].mark == 'X' and self.gameboard[state[2]].mark == 'X':
                self.winner = 'X'
                return True
            # O win options
            elif self.gameboard[state[0]].mark == 'O' and self.gameboard[state[
                    1]].mark == 'O' and self.gameboard[state[2]].mark == 'O':
                self.winner = 'O'
                return True
            # tie condition    
            elif num_spaces == 0:
                self.winner = "Nobody"
                return
        return False

# class for each of the nine spaces        
class GamePiece:
    def __init__(self, position):
        self.mark = ' '
        self.position = position
    def __str__(self):
        return self.mark
    def set_mark(self, mark):
        self.mark = mark


# Run the game!        
test_game = Game()


