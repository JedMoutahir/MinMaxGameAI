import numpy as np

# Constants
ROWS = 6
COLS = 7
PLAYER = 2
AI = 1

# Create the board
def create_board():
    board = np.zeros((ROWS, COLS))
    return board

# Drop a piece in a column
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if a move is valid
def is_valid_move(board, col):
    return board[ROWS-1][col] == 0

# Get the next open row for a piece
def get_next_open_row(board, col):
    for r in range(ROWS):
        if board[r][col] == 0:
            return r

# Display the board
def print_board(board):
    print(np.flip(board, 0))

# Check if the board is full
def is_board_full(board):
    return np.all(board != 0)

# Check if a player has won
def is_winner(board, piece):
    # Check horizontal
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece :
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check diagonal positive slope
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check diagonal negative slope
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

    return False

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    max_depth = 7
    if is_winner(board, AI):
        return {'score': 100-depth}
    elif is_winner(board, PLAYER):
        return {'score': depth-100}
    elif is_board_full(board):
        return {'score': 0}
    elif depth == max_depth:
        return {'score': 0}

    if maximizing_player:
        best_move = {'index': None, 'score': -np.inf}
        for col in range(COLS):
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                board_copy = board.copy()
                drop_piece(board_copy, row, col, AI)
                score = minimax(board_copy, depth+1, False)
                score['index'] = col
                if score['score'] > best_move['score']:
                    best_move = score
        return best_move
    else:
        best_move = {'index': None, 'score': np.inf}
        for col in range(COLS):
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                board_copy = board.copy()
                drop_piece(board_copy, row, col, PLAYER)
                score = minimax(board_copy, depth+1, True)
                score['index'] = col
                if score['score'] < best_move['score']:
                    best_move = score
        return best_move

# Main game loop
def play_game():
    board = create_board()
    print_board(board)

    game_over = False
    turn = PLAYER

    while not game_over:
        if turn == PLAYER:
            col = int(input("Player 1, choose a column to drop your piece (0-6): "))
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER)
                print_board(board)
                if is_winner(board, PLAYER):
                    print("Congratulations, you win!")
                    game_over = True
                    break
                turn = AI
            else:
                print("That column is full!")
                continue
        else:
            print("AI is thinking...")
            col = minimax(board, 2, True)['index']
            if is_valid_move(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI)
                print_board(board)
                if is_winner(board, AI):
                    print("Sorry, you lose!")
                    game_over = True
                    break
                turn = PLAYER
            else:
                continue

        if is_board_full(board):
            print("It's a tie!")
            game_over = True
            break

play_game()