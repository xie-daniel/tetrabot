#I L J T S Z O
#1 2 3 4 5 6 7
def place(board, pos, piece, rot):
    down = 1
    placed = False
    if (piece == 1 and rot % 2 == 0 and pos <= 6): #horiz I
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][20-down] == 1 or board[pos+3][20-down] == 1):
                down -= 1
                placed = True
                for j in range (0, 4):
                    board[pos+j][20-down] = 1
    elif (piece == 1 and rot % 2 == 1): #vert I
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1):
                down -= 1
                placed = True
                for j in range (0, 4):
                    board[pos][20-down+j] = 1
    elif (piece == 2 and rot == 0 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+2][20-down] = 1
                board[pos+2][21-down] = 1
    elif (piece == 2 and rot == 1 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos][21-down] = 1
                board[pos][22-down] = 1
    elif (piece == 2 and rot == 2 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][21-down] == 1 or board[pos+2][21-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos+1][21-down] = 1
                board[pos+2][21-down] = 1
    elif (piece == 2 and rot == 3 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][18-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][19-down] = 1
                board[pos+1][18-down] = 1
    elif (piece == 3 and rot == 0 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos+1][20-down] = 1
                board[pos+2][20-down] = 1
    elif (piece == 3 and rot == 1 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][22-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos][22-down] = 1
                board[pos+1][22-down] = 1
    elif (piece == 3 and rot == 2 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][19-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+2][20-down] = 1
                board[pos+2][19-down] = 1
    elif (piece == 3 and rot == 3 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][21-down] = 1
                board[pos+1][22-down] = 1
    elif (piece == 4 and rot == 0 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][21-down] = 1
                board[pos+1][20-down] = 1
                board[pos+2][20-down] = 1
    elif (piece == 4 and rot == 1 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][21-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos][22-down] = 1
                board[pos+1][21-down] = 1
    elif (piece == 4 and rot == 2 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][19-down] == 1 or board[pos+2][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][19-down] = 1
                board[pos+1][20-down] = 1
                board[pos+2][20-down] = 1
    elif (piece == 4 and rot == 3 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][19-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][19-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][21-down] = 1
    elif (piece == 5 and rot % 2 == 0 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1 or board[pos+2][21-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][21-down] = 1
                board[pos+2][21-down] = 1
    elif (piece == 5 and rot % 2 == 1 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][19-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][19-down] = 1
    elif (piece == 6 and rot % 2 == 0 and pos <= 7):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][19-down] == 1 or board[pos+2][19-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][19-down] = 1
                board[pos+2][19-down] = 1
    elif (piece == 6 and rot % 2 == 1 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][21-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos+1][21-down] = 1
                board[pos+1][22-down] = 1
    elif (piece == 7 and pos <= 8):
        while (placed == False):
            down += 1
            if (board[pos][20-down] == 1 or board[pos+1][20-down] == 1):
                down -= 1
                placed = True
                board[pos][20-down] = 1
                board[pos][21-down] = 1
                board[pos+1][20-down] = 1
                board[pos+1][21-down] = 1
    else: return
    
    return board