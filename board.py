# =============================
# board.py
# Reversi Board Management
# =============================


# Board size is 8 x 8
BOARD_SIZE = 8


# Board values
EMPTY = 0
BLACK = 1
WHITE = 2


# All 8 possible directions
DIRECTIONS = [
    (-1, -1),   # Up-Left
    (-1, 0),    # Up
    (-1, 1),    # Up-Right
    (0, -1),    # Left
    (0, 1),     # Right
    (1, -1),    # Down-Left
    (1, 0),     # Down
    (1, 1)      # Down-Right
]


# =============================
# Create Initial Board
# =============================

def create_board():

    # Create an empty 8 x 8 board
    board = [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],

        # Initial four discs
        [EMPTY, EMPTY, EMPTY, WHITE, BLACK, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, BLACK, WHITE, EMPTY, EMPTY, EMPTY],

        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
    ]

    return board


# =============================
# Check Position
# =============================

def inside_board(row, col):

    # Check whether the position is inside 8 x 8 board
    return (
        0 <= row < BOARD_SIZE
        and
        0 <= col < BOARD_SIZE
    )


# =============================
# Check Whether Move is Valid
# =============================

def is_valid_move(board, row, col, player):

    # The selected cell must be empty
    if board[row][col] != EMPTY:
        return False

    # Find opponent colour
    if player == BLACK:
        opponent = WHITE
    else:
        opponent = BLACK

    # Check all 8 directions
    for dr, dc in DIRECTIONS:

        r = row + dr
        c = col + dc

        found_opponent = False

        # Look for opponent discs in this direction
        while (
            inside_board(r, c)
            and board[r][c] == opponent
        ):

            found_opponent = True

            r += dr
            c += dc

        # A valid move needs opponent disc(s)
        # followed by the player's own disc
        if (
            found_opponent
            and inside_board(r, c)
            and board[r][c] == player
        ):

            return True

    return False


# =============================
# Get All Valid Moves
# =============================

def get_valid_moves(board, player):

    valid_moves = []

    # Check every cell on the board
    for row in range(BOARD_SIZE):

        for col in range(BOARD_SIZE):

            if is_valid_move(
                board,
                row,
                col,
                player
            ):

                valid_moves.append(
                    (row, col)
                )

    return valid_moves


# =============================
# Make Move and Flip Discs
# =============================

def make_move(board, row, col, player):

    # Check whether the move is valid
    if not is_valid_move(
        board,
        row,
        col,
        player
    ):

        # Return an empty list if move is invalid
        return []

    # Find opponent colour
    if player == BLACK:
        opponent = WHITE
    else:
        opponent = BLACK

    # Place the player's disc
    board[row][col] = player

    # Store all discs that are flipped
    flipped_discs = []

    # Check all 8 directions
    for dr, dc in DIRECTIONS:

        r = row + dr
        c = col + dc

        # Temporarily store opponent discs
        # found in this direction
        disks_to_flip = []

        # Continue while opponent discs are found
        while (
            inside_board(r, c)
            and board[r][c] == opponent
        ):

            disks_to_flip.append(
                (r, c)
            )

            r += dr
            c += dc

        # If our own disc closes the line,
        # all collected opponent discs are flipped
        if (
            disks_to_flip
            and inside_board(r, c)
            and board[r][c] == player
        ):

            for flip_row, flip_col in disks_to_flip:

                # Change opponent disc to player's disc
                board[flip_row][flip_col] = player

                # Save the position for visual highlight
                flipped_discs.append(
                    (flip_row, flip_col)
                )

    # Return positions of all flipped discs
    return flipped_discs


# =============================
# Count Discs
# =============================

def count_disks(board, player):

    count = 0

    # Check every cell
    for row in board:

        for cell in row:

            if cell == player:
                count += 1

    return count


# =============================
# Check Whether Board is Full
# =============================

def is_board_full(board):

    # Check every cell
    for row in board:

        for cell in row:

            # Empty cell means board is not full
            if cell == EMPTY:
                return False

    return True


# =============================
# TEST BOARD.PY
# =============================

if __name__ == "__main__":

    # Create starting board
    board = create_board()

    print("Initial Board:")

    for row in board:
        print(row)

    # Show valid moves for Black
    print("\nValid moves for BLACK:")

    print(
        get_valid_moves(
            board,
            BLACK
        )
    )

    # Test a Black move
    print("\nMaking move at (2, 3)...")

    flipped = make_move(
        board,
        2,
        3,
        BLACK
    )

    # Show which discs were flipped
    print(
        "Flipped discs:",
        flipped
    )

    # Show board after move
    print("\nBoard after move:")

    for row in board:
        print(row)

    # Show scores
    print(
        "\nBlack disks:",
        count_disks(board, BLACK)
    )

    print(
        "White disks:",
        count_disks(board, WHITE)
    )

    # Check whether board is full
    print(
        "\nBoard full:",
        is_board_full(board)
    )