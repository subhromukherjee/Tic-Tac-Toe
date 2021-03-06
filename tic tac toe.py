#----Global Variable----

# game board
board=["-", "-", "-", 
       "-", "-", "-", 
       "-", "-", "-"]

game_still_going = True

# who won or tie
winner = None


# whose turn is it
current_player = "X"




def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Play a game of tic tac toe 
def play_game():
    #display initial board
    display_board()
    
    while game_still_going:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        # Flip to the other player
        flip_player()
    
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " WON !! ")
    elif winner == None:
        print("TIE!!")


def handle_turn(player):
    
    print(player + "'s turn")
    position = input("Choose a position from 1-9 : ")
    
    valid = False
    
    while not valid:
    
        while position not in ["1","2","3","4","5", "6", "7", "8", "9"]:
            position = input("Invalid position. Choose a position from 1-9: ")
        
        position = int(position) - 1
        
        if board[position] == "-":
            valid = True
        else:
            print("Oops!! Position already taken. Try again! ")
        
    board[position] = player

    display_board()
    
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    
    # setup global variables
    global winner
    
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner  = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    
    
    return

def check_rows():
    
    # setup global variables
    global game_still_going
    
    # Check if any of the rows has same has value at all places
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    # If any row has a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    # Return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    
    # setup global variables
    global game_still_going
    
    # Check if any of the columns has same has value at all places
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    # If any row has a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    # Return the winner X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    
    # setup global variables
    global game_still_going
    
    # Check if any of the columns has same has value at all places
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    
    # If any row has a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
    # Return the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    
    return

def check_if_tie():
    
    # setup global variables
    global game_still_going
    
    if "-" not in board:
        game_still_going = False
    
    return

def flip_player():
    
    # setup global variables
    global current_player
    
    # Flipping the player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return
    
    
play_game()
