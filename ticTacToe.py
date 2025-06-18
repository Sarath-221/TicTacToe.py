board=['-','-','-',
        '-','-','-',
        '-','-','-']
currentPlayer='x'
winner=None
gameRunning=True

def printBoard(board): 
    global currentPlayer
    print(board[0] +"|"+board[1] + "|"+board[2])
    print("-----")
    print(board[3] +"|"+board[4] + "|"+board[5])
    print("-----")
    print(board[6] +"|"+board[7] + "|"+board[8])
    
def playerInput(board):
    ins=int(input("Enter position between 0-9 : "))
    if (ins>0 and ins<=9) and board[ins-1]=="-":
        board[ins-1]=currentPlayer
    else :
        print("Something! went Wrong plz try again....")
        
def checkRows(board):
    global winner
    if board[0]==board[1]==board[2] and board[2]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[5]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[8]!="-":
        winner=board[6]
        return True
        
def checkColunmns(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner=board[0]
        return True
        
    elif board[0+1]==board[3+1]==board[6+1] and board[0+1]!='-':
        winner=board[0+1]
        return True
    elif board[0+1+1]==board[3+1+1]==board[6+1+1] and board[0+1+1]!='-':
        winner=board[0+1]
        return True

def checkDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!='-':
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!='-':
        winner=board[2]
        return True
        
def checkTie(board):
    global gameRunning
    if '-' not in board:
        printBoard(board)
        print("Its!Tie...")
        gameRunning=False

def checkWin():
    global winner
    if checkRows(board) or checkColunmns(board) or checkDiagonal(board):
        print(f"The Winner is {winner}")
        gamerunning=False
        

def switchPlayer():
    global currentPlayer
    if currentPlayer=='x':
        currentPlayer='o'
    else :
        currentPlayer='x'
        
        
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()