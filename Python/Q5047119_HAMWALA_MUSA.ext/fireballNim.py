#MUSA HAMWAlA's ICA

#GAME VARIABLES
BOARD=[]
COUNTER = ' X '
END_POS = ' 0 '
BLANK_S = '   '
player = 2  #PLAYER 1 USES ROWS  #PLAYER 2 USES COLUMNS
previous_pos = 0
start_row = 0
start_col = 0
current_col = 0
current_row = 0
game_on = True
game_won = False
LINE = '|'
DASH = '-'
one_roll = 0
two_roll = 0
import time
import random
player_one_points = 0
player_two_points = 0
DICE = 'Rolling Dice...'
move = 0
TITLE = ('''                            Welcome to FIREBALL NIM
                                By. MUSA HAMWALA\n
''')
#>------------------------------------------
print(TITLE)
print('Roll the dice to Start:')
print()
player_one = input('Player 1, enter your name?    :').upper()
player_two = input('Player 2, enter your name?    :').upper()
print()
print('Highest Dice roll goes first!\n')
print(player_one, 'press "Enter" to roll the dice')
input()
print(DICE)
time.sleep(1)
print()
print(player_two, 'press "Enter" to roll the dice')
input()
print(DICE)
time.sleep(1)
print()

        #START OF MAIN OUTSIDE LOOP
#>------------------------------------------

def create_board():
    global BOARD
    for col in range(10):
        BOARD.append(['   ']*10)
    BOARD[start_row][start_col] = COUNTER
    BOARD[9][9] = END_POS

def player_roll():
    global one_roll
    global two_roll
    global player
    one_roll = (random.randrange(1, 7))
    print(player_one,': ', "rolls a ", one_roll)
    two_roll = (random.randrange(1, 7))
    print(player_two,': ', "rolls a ", two_roll)
    while one_roll == two_roll:
        print('Reroll\n')
        time.sleep(1.5)
        player_roll()

    else:
        if one_roll > two_roll:
            time.sleep(1)
            print(player_one,' goes first!!\n')
            player = 1
            return

        else:
            time.sleep(1.5)
            print(player_two,' goes first!!\n')
            player = 2
            return

def draw_board():
    global BOARD
    for row in range(10):
        print(DASH*41)
        for col in range(10):
            print(LINE + BOARD[row][col],end='')
        print(LINE)
    print(DASH*41)
    
        #START OF MAIN INSIDE LOOP
#>------------------------------------------

def get_move():
    global move
    valid = False
    while not valid:
        move = str(input('please enter your move: '))
        valid = validation(move)
    if player == 1:
        print("it's", player_one,"'s", 'turn\n')
    if player == 2:
        print("it's", player_two,"'s", 'turn\n')
    return move
    
def make_move(movement):
    global player, start_row, start_col, previous_pos, BLANK_S, current_row, current_col
    
    if player == 1:
        previous_pos = start_row
        end_row = start_row + int(movement)
        BOARD[end_row][start_col] = COUNTER
        start_row = end_row

##      remove previous row counter
        BOARD[previous_pos][start_col] = BLANK_S
        previous_pos = 0

        current_row += int(movement)
        
    else:
        previous_pos = start_col
        end_col = start_col + int(movement)
        BOARD[start_row][end_col] = COUNTER
        start_col = end_col

##      remove previous col counter
        BOARD[start_row][previous_pos] = BLANK_S
        previous_pos = 0

        current_col += int(movement)
    print('')
    
#THIS IS A FUCNTION FOR SWITCHING BETWEEN PLAYERS 1 and 2, player 1 always goes first.
def switching_player():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

def check_winner():
    global COUNTER, game_won, game_on
    game_won = False
    if COUNTER == BOARD[9][9]:
        game_on = False
        game_won = True
        if player == 1:
            print('Game over!: ', player_one, 'Wins\n')
        elif player == 2:
            print('Game over!: ', player_two, 'Wins\n')
        entry = input('Would you like to play again? (Y/N): ').upper()
        if entry == "Y":
            print('lets play again!!\n')
            adding_score()
            restart()
        elif entry == "N":
            print('Thanks for playing!!\n')
            adding_score()
            quit()
        elif entry != "n" or "y":
            print('Please enter "Y" for yes or "N" for no!')
            check_winner()

#this fucntion accumulates the total score(how many times player 1 + 2 have won)
def adding_score():
    global game_won, player, player_one_points, player_two_points
    player_one == 1
    player_two == 2
    if game_won:
        if player == 1:
            player_one_points += 1
        elif player == 2:
            player_two_points += 1
        print(player_one, ' has won ', player_one_points, ' time(s)')
        print(player_two, ' has won ', player_two_points, ' time(s)\n')
        
def rules():
    answer = input('\nwould you like to see the game rules?  Y/N:' ).upper()
    if answer == "Y":
        print("""
Heres the game rules!!

1.Players alternate turns and each player must move the fireball at least one space. 
2.The first player may move the fireball orthogonally straight down the board as far as desired,
up to the edge of the board, remaining in the same column of squares. The fireball must move at least one square. 
3.The second player must move the ball orthogonally rightwards as many squares as desired, up to the edge of the board.
Again, the fireball must remain on the same row during the second player’s rightwards move and move at least one space. 
4.Players alternate moving the fireball in this manner until it is moved onto the pit space. When the fireball is moved
on to the pit space, the game is over.  The player who moved the fireball on to the pit space is declared the winner! 
5.Players may only move the fireball horizontally or vertically (but not diagonally). 
\n""")
    elif answer == "N":
        print('\n')
        pass
    else:
        print('please enter Y/N!')
        rules()
        
def validation(move):
    global player
    if move.isdigit():
        move = int(move)
        if move in range(1,10):
            if player == 1:
                if move + current_row <= 9:
                    return True
                else:
                    print('error, move exceeds the board')
                    return False
            if player == 2:
                 if move + current_col <= 9:
                    return True
                 else:
                    print('error, move exceeds the board')
                    return False
        else:
            print('Error, Please enter a integer between 1-9\n')
            return False
    else:
        print('Error, please enter a number')
        return False

        
                #CALLING MAIN()
#>------------------------------------------

def main():
    global game_on
    game_on = True
    create_board()
    player_roll()
    draw_board()
    rules()
    while game_on:
        movement = get_move()
        print(movement)
        make_move(movement)
        draw_board()
        check_winner()
        switching_player()

                #CALLING RESTART()
#>------------------------------------------

def restart():
    global previous_pos, start_row, start_col, game_on, game_won, current_row, current_col 
    current_row = 0
    current_col = 0
    previous_pos = 0
    start_row = 0
    start_col = 0
    game_won = False
    BOARD[0][0] = COUNTER
    BOARD[9][9] = END_POS
    main()
    
main()
