import random

def display_board(board):
    print('\n'*100)
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    cond = True
    while cond:
        
        marker_player1 = input("Enter the 1st player's marker, i.e 'X' or 'O' : " ).upper()
        
        if marker_player1 == 'X':
            marker_player2 = 'O'
            cond = False
       
        elif marker_player1 == 'O':
            marker_player2 = 'X'
            cond = False
        
        else:
            print("Wrong Input. Please try again.!")
            continue
    
    return marker_player1 , marker_player2

def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or 
    (board[7]==mark and board[8]==mark and board[9]==mark) or 
    (board[1]==mark and board[5]==mark and board[9]==mark) or 
    (board[3]==mark and board[5]==mark and board[7]==mark) or 
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark))


def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    if board[position]==' ':
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1,10):
    
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) : '))
        
    return position

def replay():
    while True:
        replay_game = input("Do you want to play again? (Yes/No) : ").lower()
        if replay_game == 'yes':
            return True
            break
        elif replay_game == 'no':
            return False
            break
        else:
            continue

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = [' ']*10
    display_board(board)
    
    player1_marker , player2_marker = player_input()
    turn = choose_first()
    print(turn +" will go first.!")
    
    game_ready = input("Are you ready to play?(Yes/No) : ").lower()
    if game_ready == 'yes':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)

            if win_check(board,player1_marker):
                display_board(board)
                print("Congrats Player 1 has won the game.!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is drawn.!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)

            if win_check(board,player2_marker):
                display_board(board)
                print("Congrats Player 2 has won the game.!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is drawn.!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break            
