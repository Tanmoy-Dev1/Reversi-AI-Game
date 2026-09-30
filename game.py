from board import (
    create_board,
    get_valid_moves,
    make_move,
    count_disks,
    is_board_full,
    BLACK,
    WHITE
)


class Game:

    def __init__(self, human_color, first_player):

        # Create the starting Reversi board
        self.board = create_board()

        # Store the human player's colour
        self.human_color = human_color

        # Set the AI colour opposite to the human colour
        if human_color == BLACK:
            self.ai_color = WHITE
        else:
            self.ai_color = BLACK

        # Set who will play first
        self.current_player = first_player

        # Game status
        self.game_over = False
        self.winner = None

        # Store the discs flipped by the latest move
        self.last_flipped = []

        # Store the board before the latest human move
        self.previous_board = None

        # Store the player before the latest human move
        self.previous_player = None

        # Control whether rewind is available
        self.can_rewind = False

    def get_current_moves(self):

        # Get all valid moves for the current player
        return get_valid_moves(
            self.board,
            self.current_player
        )

    def save_human_state(self):

        # Save a copy of the board before human move
        self.previous_board = [
            row[:]
            for row in self.board
        ]

        # Save the current player
        self.previous_player = (
            self.current_player
        )

        # Enable rewind
        self.can_rewind = True

    def make_move(self, row, col):

        # Do not allow moves after the game ends
        if self.game_over:
            return False

        # Get valid moves for the current player
        moves = self.get_current_moves()

        # Check whether the selected position is valid
        if (row, col) not in moves:
            return False

        # Make the move and store flipped discs
        self.last_flipped = make_move(
            self.board,
            row,
            col,
            self.current_player
        )

        # Change to the other player's turn
        self.change_turn()

        # Check whether the game should continue or end
        self.check_game_status()

        return True

    def rewind(self):

        # Rewind is not available
        if not self.can_rewind:
            return False

        # Restore the board from before the human move
        self.board = [
            row[:]
            for row in self.previous_board
        ]

        # Restore the human player's turn
        self.current_player = (
            self.previous_player
        )

        # Remove the previous flipped-disc highlight
        self.last_flipped = []

        # Disable rewind after using it once
        self.can_rewind = False

        # Make sure the game is active
        self.game_over = False
        self.winner = None

        return True

    def change_turn(self):

        # Change Black's turn to White
        if self.current_player == BLACK:

            self.current_player = WHITE

        # Change White's turn to Black
        else:

            self.current_player = BLACK

    def check_game_status(self):

        # If the board is completely full, the game ends
        if is_board_full(self.board):

            self.end_game()
            return

        # Get valid moves for the current player
        current_moves = get_valid_moves(
            self.board,
            self.current_player
        )

        # Check if the current player has no valid move
        if len(current_moves) == 0:

            # Find the other player
            other_player = (
                BLACK
                if self.current_player == WHITE
                else WHITE
            )

            # Get valid moves for the other player
            other_moves = get_valid_moves(
                self.board,
                other_player
            )

            # If neither player can move, the game ends
            if len(other_moves) == 0:

                self.end_game()

            # Otherwise, the current player must pass
            else:

                self.change_turn()

    def end_game(self):

        # Mark the game as finished
        self.game_over = True

        # Count Black discs
        black_score = count_disks(
            self.board,
            BLACK
        )

        # Count White discs
        white_score = count_disks(
            self.board,
            WHITE
        )

        # Decide the winner
        if black_score > white_score:

            self.winner = BLACK

        elif white_score > black_score:

            self.winner = WHITE

        # Equal scores mean a draw
        else:

            self.winner = None

    def get_score(self):

        # Count Black discs
        black_score = count_disks(
            self.board,
            BLACK
        )

        # Count White discs
        white_score = count_disks(
            self.board,
            WHITE
        )

        # Return both scores
        return black_score, white_score