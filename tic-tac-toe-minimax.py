'''
This is a simple tic tac toe game that utilizes the algorithm "Minimax" in order to find the optimum move without explecetly programming the moves
the computer always takes the x and the player is left with o.
it is impossible to win against the computer, only a Tie or a loss can be achieved.
there is a huge room for improving the code in terms of speed and efficiency, but I think for a game this simple clarity is more important than efficiency.

    Created by: Omar alelwani
'''

from copy import deepcopy   

def print_board():  # - Used to print the main board
    for i, value in enumerate(the_board, 1):
        print(value, end = '  ')
        if i%3 == 0: print()

def h_move():   # - allowing the human player(o) to play his/her turn
    c = int(input('enter a non taken number between 1 - 9: '))
    if c == the_board[c-1]:
        the_board[c-1] = current_player

def c_move():   # - allowing the computer(x) to play its turn
    c = minimax(the_board, depth(the_board), True)
    c = c[1]
    the_board[c-1] = current_player

def play():     # - choosing between two function to call based on the turn of the game
    global current_player
    if turn%2 == 0:
        current_player = 'o'
        h_move()
    else:
        current_player = 'x'
        c_move()

def return_winning(b, player):      # - returning true if one of the players has won, otherwise returning false
    if (b[0] == player and b[1] == player and b[2] == player)or\
    (b[3] == player and b[4] == player and b[5] == player)or\
    (b[6] == player and b[7] == player and b[8] == player)or\
    (b[0] == player and b[3] == player and b[6] == player)or\
    (b[1] == player and b[4] == player and b[7] == player)or\
    (b[2] == player and b[5] == player and b[8] == player)or\
    (b[0] == player and b[4] == player and b[8] == player)or\
    (b[2] == player and b[4] == player and b[6] == player):
        return True
    else: return False
    
def return_empty_values(b):     # - return a list of non taked values
    return [x for x in b if isinstance(x, int)]

def is_terminal(b):     # - returns true if a winning comabnation is reached
    w_c = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]]:   return True
    
def depth(b):   # - return the number of non taked values in a board
    d = 0
    for i in b:
        if isinstance(i, int): d += 1
    return d

def evaluate(b):    # - assigning values to boards based on the faviorability of player x
    w_c = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for c in w_c:
        if b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'x':   return [20-depth(b), -1]
        elif b[c[0]] == b[c[1]] and b[c[1]] == b[c[2]] and b[c[2]] == 'o':   return [-10+depth(b), -1]
    return [10-depth(b), -1]

def moves_boards(b, player = 'x'): # returns a list that has pairs of the moves taken and the lists resulted from taking those moves for example:  [ [1,['x',2,3,4,5,6,7,8,9,]], [1,[1,'x',3,4,5,6,7,8,9,]], ... ]
    available_values =  [x for x in b if isinstance(x, int)]
    possible_boards = []
    output = []
    for i in available_values:
        c = deepcopy(b)
        c[i-1] = player
        output.append([i,c])
    return output

def minimax(b, depth_of_the_board, max_player):     # - the minimax algorithm that searches the game space and returns the best move possible
    if (depth(b) == 0) or (is_terminal(b) == True):
        return evaluate(b)

    if max_player:
        max_eval, best_move = float("-inf"), -1
        for move, child in moves_boards(b):
            ev = minimax(child, depth_of_the_board-1, False)[0]
            max_eval = max(ev, max_eval)
            if ev == max_eval:  best_move = move
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move, child in moves_boards(b, 'o'):
            ev = minimax(child, depth_of_the_board-1, True)[0]
            min_eval = min(ev, min_eval)
        return min_eval, -1

the_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = 'o'

"The Game loop"

print("Welcome to this game i hope u enjoy it, please wait a bit for the computer to think")
for turn in range(len([x for x in the_board if isinstance(x, str)])+1,10):
    play()
    print_board()
    if return_winning(the_board, current_player)== True:
        print('player {} has won the match'.format(current_player))
        break
    print('--------------------this is the computer turn----------------------')
if return_winning(the_board, current_player) != True: print('it is a Tie')    
