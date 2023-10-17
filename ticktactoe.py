def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3))
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter your move (row col): ").split())

        if board[row][col] == ' ':
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    main()
