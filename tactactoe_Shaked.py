'''
Shaked Seller
11 February 2026 - 18 February 2026
This program is a classic game of tic-tac-toe on a 3x3 board.
The computer player is programmed with logic and tic tac toe strategies.
It also includes a scoreboard that keeps track of each player's wins.
'''
import random

'''
Validates and returns the human's turn 
'''
def human_turn():
    valid_nums = [0, 1, 2] # Valid range of numbers that the user can enter
    print("-------------------------")
    print("Place your symbol (X): [Note: for both rows and columns, 0 is the first and 2 is the last]")
    while True:
        try:
            row, col = input("Please enter the row and column numbers with a space in between: ").split()
            row = int(row)
            col = int(col)

            if row in valid_nums and col in valid_nums:
                return (row, col)
            else:
                print(" ! Please enter numbers in the valid range 0 - 2.")

        except ValueError:
            print(" ! Please enter a valid pair of numbers in the range 0 - 2.")


'''
Makes sure that the human's turn is not in an occupied spot
'''
def validate_human_turn(board):
    print("-------------------------")
    print("Your turn!")
    row, col = human_turn()
    while board[row][col] != ".":
        print("-------------------------")
        print("! Please try again and enter a different spot.")
        row, col = human_turn()

    return (row, col)

'''
Controls the computer's logic, including blocking and which
spots on the board it should prioritize.
'''
def computer_logic(board, PLAYER_SIGN, COMP_SIGN):
    # If the computer is unable to block, it will prioritize taking a corner, or a side, then the center
    corners = ((0, 0), (0, 2), (2, 0), (2, 2))
    sides = ((1, 0), (0, 1), (1, 2), (2, 1))
    # For row, column, and diagonal logic, it looks at the first two values according to the
    # respective tuple, then checks if their positions on the board have an "X", then, if the
    # third position is empty, it will block the player
    row_col_logic = ((0, 1, 2), (0, 2, 1), (1, 2, 0))
    diagonal_logic = (
        #Left top to right bottom
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (2, 2), (1, 1)),
        ((1, 1), (2, 2), (0, 0)),
        # Right top to left bottom
        ((0, 2), (1, 1), (2, 0)),
        ((0, 2), (2, 0), (1, 1)),
        ((1, 1), (2, 0), (0, 2))
    )

    # Checks to see if it can win a row
    for r in range(len(board)):
        for i in range(len(row_col_logic)):
            if board[r][row_col_logic[i][0]] == board[r][row_col_logic[i][1]] == COMP_SIGN and board[r][row_col_logic[i][2]] == ".":
                return (r, row_col_logic[i][2])

    # Checks to see if it can win a column
    for c in range(len(board[0])):
        for i in range(len(row_col_logic)):
            if board[row_col_logic[i][0]][c] == board[row_col_logic[i][1]][c] == COMP_SIGN and board[row_col_logic[i][2]][c] == ".":
                return (row_col_logic[i][2], c)

    # Checks to see if it can win a diagonal
    for i in range(len(diagonal_logic)):
        x, y, z = diagonal_logic[i]
        if board[x[0]][x[1]] == board[y[0]][y[1]] == COMP_SIGN and board[z[0]][z[1]] == ".":
            return (z[0], z[1])

    # Checks to see if it can block a row
    for r in range(len(board)):
        for i in range(len(row_col_logic)):
            if board[r][row_col_logic[i][0]] == board[r][row_col_logic[i][1]] == PLAYER_SIGN and board[r][row_col_logic[i][2]] == ".":
                return (r, row_col_logic[i][2])

    # Checks to see if it can block a column
    for c in range(len(board[0])):
        for i in range(len(row_col_logic)):
            if board[row_col_logic[i][0]][c] == board[row_col_logic[i][1]][c] == PLAYER_SIGN and board[row_col_logic[i][2]][c] == ".":
                return (row_col_logic[i][2], c)

    # Checks to see if it can block a diagonal
    for i in range(len(diagonal_logic)):
        x, y, z = diagonal_logic[i]
        if board[x[0]][x[1]] == board[y[0]][y[1]] == PLAYER_SIGN and board[z[0]][z[1]] == ".":
            return (z[0], z[1])

    # Prioritize placing an "O" in a corner
    for i in range(len(corners)):
        x, y = corners[i]
        if board[x][y] == ".":
            return (x, y)

    # If no corners are available, select a side
    for i in range(len(sides)):
        x, y = sides[i]
        if board[x][y] == ".":
            return (x, y)

    # If no corners or sides are available, select the center
    if board[1][1] == ".":
        return (1, 1)

    # As a backup, if all the blocks and logical moves are unavailable, choose a random spot
    rand_row = random.randint(0, 2)
    rand_col = random.randint(0, 2)
    while board[rand_row][rand_col] != ".":
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)

    return rand_row, rand_col

'''
The computer's turn, it calls to the computer logic above
'''
def computer_turn(board, PLAYER_SIGN, COMP_SIGN):
    print("---------------------")
    print("Computer's turn!")

    # Gets row and column from the computer logic function
    row, col = computer_logic(board, PLAYER_SIGN, COMP_SIGN)

    return (row, col)

'''
Makes a classic 3x3 board and fills each spot with a "." placeholder.
'''
def make_board(rows, cols):
    # Initialize the board
    board = []
    # Create rows and columns, with a placeholder of "." in each spot
    for r in range(rows):
        row_list = []
        for c in range(cols):
            row_list.append(".")
        board.append(row_list)

    return board

'''
Displays the current tic tac toe board.
'''
def print_board(board):
    # Prints the board with a neat border
    print("*------*")
    for r in range(len(board)):
        for c in range(len(board[0])):
            print(board[r][c], end = " ")
        print()
    print("*------*")

'''
Checks to see if either the computer or the player won
'''
def check_for_wins(board, symbol):
    # Check the rows for a win
    for r in range(len(board)):
        if board[r][0] == board[r][1] == board[r][2] == symbol:
            return True

    # Check the columns for a win
    for c in range(len(board[0])):
        if board[0][c] == board[1][c] == board[2][c] == symbol:
            return True

    # Check the diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True

    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    return False

'''
If all the spots have been occupied and no win was detected
'''
def check_for_tie(board):
    all_values = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            all_values.append(board[r][c])

    if "." not in all_values:
        return True

    return False

'''
Displays the current number of wins for each player, as well as the number of ties
'''
def display_stats(player_win_count, computer_win_count, tie_count):
    print()
    print(f"Your wins: {player_win_count}")
    print(f"Computer's wins: {computer_win_count}")
    print(f"Ties: {tie_count}")

def main():
    # Initialize the rows, win count for both players, tie count, X and O, and "play again"
    rows = 3
    cols = 3

    player_win_count = 0
    computer_win_count = 0
    tie_count = 0

    PLAYER_SIGN = "X"
    COMP_SIGN = "O"

    play_again = 'y'

    # Welcome message
    print("Welcome to Tic-tac-toe.")
    print(f"You are {PLAYER_SIGN}, and the computer is {COMP_SIGN}.")

    # Runs as long as the player wants to play again
    while play_again.lower() == 'y':
        board = make_board(rows, cols)
        player_win_check = False
        computer_win_check = False
        tie_check = False
        # Runs as long as no one won
        while not player_win_check and not computer_win_check and not tie_check:
            # Display the board each turn
            print_board(board)

            # Human's turn
            player_row, player_col = validate_human_turn(board) # Get the row and column
            board[player_row][player_col] = PLAYER_SIGN # Assign the player's chosen row and column to the board
            player_win_check = check_for_wins(board, PLAYER_SIGN) # Check for wins
            tie_check = check_for_tie(board) # Check for ties
            if player_win_check:
                player_win_count += 1
                print("-------------")
                print("You won!")
                print_board(board)
                break
            if tie_check:
                tie_count += 1
                print("-------------")
                print("Tie! No one wins.")
                print_board(board)
                break

            # Computer's turn
            comp_row, comp_col = computer_turn(board, PLAYER_SIGN, COMP_SIGN)
            board[comp_row][comp_col] =  COMP_SIGN
            print("The Computer has placed an O!")
            computer_win_check = check_for_wins(board, COMP_SIGN)
            tie_check = check_for_tie(board)
            if computer_win_check:
                computer_win_count += 1
                print("-------------")
                print("The Computer won!")
                print_board(board)
                break
            if tie_check:
                tie_count += 1
                print("-------------")
                print("Tie! No one wins.")
                print_board(board)
                break

        print("-------------")
        print("Current scoreboard stats:")
        display_stats(player_win_count, computer_win_count, tie_count)
        print("-------------")
        play_again = input("Play again? (y = yes/n = no): ")
    '''
    End message, and prints the final stats
    '''
    print("-------------")
    print("Thank you for playing!")
    print("-------------")
    print("Your final stats:")
    display_stats(player_win_count, computer_win_count, tie_count)
    print("-------------")

if __name__ == '__main__':
    main()
