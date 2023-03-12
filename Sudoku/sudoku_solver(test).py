#no user input, makes sure the code works

#board as 2D array
board = [[0,0,0,5,0,0,3,0,0],
         [0,7,0,0,3,2,0,0,5],
         [0,3,0,7,6,0,0,0,9],
         [0,0,0,4,0,7,0,0,8],
         [0,0,0,0,0,0,0,3,0],
         [2,5,0,0,0,0,9,0,7],
         [7,2,0,3,0,9,5,0,0],
         [8,9,0,2,0,0,0,0,0],
         [0,0,5,0,0,0,0,0,6]]
         
#display board as a sudoku grid - function
for i in range(9):
    for j in range(9):
        print("{:2} ".format(board[i][j]), end="")
    print()

#checking for possible values - function


#checking for 0

