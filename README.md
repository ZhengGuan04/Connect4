# Connect4
project1(python)

Connect 4 is a two player game played on a six-row, seven-column vertically suspended grid where players alternate by dropping a yellow or red disc to the grid (the discs may vary in color as long as two different color discs are used). The discs fall straight down, occupying the lowest available space within the column. The object of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

When a game starts, yellow disc always play first. We are concerned about valid moves. A valid move is a move that:
1. places the disc to an empty spot.
2. complies with the law of gravity, that is, it should be the lowest available space within the column.
3. can not place the disc with the same color consecutively. For example, if a yellow disc was placed in the last move, a yellow disc can not be placed in the current move. Same rule applys to the red disc.

Write the function: connect4(board, disc, row, col)
that consumes a board of type Board (see the starter file below for the data definition which you may use in your documentation), a disc which is one of 'Y' or 'R' and two parameters row and col. row is a natural number between 0 and 5 inclusive, col is a natural number between 0 and 6 inclusive, which represents the location on the Board where we are trying to put a disc. It returns a string:

1. "Win" if the move results a "Win" state. A "Win" state is a state where a line of four of one's own discs is formed horizontally, vertically, or diagonally.
2. "Draw" if the move occupies the last empty place, but does not result a "Win" state.
3. "Valid" if the move results neither a "Win" nor a "Draw" state.

and mutates the board. The function only makes one move.

Sample:
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

 board2 = [['Y', 'Y', 'Y', '', 'Y', 'Y', 'Y'],
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

