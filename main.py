import random
import time

def print_board(board):
    """Print the current board state."""
    print("   |   |")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |")
    print("        ")
    print("        ")
    # wait a second:
    time.sleep(1)

def get_player_move(board):
    """Get the player's move."""
    valid_move = False
    while not valid_move:
        player_move = input("Enter your move (0-8): ")
        if player_move.isdigit() and int(player_move) in range(9) and board[int(player_move)] == " ":
            return int(player_move)
        else:
            print("Invalid move. Please try again.")

def get_computer_move(board):
    """Get the computer's move."""
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

def check_win(board, symbol):
    """Check if a player has won."""
    win_positions = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    )
    for win_position in win_positions:
        if all(board[i] == symbol for i in win_position):
            return True
    return False

def play_game(game_mode):
    """Play a game of Noughts and Crosses."""
    board = [" "] * 9
    symbols = ["X", "O"]
    player_symbol = symbols[0]
    computer_symbol = symbols[1]
    print_board(board)
    while True:
        # Are we playing human vs PC, or PC vs PC?
        if (game_mode == 1):
            # Player's move
            player_move = get_player_move(board)
        else:
            # Dumb PC
            player_move = get_computer_move(board)

        board[player_move] = player_symbol
        print_board(board)
        print("Player 1 chose position", player_move)
        time.sleep(1)
        if check_win(board, player_symbol):
            print("You win!")
            break
        if " " not in board:
            print("It's a tie!")
            break
        # Computer's move
        computer_move = get_computer_move(board)
        board[computer_move] = computer_symbol
        print("Player 2 chose position", computer_move)
        time.sleep(1)
        print_board(board)
        if check_win(board, computer_symbol):
            print("You lose!")
            break

def game_mode_choice():
    # Get user input for game mode
    game_mode = input("Choose game mode: 1) Play against the computer, 2) Watch the computer play against itself: ")
    return(game_mode)


if __name__ == '__main__':
    game_mode = game_mode_choice()
    play_game(game_mode)