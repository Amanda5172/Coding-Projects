def CreateBoard():
    global board
    board=[]

    print("Enter 9 numbers at a time, with one space in between each number.")
    for i in range(9):
        j=[]
        a,b,c,d,e,f,g,h,i=input("Enter one row (9 numbers): ").split()
        j.append(int(a))
        j.append(int(b))
        j.append(int(c))
        j.append(int(d))
        j.append(int(e))
        j.append(int(f))
        j.append(int(g))
        j.append(int(h))
        j.append(int(i))
        board.append(j)


def DisplayBoard():
    for i in range(9):
        for j in range(9):
            print("{:2} ".format(board[i][j]), end="")
        print()

def Possible(row,column,number):
    global board
    for i in range(9):
        if board[row][i]==number:
            return False
    for i in range(9):
        if board[i][column]==number:
            return False
    x0=(column//3)*3 
    y0=(row//3)*3 
    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j]==number:
                return False
    return True

def Solve():
    global board
    for row in range(9): 
        for column in range(9): 
            if board[row][column]==0: 
                for number in range(1,10): 
                    if Possible(row,column,number): 
                        board[row][column]=number 
                        Solve() 
                        board[row][column]=0 #if stuck, erase the number

                return
    DisplayBoard()
    input("Other solutions: ")

CreateBoard()
Solve()
            

