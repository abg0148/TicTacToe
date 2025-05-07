# Command-Line Based TicTacToe Game

This project is a Python-based command-line game that supports multiple modes of play. Players interact with a virtual grid to make moves, and the game can be played repeatedly. The program is designed to provide a smooth gaming experience, with easy setup and intuitive gameplay mechanics.


## Features

- **Interactive Gameplay**: Players take turns making moves in a grid-based game.
- **Multiple Play Modes**: Choose between different player types, including human players and bots (NOT YET AVAILABLE).
- **Replay Option**: After a match, the game prompts for replayability.
- **Dynamic Grid Interaction**: The game board updates in real-time and displays moves as they are played.


## How to Run the Game

1. Clone the repository or download the project files.
2. Ensure Python 3 is installed on your system.
3. Open a terminal in the project directory.
4. Run the game with the following command:
   ```bash
   python lets-play.py
   ```
5. Follow the on-screen prompts to set up and play the game.


## Class Overview

The project is organized around the following key classes:

### `Player`
- Represents a generic player in the game.
- Attributes:
  - `name`: The name of the player.
  - `is_bot`: Defines whether the player is a bot or a human.
- Methods:
  - `__init__`: Constructor to initialize the player.
  - `get_move`: Retrieves a move from the player (manually for humans, programmatically for bots).

### `HumanPlayer`
- Inherits from `Player`, representing a human-specific player.
- Methods:
  - `__init__`: Initializes the human player.
  - `get_move`: Gets the move input from the user.

### `Grid`
- Represents the game board.
- Attributes:
  - `state`: The current state of the game board.
- Methods:
  - `__init__`: Initializes a fresh grid.
  - `print_grid`: Prints the grid to the console.
  - `make_move`: Executes a move on the grid.
  - `get_available_moves`: Retrieves all moves currently available.

### `Game`
- Manages the game's logic, flow, and user experience.
- Attributes:
  - `grid`: An instance of the `Grid` class.
  - `players`: A list of participating players.
  - `available_modes`: The different modes of gameplay offered.
- Methods:
  - `__init__`: Sets up the initial game state.
  - `setup`: Configures the game based on player choices.
  - `evaluate`: Checks for game-winning conditions or a tie.
  - `play`: Manages the main loop for running the game.


## How the Game Works

1. After launching, you will first configure the game, selecting players and modes.
2. Moves proceed turn-by-turn as players interact with the grid.
3. The game state is updated dynamically, and a win or tie condition is evaluated at the end of each turn.
4. After each match, you're given the option to restart or exit.


## Prerequisites

- Python 3.6 or higher


## Contributing

Contributions are welcome! If you'd like to improve this game or add new features:

1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as per the license terms.
