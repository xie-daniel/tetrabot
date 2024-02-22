import copy
def boardScore(board):
    
    if (type(board) != list): return

    boardScore = 0
    cleared = 0
    delay = 0
    for i in range(1, 21+delay):
        filled = 0
        for j in range(0, 10):
            if (board[j][i-delay] == 1):
                filled += 1
        if (filled == 10):
            cleared += 1
            b3 = copy.deepcopy(board)
            for k in range(i-delay, 19):
                for l in range(0, 10):
                    board[l][k] = b3[l][k+1]
            for m in range(0, 10):
                board[m][20] = 0
            delay+=1
    height = [0]*10
    averageHeight = 0
    for i in range(0, 10):
        for j in range (0, 24):
            if (board[i][j] == 0):
                height[i] = j
                averageHeight += j
                break
    averageHeight //= 10
    well = 0
    for i in range(0, 10):
            #boardScore -= abs(height[i]-height[i-1])
            boardScore -= abs(averageHeight - height[i])
            if (abs(averageHeight - height[i]) > well): well = abs(averageHeight - height[i])
            if (i >= 1): boardScore -= abs(height[i] - height[i-1])
    if (cleared == 4):
        boardScore += 500
    elif (cleared != 0):
        boardScore -= 10
    for i in range(0, 10):
        for j in range(1, 20):
            if (board[i][j] == 1 and board[i][j-1] == 0):
                boardScore -= 100
    #print(boardScore)
    return boardScore

def clearLines(board):
    delay = 0
    for i in range(1, 21+delay):
        filled = 0
        for j in range(0, 10):
            if (board[j][i-delay] == 1):
                filled += 1
        if (filled == 10):
            b3 = copy.deepcopy(board)
            for k in range(i-delay, 19):
                for l in range(0, 10):
                    board[l][k] = b3[l][k+1]
            for m in range(0, 10):
                board[m][20] = 0
            delay+=1
    return board