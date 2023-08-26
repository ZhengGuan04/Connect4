import check

## A board is a (listof (listof Str))
## Requires:
##      The length of the outer list is 6.
##      The length of each inner list is 7.
##      Each string is '', 'Y', or 'R'.

msg_valid = "Valid"
msg_draw = "Draw"
msg_win = "Win"

board_row = 6
board_col = 7
Yellow = "Y"
Red = "R"
Four = 4
Total_disc = 42

def is_draw(board, disc, row, col) :
    '''
    Returns True if the given board and move is in a draw state

    is_draw: listof(listof Str) Str Nat Nat -> Bool
    requires: row between 0 and 5 inclusive
              col between 0 and 6 inclusive
              disc either 'Y' or 'R'
    '''
    total_Y = 0
    total_R = 0
    for l in board:
        total_Y += l.count(Yellow)
        total_R += l.count(Red)

    if total_Y == 21 and total_R == 21:
        return True
    else:
        return False
    
def move(board, disc, row, col, dir_row, dir_col):
    '''
    Returns the number of consecutive discs from the given row and col along dir_row and dir_col

    move: listof(listof Str) Str Nat Nat Nat Nat -> Nat
    requires: row between 0 and 5 inclusive
              col between 0 and 6 inclusive
              disc either 'Y' or 'R'
              dir_x and dir_y -1, 0, or 1
    '''
    counter = 0
    index_row = row + dir_row
    index_col = col + dir_col

    while ((index_row >= 0 and index_row < board_row) and 
           (index_col >= 0 and index_col < board_col)):
        disc2 = board[index_row][index_col]
        if disc2 != '' and disc2 == disc: #if it is not empty, and own disk
            counter = counter + 1 #keep moving and count
            index_row = index_row + dir_row
            index_col = index_col + dir_col
        else:
            return counter
    return counter

def is_win(board, disc, row, col):
    '''
    Returns True if the given board and move is in a winning state, a line of
    four of one's own discs is formed horizontally, vertically, or diagonally

    is_win: listof(listof Str) Str Nat Nat -> Bool
    requires: row between 0 and 5 inclusive
              col between 0 and 6 inclusive
              disc either 'Y' or 'R'
    '''

    # search to right 
    counter1 = move(board, disc, row, col, 0, 1)

    # search to left
    counter2 = move(board, disc, row, col, 0, -1)

    if counter1 + counter2 + 1 == Four: # winning
        return True
    
    # search up
    counter1 = move(board, disc, row, col, -1, 0)

    # search down 
    counter2 = move(board, disc, row, col, 1, 0)

    if counter1 + counter2 + 1 == Four: # winning
        return True
    
    # search to upper right 
    counter1 = move(board, disc, row, col, -1, 1)

    # search to down left 
    counter2 = move(board, disc, row, col, 1, -1)

    if counter1 + counter2 + 1 == Four: # winning
        return True

    # search to upper left 
    counter1 = move(board, disc, row, col, -1, -1)

    # search to down right 
    counter2 = move(board, disc, row, col, 1, 1)

    if counter1 + counter2 + 1 == Four: # winning
        return True
    
    return False

def connect4(board, disc, row, col):
    '''
    Returns string "Valid", "Draw" or "Win" based on the given board and next move (disc, row and col).
    The board is updated with the move.

    Effects: the board is mutated

    connect4: (listof (listof Str)) Str Nat Nat -> Str

    requires: row between 0 and 5 inclusive
              col between 0 and 6 inclusive
              disc either 'Y' or 'R'
            
    Examples:

    board = [[ '',  '',  '',  '',  '',  '',  ''],
             [ '',  '',  '',  '',  '',  '',  ''],
             [ '',  '',  '',  '',  '',  '',  ''],
             [ '', 'Y',  '',  '',  '',  '',  ''],
             [ '', 'Y',  '',  '',  '',  '',  ''],
             [ '', 'Y', 'R', 'R', 'R',  '',  '']]

    connect4(board, 'Y', 2, 1) => "Win"
    and board is changed to 

    [[ '',  '',  '',  '',  '',  '',  ''],
     [ '',  '',  '',  '',  '',  '',  ''],
     [ '', 'Y',  '',  '',  '',  '',  ''],
     [ '', 'Y',  '',  '',  '',  '',  ''],
     [ '', 'Y',  '',  '',  '',  '',  ''],
     [ '', 'Y', 'R', 'R', 'R',  '',  '']]

    board2 = [['Y', 'Y', 'Y',  '', 'Y', 'Y', 'Y'],
              ['R', 'R', 'R', 'Y', 'R', 'R', 'R'],
              ['Y', 'Y', 'R', 'R', 'R', 'Y', 'R'],
              ['R', 'R', 'Y', 'Y', 'R', 'R', 'Y'],
              ['Y', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
              ['Y', 'Y', 'R', 'R', 'Y', 'R', 'Y']]

    connect4(board2, 'R', 0, 3) => "Draw"
    and board2 is changed to 
    [['Y', 'Y', 'Y', 'R', 'Y', 'Y', 'Y'],
     ['R', 'R', 'R', 'Y', 'R', 'R', 'R'],
     ['Y', 'Y', 'R', 'R', 'R', 'Y', 'R'],
     ['R', 'R', 'Y', 'Y', 'R', 'R', 'Y'],
     ['Y', 'Y', 'R', 'R', 'Y', 'Y', 'R'],
     ['Y', 'Y', 'R', 'R', 'Y', 'R', 'Y']]
    '''
    board[row][col] = disc
    if is_win(board, disc, row, col):
        return msg_win
    elif is_draw(board, disc, row, col):
        return msg_draw
    else:
        return msg_valid
    
#Test empty board, first move
board1 = [[ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  '']]

board1_changed = [[ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '', 'Y',  '',  '',  '']]


check.expect("Empty Board, first valid name", connect4(board1, 'Y', 5, 3), "Valid")
check.expect("Empty Board, first valid move - board changed", board1, board1_changed)

#Test valid move
board2 = [[ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '', 'Y',  '',  '',  '',  '',  ''],
          [ '', 'Y',  '',  '',  '',  '',  ''],
          [ '', 'Y', 'R', 'R', 'R',  '',  '']]

board2_changed = [[ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '', 'Y',  '',  '',  '',  '',  ''],
                  [ '', 'Y',  '',  '',  '',  '',  ''],
                  [ '', 'Y', 'R', 'R', 'R', 'Y',  '']]

check.expect("valid move", connect4(board2, 'Y', 5, 5), "Valid")
check.expect("valid move - board2", board2, board2_changed)

#Test win horizontal
board3 = [[ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '', 'Y',  '',  '',  '',  '',  ''],
          [ '', 'Y',  '',  '',  '',  '',  ''],
          ['Y', 'Y', 'R', 'R', 'R',  '',  '']]

board3_changed = [[ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '', 'Y',  '',  '',  '',  '',  ''],
                  [ '', 'Y',  '',  '',  '',  '',  ''],
                  ['Y', 'Y', 'R', 'R', 'R', 'R',  '']]

check.expect("win horizontal", connect4(board3, 'R', 5, 5), "Win")
check.expect("win horizontal - board3 changed", board3, board3_changed)

#Test win diagonal
board4 = [[ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  ''],
          [ '', 'Y', 'Y', 'Y',  '',  '',  ''],
          [ '', 'Y', 'R', 'R', 'R',  '',  ''],
          ['Y', 'Y', 'R', 'R', 'R',  '',  '']]

board4_changed = [[ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '',  '',  '',  '',  ''],
                  [ '',  '',  '', 'Y',  '',  '',  ''],
                  [ '', 'Y', 'Y', 'Y',  '',  '',  ''],
                  [ '', 'Y', 'R', 'R', 'R',  '',  ''],
                  ['Y', 'Y', 'R', 'R', 'R',  '',  '']]

check.expect("win diagonal", connect4(board4, 'Y', 2, 3), "Win")
check.expect("win diagonal - board4 changed", board4, board4_changed)




