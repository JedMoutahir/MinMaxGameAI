import random

# Tic Tac Toe Board
board = [' ' for x in range(9)]

# Display the board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Check if the board is full
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# Check if a player has won
def is_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
        (board[3] == player and board[4] == player and board[5] == player) or \
        (board[6] == player and board[7] == player and board[8] == player) or \
        (board[0] == player and board[3] == player and board[6] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[0] == player and board[4] == player and board[8] == player) or \
        (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Get all the available moves
def get_available_moves(board):
    moves = []
    for i in range(9):
        if board[i] == ' ':
            moves.append(i)
    return moves

# Minimax algorithm
def minimax(board, depth, is_maximizing_player):
    if is_winner(board, 'O'):
        return {'score': 10-depth}
    elif is_winner(board, 'X'):
        return {'score': depth-10}
    elif is_board_full(board):
        return {'score': 0}

    if is_maximizing_player:
        best_move = {'index': None, 'score': -1000}
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth+1, False)
            board[move] = ' '
            score['index'] = move
            if score['score'] > best_move['score']:
                best_move = score
        return best_move
    else:
        best_move = {'index': None, 'score': 1000}
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth+1, True)
            board[move] = ' '
            score['index'] = move
            if score['score'] < best_move['score']:
                best_move = score
        return best_move

# Main function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    while not is_board_full(board):
        if not is_winner(board, 'O'):
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] == ' ':
                board[player_move] = 'X'
                print_board()
            else:
                print("That space is already taken!")
                continue
        else:
            print("Sorry, you lose!")
            break

        if not is_winner(board, 'X'):
            computer_move = minimax(board, 0, True)['index']
            board[computer_move] = 'O'
            print("Computer placed an 'O' in position", computer_move)
            print_board()
        else:
            print("Congratulations, you win!")
            break

    if is_board_full(board):
        print("It's a tie!")

play_game()