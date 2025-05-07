class Player:
    def __init__(self, name, is_bot=False):
        self.name = name
        self.is_bot = is_bot

    def get_move(self, available_moves):
        """
        Perform a move. The method must be implemented in subclasses, since we plan to have different kind of AI players
        :param available_moves: List of valid positions where a move can be made.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, is_bot=False)

    def get_move(self, available_moves):
        while True:
            try:
                move = int(input(f'{self.name}, Enter your move (1-9): '))
                if move in available_moves:
                    return move
                print(f"Invalid move. Available moves are: {available_moves}")
            except ValueError:
                print("Please enter a valid integer between 1 and 9.")


class Grid:
    def __init__(self):
        self.state = {i: ' ' for i in range(1, 10)}

    def print_grid(self):
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')
        print(
            f'\t \t {self.state[1] or ""} \t \t | \t \t {self.state[2] or ""} \t \t | \t \t {self.state[3] or ""} \t \t')
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')
        print('\t -------- \t | \t -------- \t | \t --------')
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')
        print(
            f'\t \t {self.state[4] or ""} \t \t | \t \t {self.state[5] or ""} \t \t | \t \t {self.state[6] or ""} \t \t')
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')
        print('\t -------- \t | \t -------- \t | \t --------')
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')
        print(
            f'\t \t {self.state[7] or ""} \t \t | \t \t {self.state[8] or ""} \t \t | \t \t {self.state[9] or ""} \t \t')
        print(f'\t \t \t \t | \t \t \t \t | \t \t \t \t')

    def make_move(self, position, marker):
        if self.state[position] == ' ':
            self.state[position] = marker
            return True
        return False

    def get_available_moves(self):
        return [key for key, value in self.state.items() if value == ' ']


class Game:
    def __init__(self):
        self.grid = Grid()
        self.available_modes = {1: 'Player v/s Player'}
        self.players = []
        self.current_player_index = 0

    def setup(self):
        print('Welcome to Tic Tac Toe!')
        while True:
            print('Choose a mode:')
            for key, value in self.available_modes.items():
                print(f'{key}. {value}')
            mode_choice = int(input('Enter your choice: '))
            if mode_choice == 1:
                p1 = HumanPlayer(input('Player 1, Enter your name: '))
                p2 = HumanPlayer(input('Player 2, Enter your name: '))
            else:
                print('Invalid choice. Choose again.')
                continue
            self.players = [p1, p2]
            break

    def evaluate(self):
        if ((self.grid.state[1] == self.grid.state[2] == self.grid.state[3] != ' ') |
            (self.grid.state[4] == self.grid.state[5] == self.grid.state[6] != ' ') |
            (self.grid.state[7] == self.grid.state[8] == self.grid.state[9] != ' ') |
            (self.grid.state[1] == self.grid.state[4] == self.grid.state[7] != ' ') |
            (self.grid.state[2] == self.grid.state[5] == self.grid.state[8] != ' ') |
            (self.grid.state[3] == self.grid.state[6] == self.grid.state[9] != ' ') |
            (self.grid.state[1] == self.grid.state[5] == self.grid.state[9] != ' ') |
            (self.grid.state[3] == self.grid.state[5] == self.grid.state[7] != ' ')):
            return True
        else:
            return False

    def play(self):
        print("Game Start!")
        while True:
            self.grid.print_grid()
            current_player = self.players[self.current_player_index]
            available_moves = self.grid.get_available_moves()
            move = current_player.get_move(available_moves)  # Pass available_moves here

            if self.grid.make_move(move, 'X' if self.current_player_index == 0 else 'O'):
                print(f'{current_player.name} makes a move at position {move}')
                if self.evaluate():
                    print(f'{current_player.name} wins!')
                    print('Game Over!')
                    break
                if not self.grid.get_available_moves():
                    print('Draw!')
                    print('Game Over!')
                    break
                self.current_player_index = 1 - self.current_player_index
            else:
                print('Invalid move, try again.')



            # Check for game end (win/draw) here

