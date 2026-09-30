import pygame
import sys

from board import get_valid_moves, count_disks, BLACK, WHITE
from game import Game
from ai import AI


# Start Pygame
pygame.init()


# Window settings
WIDTH = 640
HEIGHT = 760
CELL_SIZE = 80

BOARD_SIZE = 640
INFO_HEIGHT = 120


# Create game window
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Reversi - Human vs AI"
)


# Game colours
BACKGROUND_COLOR = (25, 25, 25)
BOARD_COLOR = (34, 139, 34)
GRID_COLOR = (20, 90, 20)

BLACK_COLOR = (15, 15, 15)
WHITE_COLOR = (245, 245, 245)

MOVE_COLOR = (255, 220, 50)
LAST_MOVE_COLOR = (255, 170, 0)
FLIP_COLOR = (80, 200, 255)


# Show game instructions
def how_to_play():

    title_font = pygame.font.Font(
        None,
        60
    )

    text_font = pygame.font.Font(
        None,
        27
    )

    back_font = pygame.font.Font(
        None,
        30
    )

    # Create back button
    back_button = pygame.Rect(
        220,
        650,
        200,
        55
    )

    while True:

        screen.fill(
            (25, 35, 30)
        )

        # Draw title
        title = title_font.render(
            "HOW TO PLAY",
            True,
            WHITE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 70)
            )
        )

        # Game instructions
        instructions = [
            "Place your disc on a valid position.",
            "Surround opponent discs to flip them.",
            "Yellow dots show valid moves.",
            "Blue circles show flipped discs.",
            "Yellow box shows the latest move.",
            "Corners are valuable positions.",
            "If no move is possible, the turn is passed.",
            "The player with more discs wins."
        ]

        y = 140

        # Display each instruction
        for line in instructions:

            text = text_font.render(
                line,
                True,
                (220, 220, 220)
            )

            screen.blit(
                text,
                (45, y)
            )

            y += 52

        # Draw back button
        pygame.draw.rect(
            screen,
            (50, 120, 75),
            back_button,
            border_radius=10
        )

        back_text = back_font.render(
            "BACK",
            True,
            WHITE_COLOR
        )

        screen.blit(
            back_text,
            back_text.get_rect(
                center=back_button.center
            )
        )

        pygame.display.update()

        # Handle buttons
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.collidepoint(
                    event.pos
                ):

                    return


# Show opening screen
def opening_screen():

    title_font = pygame.font.Font(
        None,
        100
    )

    button_font = pygame.font.Font(
        None,
        38
    )

    # Create menu buttons
    play_button = pygame.Rect(
        190,
        330,
        260,
        65
    )

    how_button = pygame.Rect(
        190,
        420,
        260,
        65
    )

    exit_button = pygame.Rect(
        190,
        510,
        260,
        65
    )

    while True:

        screen.fill(
            (20, 80, 50)
        )

        # Draw game title
        title = title_font.render(
            "REVERSI",
            True,
            WHITE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 150)
            )
        )

        # Draw sample black disc
        pygame.draw.circle(
            screen,
            (70, 70, 70),
            (270, 250),
            44
        )

        pygame.draw.circle(
            screen,
            BLACK_COLOR,
            (265, 244),
            44
        )

        # Draw sample white disc
        pygame.draw.circle(
            screen,
            (120, 120, 120),
            (370, 250),
            44
        )

        pygame.draw.circle(
            screen,
            WHITE_COLOR,
            (365, 244),
            44
        )

        mouse_pos = pygame.mouse.get_pos()

        # Change button colour when mouse is over it
        if play_button.collidepoint(mouse_pos):
            play_color = (60, 160, 100)
        else:
            play_color = (40, 120, 75)

        if how_button.collidepoint(mouse_pos):
            how_color = (70, 130, 180)
        else:
            how_color = (50, 100, 150)

        if exit_button.collidepoint(mouse_pos):
            exit_color = (160, 70, 70)
        else:
            exit_color = (120, 50, 50)

        # Draw menu buttons
        pygame.draw.rect(
            screen,
            play_color,
            play_button,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            how_color,
            how_button,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            exit_color,
            exit_button,
            border_radius=12
        )

        # Create button text
        play_text = button_font.render(
            "PLAY GAME",
            True,
            WHITE_COLOR
        )

        how_text = button_font.render(
            "HOW TO PLAY",
            True,
            WHITE_COLOR
        )

        exit_text = button_font.render(
            "EXIT",
            True,
            WHITE_COLOR
        )

        # Display button text
        screen.blit(
            play_text,
            play_text.get_rect(
                center=play_button.center
            )
        )

        screen.blit(
            how_text,
            how_text.get_rect(
                center=how_button.center
            )
        )

        screen.blit(
            exit_text,
            exit_text.get_rect(
                center=exit_button.center
            )
        )

        pygame.display.update()

        # Handle menu buttons
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(
                    event.pos
                ):

                    return

                if how_button.collidepoint(
                    event.pos
                ):

                    how_to_play()

                if exit_button.collidepoint(
                    event.pos
                ):

                    pygame.quit()
                    sys.exit()


# Choose player's disc colour
def choose_colour():

    title_font = pygame.font.Font(
        None,
        55
    )

    small_font = pygame.font.Font(
        None,
        30
    )

    # Create colour cards
    black_card = pygame.Rect(
        80,
        260,
        220,
        260
    )

    white_card = pygame.Rect(
        340,
        260,
        220,
        260
    )

    while True:

        screen.fill(
            (25, 30, 28)
        )

        # Draw title
        title = title_font.render(
            "Choose Your Disc",
            True,
            WHITE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 150)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        # Check mouse position
        black_hover = black_card.collidepoint(
            mouse_pos
        )

        white_hover = white_card.collidepoint(
            mouse_pos
        )

        # Highlight black card
        if black_hover:
            black_border = (255, 200, 50)
        else:
            black_border = (90, 90, 90)

        # Highlight white card
        if white_hover:
            white_border = (255, 200, 50)
        else:
            white_border = (90, 90, 90)

        # Draw black card
        pygame.draw.rect(
            screen,
            (35, 35, 35),
            black_card,
            border_radius=18
        )

        pygame.draw.rect(
            screen,
            black_border,
            black_card,
            4,
            border_radius=18
        )

        # Draw white card
        pygame.draw.rect(
            screen,
            (55, 55, 55),
            white_card,
            border_radius=18
        )

        pygame.draw.rect(
            screen,
            white_border,
            white_card,
            4,
            border_radius=18
        )

        # Draw black disc
        pygame.draw.circle(
            screen,
            (80, 80, 80),
            (195, 370),
            65
        )

        pygame.draw.circle(
            screen,
            BLACK_COLOR,
            (190, 363),
            65
        )

        # Draw white disc
        pygame.draw.circle(
            screen,
            (120, 120, 120),
            (455, 370),
            65
        )

        pygame.draw.circle(
            screen,
            WHITE_COLOR,
            (450, 363),
            65
        )

        # Draw colour names
        black_text = small_font.render(
            "BLACK",
            True,
            WHITE_COLOR
        )

        white_text = small_font.render(
            "WHITE",
            True,
            WHITE_COLOR
        )

        screen.blit(
            black_text,
            black_text.get_rect(
                center=(190, 470)
            )
        )

        screen.blit(
            white_text,
            white_text.get_rect(
                center=(450, 470)
            )
        )

        pygame.display.update()

        # Handle colour selection
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if black_card.collidepoint(
                    event.pos
                ):

                    return BLACK

                if white_card.collidepoint(
                    event.pos
                ):

                    return WHITE


# Choose AI difficulty
def choose_difficulty():

    font = pygame.font.Font(
        None,
        55
    )

    button_font = pygame.font.Font(
        None,
        38
    )

    # Create difficulty buttons
    easy_button = pygame.Rect(
        190,
        260,
        260,
        65
    )

    medium_button = pygame.Rect(
        190,
        350,
        260,
        65
    )

    hard_button = pygame.Rect(
        190,
        440,
        260,
        65
    )

    while True:

        screen.fill(
            (30, 30, 30)
        )

        # Draw title
        title = font.render(
            "Choose Difficulty",
            True,
            WHITE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 170)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        # Highlight buttons
        if easy_button.collidepoint(mouse_pos):
            easy_color = (70, 170, 100)
        else:
            easy_color = (50, 130, 75)

        if medium_button.collidepoint(mouse_pos):
            medium_color = (80, 130, 190)
        else:
            medium_color = (60, 100, 150)

        if hard_button.collidepoint(mouse_pos):
            hard_color = (180, 70, 70)
        else:
            hard_color = (140, 50, 50)

        # Draw buttons
        pygame.draw.rect(
            screen,
            easy_color,
            easy_button,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            medium_color,
            medium_button,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            hard_color,
            hard_button,
            border_radius=10
        )

        # Create button text
        easy_text = button_font.render(
            "EASY",
            True,
            WHITE_COLOR
        )

        medium_text = button_font.render(
            "MEDIUM",
            True,
            WHITE_COLOR
        )

        hard_text = button_font.render(
            "HARD",
            True,
            WHITE_COLOR
        )

        # Display button text
        screen.blit(
            easy_text,
            easy_text.get_rect(
                center=easy_button.center
            )
        )

        screen.blit(
            medium_text,
            medium_text.get_rect(
                center=medium_button.center
            )
        )

        screen.blit(
            hard_text,
            hard_text.get_rect(
                center=hard_button.center
            )
        )

        pygame.display.update()

        # Handle difficulty selection
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if easy_button.collidepoint(
                    event.pos
                ):

                    return "easy"

                if medium_button.collidepoint(
                    event.pos
                ):

                    return "medium"

                if hard_button.collidepoint(
                    event.pos
                ):

                    return "hard"


# Choose who plays first
def choose_first_player(
    human_color,
    ai_color
):

    font = pygame.font.Font(
        None,
        55
    )

    button_font = pygame.font.Font(
        None,
        38
    )

    # Create player buttons
    you_button = pygame.Rect(
        120,
        300,
        180,
        70
    )

    ai_button = pygame.Rect(
        340,
        300,
        180,
        70
    )

    while True:

        screen.fill(
            (30, 30, 30)
        )

        # Draw title
        title = font.render(
            "Who Plays First?",
            True,
            WHITE_COLOR
        )

        screen.blit(
            title,
            title.get_rect(
                center=(WIDTH // 2, 190)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        # Highlight buttons
        if you_button.collidepoint(mouse_pos):
            you_color = (60, 160, 100)
        else:
            you_color = (40, 120, 75)

        if ai_button.collidepoint(mouse_pos):
            ai_button_color = (80, 130, 190)
        else:
            ai_button_color = (60, 100, 150)

        # Draw buttons
        pygame.draw.rect(
            screen,
            you_color,
            you_button,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            ai_button_color,
            ai_button,
            border_radius=10
        )

        # Create button text
        you_text = button_font.render(
            "YOU",
            True,
            WHITE_COLOR
        )

        ai_text = button_font.render(
            "AI",
            True,
            WHITE_COLOR
        )

        # Display button text
        screen.blit(
            you_text,
            you_text.get_rect(
                center=you_button.center
            )
        )

        screen.blit(
            ai_text,
            ai_text.get_rect(
                center=ai_button.center
            )
        )

        pygame.display.update()

        # Handle selection
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if you_button.collidepoint(
                    event.pos
                ):

                    return human_color

                if ai_button.collidepoint(
                    event.pos
                ):

                    return ai_color


# Draw the Reversi board
def draw_board(
    board,
    last_move=None,
    flipped_discs=None
):

    # Use an empty list if there are no flipped discs
    if flipped_discs is None:
        flipped_discs = []

    screen.fill(
        BACKGROUND_COLOR
    )

    # Draw board border
    pygame.draw.rect(
        screen,
        (90, 60, 30),
        (0, 0, 640, 640)
    )

    # Draw green board
    pygame.draw.rect(
        screen,
        BOARD_COLOR,
        (8, 8, 624, 624)
    )

    # Draw cells and discs
    for row in range(8):

        for col in range(8):

            x = 8 + col * CELL_SIZE
            y = 8 + row * CELL_SIZE

            # Draw board cell
            pygame.draw.rect(
                screen,
                BOARD_COLOR,
                (
                    x,
                    y,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

            # Draw grid line
            pygame.draw.rect(
                screen,
                GRID_COLOR,
                (
                    x,
                    y,
                    CELL_SIZE,
                    CELL_SIZE
                ),
                1
            )

            # Draw black disc
            if board[row][col] == BLACK:

                pygame.draw.circle(
                    screen,
                    (80, 80, 80),
                    (
                        x + CELL_SIZE // 2 + 3,
                        y + CELL_SIZE // 2 + 4
                    ),
                    CELL_SIZE // 2 - 9
                )

                pygame.draw.circle(
                    screen,
                    BLACK_COLOR,
                    (
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - 9
                )

            # Draw white disc
            elif board[row][col] == WHITE:

                pygame.draw.circle(
                    screen,
                    (120, 120, 120),
                    (
                        x + CELL_SIZE // 2 + 3,
                        y + CELL_SIZE // 2 + 4
                    ),
                    CELL_SIZE // 2 - 9
                )

                pygame.draw.circle(
                    screen,
                    WHITE_COLOR,
                    (
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - 9
                )

    # Highlight flipped discs
    for row, col in flipped_discs:

        x = 8 + col * CELL_SIZE
        y = 8 + row * CELL_SIZE

        pygame.draw.circle(
            screen,
            FLIP_COLOR,
            (
                x + CELL_SIZE // 2,
                y + CELL_SIZE // 2
            ),
            CELL_SIZE // 2 - 5,
            3
        )

    # Highlight the latest placed disc
    if last_move is not None:

        row, col = last_move

        x = 8 + col * CELL_SIZE
        y = 8 + row * CELL_SIZE

        pygame.draw.rect(
            screen,
            LAST_MOVE_COLOR,
            (
                x + 3,
                y + 3,
                CELL_SIZE - 6,
                CELL_SIZE - 6
            ),
            3
        )


# Show available moves
def draw_valid_moves(
    board,
    player
):

    moves = get_valid_moves(
        board,
        player
    )

    # Draw a yellow dot on every valid position
    for row, col in moves:

        x = (
            8
            + col * CELL_SIZE
            + CELL_SIZE // 2
        )

        y = (
            8
            + row * CELL_SIZE
            + CELL_SIZE // 2
        )

        pygame.draw.circle(
            screen,
            MOVE_COLOR,
            (x, y),
            8
        )

        pygame.draw.circle(
            screen,
            (80, 80, 30),
            (x, y),
            3
        )


# Draw a small player disc
def draw_player_disc(
    color,
    center,
    radius=18
):

    # Draw black player disc
    if color == BLACK:

        pygame.draw.circle(
            screen,
            (75, 75, 75),
            (
                center[0] + 2,
                center[1] + 3
            ),
            radius
        )

        pygame.draw.circle(
            screen,
            BLACK_COLOR,
            center,
            radius
        )

    # Draw white player disc
    else:

        pygame.draw.circle(
            screen,
            (110, 110, 110),
            (
                center[0] + 2,
                center[1] + 3
            ),
            radius
        )

        pygame.draw.circle(
            screen,
            WHITE_COLOR,
            center,
            radius
        )


# Draw score and game information
def draw_score(
    board,
    current_player,
    human_color,
    ai_color,
    ai_waiting,
    can_rewind
):

    # Count both colours
    black_score = count_disks(
        board,
        BLACK
    )

    white_score = count_disks(
        board,
        WHITE
    )

    # Draw bottom information bar
    pygame.draw.rect(
        screen,
        (35, 35, 35),
        (0, 640, 640, 120)
    )

    font = pygame.font.Font(
        None,
        25
    )

    small_font = pygame.font.Font(
        None,
        23
    )

    # Find human and AI scores
    if human_color == BLACK:

        human_score = black_score
        ai_score = white_score

    else:

        human_score = white_score
        ai_score = black_score

    # Draw player's disc
    draw_player_disc(
        human_color,
        (35, 665),
        16
    )

    # Draw AI's disc
    draw_player_disc(
        ai_color,
        (605, 665),
        16
    )

    # Show human score
    you_text = font.render(
        f"YOU  {human_score}",
        True,
        WHITE_COLOR
    )

    screen.blit(
        you_text,
        (60, 653)
    )

    # Show AI score
    ai_text = font.render(
        f"AI  {ai_score}",
        True,
        WHITE_COLOR
    )

    ai_text_rect = ai_text.get_rect(
        top=653,
        right=630
    )

    screen.blit(
        ai_text,
        ai_text_rect
    )

    # Show current turn
    if ai_waiting:

        turn_text = "AI is thinking..."

    elif current_player == human_color:

        turn_text = "YOUR TURN"

    else:

        turn_text = "AI TURN"

    turn = small_font.render(
        turn_text,
        True,
        MOVE_COLOR
    )

    screen.blit(
        turn,
        turn.get_rect(
            center=(WIDTH // 2, 665)
        )
    )

    # Create rewind button
    rewind_button = pygame.Rect(
        255,
        705,
        130,
        40
    )

    # Change rewind colour when available
    if (
        can_rewind
        and current_player == human_color
    ):

        rewind_color = (180, 120, 40)

    else:

        rewind_color = (80, 80, 80)

    pygame.draw.rect(
        screen,
        rewind_color,
        rewind_button,
        border_radius=7
    )

    rewind_text = small_font.render(
        "REWIND",
        True,
        WHITE_COLOR
    )

    screen.blit(
        rewind_text,
        rewind_text.get_rect(
            center=rewind_button.center
        )
    )

    return rewind_button


# Show final game result
def result_screen(game):

    font = pygame.font.Font(
        None,
        80
    )

    score_font = pygame.font.Font(
        None,
        40
    )

    button_font = pygame.font.Font(
        None,
        36
    )

    # Create result buttons
    play_again_button = pygame.Rect(
        150,
        470,
        160,
        65
    )

    exit_button = pygame.Rect(
        330,
        470,
        160,
        65
    )

    # Get final scores
    black_score, white_score = game.get_score()

    # Decide result
    if game.winner == game.human_color:

        result_text = "YOU WIN!"
        result_color = (40, 180, 80)

    elif game.winner == game.ai_color:

        result_text = "YOU LOSE!"
        result_color = (200, 60, 60)

    else:

        result_text = "DRAW!"
        result_color = (230, 170, 40)

    while True:

        screen.fill(
            (25, 25, 25)
        )

        # Show result
        result = font.render(
            result_text,
            True,
            result_color
        )

        screen.blit(
            result,
            result.get_rect(
                center=(WIDTH // 2, 170)
            )
        )

        # Show final score
        score_text = score_font.render(
            f"Black: {black_score}    White: {white_score}",
            True,
            WHITE_COLOR
        )

        screen.blit(
            score_text,
            score_text.get_rect(
                center=(WIDTH // 2, 270)
            )
        )

        # Show winning colour
        if game.winner == BLACK:

            winner_text = "Black wins!"

        elif game.winner == WHITE:

            winner_text = "White wins!"

        else:

            winner_text = "The game is a draw!"

        winner = score_font.render(
            winner_text,
            True,
            (220, 220, 220)
        )

        screen.blit(
            winner,
            winner.get_rect(
                center=(WIDTH // 2, 330)
            )
        )

        mouse_pos = pygame.mouse.get_pos()

        # Highlight result buttons
        if play_again_button.collidepoint(
            mouse_pos
        ):

            play_color = (60, 160, 100)

        else:

            play_color = (40, 120, 75)

        if exit_button.collidepoint(
            mouse_pos
        ):

            exit_color = (160, 70, 70)

        else:

            exit_color = (120, 50, 50)

        # Draw result buttons
        pygame.draw.rect(
            screen,
            play_color,
            play_again_button,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            exit_color,
            exit_button,
            border_radius=10
        )

        # Create button text
        play_text = button_font.render(
            "PLAY AGAIN",
            True,
            WHITE_COLOR
        )

        exit_text = button_font.render(
            "EXIT",
            True,
            WHITE_COLOR
        )

        # Display button text
        screen.blit(
            play_text,
            play_text.get_rect(
                center=play_again_button.center
            )
        )

        screen.blit(
            exit_text,
            exit_text.get_rect(
                center=exit_button.center
            )
        )

        pygame.display.update()

        # Handle result buttons
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_again_button.collidepoint(
                    event.pos
                ):

                    return "again"

                if exit_button.collidepoint(
                    event.pos
                ):

                    pygame.quit()
                    sys.exit()


# Start a new game
while True:

    # Show opening menu
    opening_screen()

    # Choose human colour
    human_color = choose_colour()

    # Choose AI difficulty
    difficulty = choose_difficulty()

    # Set AI colour
    ai_color = (
        WHITE
        if human_color == BLACK
        else BLACK
    )

    # Choose who plays first
    first_player = choose_first_player(
        human_color,
        ai_color
    )

    # Create game object
    game = Game(
        human_color,
        first_player
    )

    # Create AI object
    ai = AI(
        game.ai_color,
        difficulty
    )

    # AI waiting status
    ai_waiting = False
    ai_wait_start = 0

    # Store latest move
    last_move = None

    running = True

    # Main game loop
    while running:

        # Draw board
        draw_board(
            game.board,
            last_move,
            game.last_flipped
        )

        # Show valid moves during human turn
        if (
            game.current_player == human_color
            and not game.game_over
        ):

            draw_valid_moves(
                game.board,
                human_color
            )

        # Draw score and rewind button
        rewind_button = draw_score(
            game.board,
            game.current_player,
            human_color,
            game.ai_color,
            ai_waiting,
            game.can_rewind
        )

        pygame.display.update()

        # Handle user input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Check rewind button
                if rewind_button.collidepoint(
                    event.pos
                ):

                    if (
                        game.can_rewind
                        and game.current_player
                        == human_color
                    ):

                        if game.rewind():

                            last_move = None

                            game.last_flipped = []

                            ai_waiting = False

                            continue

                # Handle human move
                if (
                    game.current_player
                    == human_color
                    and not game.game_over
                ):

                    x, y = event.pos

                    # Check if click is inside board
                    if y < 640:

                        col = x // CELL_SIZE
                        row = y // CELL_SIZE

                        # Check if selected position is valid
                        if (
                            (row, col)
                            in get_valid_moves(
                                game.board,
                                human_color
                            )
                        ):

                            # Save state before human move
                            game.save_human_state()

                            # Make human move
                            if game.make_move(
                                row,
                                col
                            ):

                                # Store latest move
                                last_move = (
                                    row,
                                    col
                                )

                                # Start AI thinking
                                if (
                                    game.current_player
                                    == game.ai_color
                                    and not game.game_over
                                ):

                                    ai_waiting = True

                                    ai_wait_start = (
                                        pygame.time.get_ticks()
                                    )

        # Handle AI turn
        if (
            game.current_player
            == game.ai_color
            and not game.game_over
        ):

            # Start AI waiting timer
            if not ai_waiting:

                ai_waiting = True

                ai_wait_start = (
                    pygame.time.get_ticks()
                )

            # Give a small delay before AI move
            if (
                pygame.time.get_ticks()
                - ai_wait_start
                >= 900
            ):

                # Ask AI to choose a move
                ai_move = ai.choose_move(
                    game.board
                )

                if ai_move is not None:

                    # Make AI move
                    game.make_move(
                        ai_move[0],
                        ai_move[1]
                    )

                    # Store AI move
                    last_move = ai_move

                ai_waiting = False

        # Show result when game ends
        if game.game_over:

            pygame.time.delay(700)

            result_screen(
                game
            )

            running = False


# Close Pygame
pygame.quit()
sys.exit()