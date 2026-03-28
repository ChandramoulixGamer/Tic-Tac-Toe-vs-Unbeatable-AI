import sys
import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Measurements
WIDTH = 500
HEIGHT = 500
BOARD_ROWS = 3
BOARD_COLS = 3
LINE_WIDTH = 5
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE vs AI')
screen.fill(BLACK)

# Game board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# Draw lines
def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


# Draw figures
def draw_figures(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen, color,
                    (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                    CIRCLE_RADIUS, CIRCLE_WIDTH
                )
            elif board[row][col] == 2:
                start1 = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4)
                end1 = (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
                start2 = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
                end2 = (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4)
                pygame.draw.line(screen, color, start1, end1, CROSS_WIDTH)
                pygame.draw.line(screen, color, start2, end2, CROSS_WIDTH)


def mark_squares(row, col, player):
    board[row][col] = player


def check_squares(row, col):
    return board[row][col] == 0


def is_board_full(check_board=board):
    return not np.any(check_board == 0)


def check_win(player, check_board=board):
    # Vertical
    for col in range(BOARD_COLS):
        if np.all(check_board[:, col] == player):
            return True
    # Horizontal
    for row in range(BOARD_ROWS):
        if np.all(check_board[row, :] == player):
            return True
    # Diagonals
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True
    return False


# Minimax algorithm
def minimax(minimax_board, depth, is_maximizing):
    if check_win(2, minimax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
        mark_squares(move[0], move[1], player=2)
        return True
    return False


def restart_game():
    screen.fill(BLACK)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


# Main game loop
draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE
            if check_squares(mouseY, mouseX):
                mark_squares(mouseY, mouseX, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_win(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over and is_board_full():
                    game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
                player = 1

    draw_figures()
    if game_over:
        if check_win(1):
            draw_lines(GREEN)
            draw_figures(GREEN)
        elif check_win(2):
            draw_lines(RED)
            draw_figures(RED)
        else:
            draw_lines(GRAY)
            draw_figures(GRAY)

    pygame.display.update()

