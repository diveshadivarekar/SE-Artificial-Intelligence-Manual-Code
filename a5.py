import math

# Board cells: empty = ' ', player 'X', opponent 'O'
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[3*i], '|', board[3*i+1], '|', board[3*i+2])
        if i < 2:
            print('---------')

def is_winner(b, player):
    # Winning combinations in Tic-Tac-Toe
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b_,c in wins:
        if b[a] == b[b_] == b[c] == player:
            return True
    return False

def is_board_full(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    """
    Minimax recursive function:
    - is_maximizing: True if the current turn is maximizer (X), else minimizer (O).
    - Returns the best score from the perspective of the maximizer.
    """
    if is_winner(b, 'X'):
        return 10 - depth  # Maximizer wins
    if is_winner(b, 'O'):
        return depth - 10  # Minimizer wins
    if is_board_full(b):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'  # Try this move
                score = minimax(b, depth + 1, False)  # Recurse for minimizer
                b[i] = ' '  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'  # Try this move
                score = minimax(b, depth + 1, True)  # Recurse for maximizer
                b[i] = ' '  # Undo move
                best_score = min(score, best_score)
        return best_score

def best_move():
    """
    Find the best move for maximizer (X).
    """
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """
    Simple game loop: Human (O) vs AI (X using Minimax).
    """
    print("Board positions are numbered 0 to 8:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")
    print()

    while True:
        # AI move
        move = best_move()
        if move == -1:
            print("Game Over! It's a tie.")
            break
        board[move] = 'X'
        print("AI (X) plays move:", move)
        print_board()
        if is_winner(board, 'X'):
            print("AI (X) wins!")
            break
        if is_board_full(board):
            print("Game Over! It's a tie.")
            break

        # Human move
        while True:
            try:
                human_move = int(input("Enter your move (0-8): "))
                if 0 <= human_move <= 8 and board[human_move] == ' ':
                    board[human_move] = 'O'
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        print_board()
        if is_winner(board, 'O'):
            print("You win!")
            break
        if is_board_full(board):
            print("Game Over! It's a tie.")
            break

if __name__ == "__main__":
    play_game()
