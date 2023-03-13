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

#display board
def DisplayBoard():
    for i in range(9):
        for j in range(9):
            print("{:2} ".format(board[i][j]), end="")
        print()

#checks if value is possible to be put at a spot
def Possible(row,column,number):
    global board
    #check row
    for i in range(9):
        if board[row][i]==number:
            return False
    #check column
    for i in range(9):
        if board[i][column]==number:
            return False
    #check the 3x3 square
    #floor division -> x={0,1,2}, x//3=0
    x0=(column//3)*3 #starting column
    y0=(row//3)*3 #starting row
    for i in range(3):
        for j in range(3):
            #checks through each element in the element array first, then moves on to next element array
            if board[y0+i][x0+j]==number:
                return False
    return True

def Solve():
    global board
    for row in range(9): #array element
        for column in range(9): #element
            if board[row][column]==0: #get the unfilled boxes
                for number in range(1,10): #1 to 9
                    if Possible(row,column,number): #returned True
                        board[row][column]=number #sub in that number
                        Solve() #
                        board[row][column]=0 #if stuck, erase the number

                return
    DisplayBoard()
    input("Other solutions: ")

Solve()

