# Reversi: A 2D AI Strategy Game

A 2D Reversi board game developed using Python and Pygame. The game allows a human player to play against an AI opponent with different difficulty levels.

## Project Overview

Reversi is a two-player strategy board game played on an 8×8 board. Players place discs on the board and capture the opponent's discs by surrounding them.

In this project, the human player competes against an AI player. The AI analyzes possible moves and selects a suitable move using game-tree search techniques.

## Features

* 8×8 Reversi board
* Human vs AI gameplay
* Black and White disc selection
* Easy, Medium and Hard difficulty levels
* Legal move detection
* Automatic disc flipping
* Score tracking
* Game-over detection
* AI move selection
* Minimax algorithm
* Alpha-Beta Pruning
* Pygame-based graphical interface

## AI Algorithms

### Minimax

The Minimax algorithm explores possible future game states and evaluates the available moves. The AI tries to maximize its advantage while assuming that the opponent will try to minimize it.

### Alpha-Beta Pruning

Alpha-Beta Pruning improves the Minimax search by eliminating branches that do not need to be evaluated.

This allows the AI to search the game tree more efficiently without changing the final Minimax decision.

## Difficulty Levels

The game provides three difficulty levels:

* Easy — uses a lower search depth and weaker move selection, giving the human player a stronger chance.
* Medium — provides a more balanced gameplay experience.
* Hard — uses deeper search and stronger move evaluation.

The difficulty is implemented by changing the AI's search behavior rather than guaranteeing a fixed winning percentage.

## Technologies Used

* Python
* Pygame
* Minimax
* Alpha-Beta Pruning

## Project Structure

```text
AI-PROJECT/
│
├── main.py
├── game.py
├── board.py
├── ai.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `main.py`

Handles the main Pygame interface, screens, user interaction and game flow.

### `game.py`

Controls the game state, turns, moves and game-over conditions.

### `board.py`

Contains the Reversi board representation, legal move detection, disc flipping and score calculation.

### `ai.py`

Contains the AI logic, including Minimax, Alpha-Beta Pruning, search depth and move evaluation.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Reversi-AI-Game.git
```

### 2. Open the project folder

```bash
cd Reversi-AI-Game
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python main.py
```

## Requirements

* Python 3.x
* Pygame 2.6.1

## Gameplay

1. Start the game.
2. Select your disc colour.
3. Select the difficulty level.
4. Place your disc on a valid position.
5. The AI will make its move.
6. Continue until the game ends.
7. The player with the higher number of discs wins.

## Academic Project

This project was developed as an Artificial Intelligence course project to demonstrate game-playing AI using Minimax and Alpha-Beta Pruning.

## Author

Tanmoy Dev

## License

This project is intended for educational purposes.
