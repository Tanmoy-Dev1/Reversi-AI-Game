import random

from board import get_valid_moves, make_move, BLACK, WHITE


class AI:

    def __init__(self, color, level="medium"):

        # Store AI colour
        self.color = color

        # Store difficulty level
        self.level = level

    def get_moves(self, board):

        # Get all valid moves for AI
        return get_valid_moves(
            board,
            self.color
        )

    def evaluate(self, board):

        # Find opponent colour
        opponent = (
            BLACK
            if self.color == WHITE
            else WHITE
        )

        my_disks = 0
        opponent_disks = 0

        # Count AI and opponent disks
        for row in board:

            for cell in row:

                if cell == self.color:
                    my_disks += 1

                elif cell == opponent:
                    opponent_disks += 1

        # Difference between disks
        disk_score = (
            my_disks - opponent_disks
        )

        # Count available moves
        my_moves = len(
            get_valid_moves(
                board,
                self.color
            )
        )

        opponent_moves = len(
            get_valid_moves(
                board,
                opponent
            )
        )

        # Difference between available moves
        mobility_score = (
            my_moves - opponent_moves
        )

        # Corner positions
        corners = [
            (0, 0),
            (0, 7),
            (7, 0),
            (7, 7)
        ]

        corner_score = 0

        # Give high value to corners
        for row, col in corners:

            if board[row][col] == self.color:

                corner_score += 25

            elif board[row][col] == opponent:

                corner_score -= 25

        edge_score = 0

        # Give small value to edge positions
        for i in range(8):

            if board[0][i] == self.color:
                edge_score += 2

            elif board[0][i] == opponent:
                edge_score -= 2

            if board[7][i] == self.color:
                edge_score += 2

            elif board[7][i] == opponent:
                edge_score -= 2

            if board[i][0] == self.color:
                edge_score += 2

            elif board[i][0] == opponent:
                edge_score -= 2

            if board[i][7] == self.color:
                edge_score += 2

            elif board[i][7] == opponent:
                edge_score -= 2

        # Final evaluation score
        score = (
            disk_score
            + mobility_score * 3
            + corner_score
            + edge_score
        )

        return score

    def get_depth(self):

        # Easy uses very shallow search
        if self.level == "easy":

            return 1

        # Medium searches deeper
        elif self.level == "medium":

            return 3

        # Hard searches deepest
        else:

            return 4

    def get_weak_move(self, board):

        # Get all legal moves
        moves = self.get_moves(board)

        if len(moves) == 0:

            return None

        # Store weak moves
        weak_moves = []

        # Find moves that do not take corners
        for move in moves:

            if move not in [
                (0, 0),
                (0, 7),
                (7, 0),
                (7, 7)
            ]:

                weak_moves.append(move)

        # Prefer a non-corner random move
        if len(weak_moves) > 0:

            return random.choice(
                weak_moves
            )

        # If only corners are available
        return random.choice(moves)

    def get_easy_move(self, board):

        # Get all legal moves
        moves = self.get_moves(board)

        if len(moves) == 0:

            return None

        # 96% chance of making a weak random move
        if random.random() < 0.96:

            return self.get_weak_move(
                board
            )

        # 4% chance of making a better move
        return self.get_best_depth_one_move(
            board
        )

    def get_best_depth_one_move(self, board):

        # Get all legal moves
        moves = self.get_moves(board)

        if len(moves) == 0:

            return None

        best_move = moves[0]
        best_score = -999999

        # Check each possible move
        for move in moves:

            # Create board copy
            new_board = [
                row[:]
                for row in board
            ]

            # Try the move
            make_move(
                new_board,
                move[0],
                move[1],
                self.color
            )

            # Evaluate resulting board
            score = self.evaluate(
                new_board
            )

            # Keep the better move
            if score > best_score:

                best_score = score
                best_move = move

        return best_move

    def minimax(
        self,
        board,
        depth,
        maximizing,
        alpha,
        beta
    ):

        # Find opponent colour
        opponent = (
            BLACK
            if self.color == WHITE
            else WHITE
        )

        # Stop search at depth zero
        if depth == 0:

            return self.evaluate(board)

        # Decide whose turn it is
        if maximizing:

            player = self.color

        else:

            player = opponent

        # Get valid moves
        moves = get_valid_moves(
            board,
            player
        )

        # Handle no available move
        if len(moves) == 0:

            other_player = (
                opponent
                if player == self.color
                else self.color
            )

            other_moves = get_valid_moves(
                board,
                other_player
            )

            # Game over
            if len(other_moves) == 0:

                return self.evaluate(
                    board
                )

            # Player passes
            return self.minimax(
                board,
                depth - 1,
                not maximizing,
                alpha,
                beta
            )

        # Maximizing player
        if maximizing:

            best_score = -999999

            for move in moves:

                # Copy board
                new_board = [
                    row[:]
                    for row in board
                ]

                # Make move
                make_move(
                    new_board,
                    move[0],
                    move[1],
                    player
                )

                # Search next level
                score = self.minimax(
                    new_board,
                    depth - 1,
                    False,
                    alpha,
                    beta
                )

                # Keep highest score
                if score > best_score:

                    best_score = score

                # Update alpha
                if best_score > alpha:

                    alpha = best_score

                # Alpha-Beta pruning
                if beta <= alpha:

                    break

            return best_score

        # Minimizing player
        else:

            best_score = 999999

            for move in moves:

                # Copy board
                new_board = [
                    row[:]
                    for row in board
                ]

                # Make move
                make_move(
                    new_board,
                    move[0],
                    move[1],
                    player
                )

                # Search next level
                score = self.minimax(
                    new_board,
                    depth - 1,
                    True,
                    alpha,
                    beta
                )

                # Keep lowest score
                if score < best_score:

                    best_score = score

                # Update beta
                if best_score < beta:

                    beta = best_score

                # Alpha-Beta pruning
                if beta <= alpha:

                    break

            return best_score

    def choose_move(self, board):

        # Easy mode uses weak behaviour
        if self.level == "easy":

            return self.get_easy_move(
                board
            )

        # Get AI legal moves
        moves = self.get_moves(board)

        if len(moves) == 0:

            return None

        # Get search depth
        depth = self.get_depth()

        best_move = moves[0]
        best_score = -999999

        # Check every possible AI move
        for move in moves:

            # Copy board
            new_board = [
                row[:]
                for row in board
            ]

            # Make AI move
            make_move(
                new_board,
                move[0],
                move[1],
                self.color
            )

            # Minimax with Alpha-Beta
            score = self.minimax(
                new_board,
                depth - 1,
                False,
                -999999,
                999999
            )

            # Select highest score
            if score > best_score:

                best_score = score
                best_move = move

        return best_move


# Test AI
if __name__ == "__main__":

    from board import create_board

    board = create_board()

    # Test Easy
    easy_ai = AI(
        WHITE,
        "easy"
    )

    print("Easy AI")
    print("Colour:", easy_ai.color)
    print("Level:", easy_ai.level)
    print("Moves:", easy_ai.get_moves(board))
    print(
        "Selected:",
        easy_ai.choose_move(board)
    )

    # Test Medium
    medium_ai = AI(
        WHITE,
        "medium"
    )

    print("\nMedium AI")
    print("Depth:", medium_ai.get_depth())
    print(
        "Selected:",
        medium_ai.choose_move(board)
    )

    # Test Hard
    hard_ai = AI(
        WHITE,
        "hard"
    )

    print("\nHard AI")
    print("Depth:", hard_ai.get_depth())
    print(
        "Selected:",
        hard_ai.choose_move(board)
    )