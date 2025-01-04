import random
def print_board(board):
    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")
def computer_move(board):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    move = random.choice(available_moves)
    board[move[0]][move[1]] = 'O'
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        computer_move(board)
        print_board(board)

        if check_winner(board, 'O'):
            print("Computer wins! Better luck next time.")
            break

        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()