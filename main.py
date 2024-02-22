# Tetrabot by Daniel Xie
# Still being developed and improved!
# Works on the website tetr.io
# 1920 x 1080 resolution, fullscreen on Google Chrome
# Works best on Minimal Graphics Settings in tetr.io Settings
# Requires pynput/pip/PIL to be installed
# Warning - the program will directly control your keyboard & key inputs
# Use only in 40 Lines (with guest account) or Zen mode

import pynput
from pynput.keyboard import Key, Controller
from pynput import keyboard as kb
import checkQueue
import tryPlacement
import evaluateBoard
import placePiece
import time
import copy
def press_callback(key):
    if hasattr(key, 'char'):
        if key.char == "b" or key.char == "B":
            while True: 
                if (checkQueue.checkStart()):
                    break
            board = [[0 for c in range(24)] for r in range(10)]
            for i in range(0, 10):
                board[i][0] = 1
            curPiece = checkQueue.checkQueue()
            heldPiece = 0
            time.sleep(1)
            while True:
                nextPiece = checkQueue.checkQueue()
                bestScore = -100000.0
                bestPos = 0 
                bestRot = 0 
                hold = False
                for i in range (0, 10):
                    for j in range (0, 4):
                        b2 = copy.deepcopy(board)
                        score = evaluateBoard.boardScore(tryPlacement.place(b2, i, curPiece, j))
                        if (type(score) == int and score > bestScore):
                            bestPos = i
                            bestRot = j
                            bestScore = score
                            hold = False
                        if (heldPiece != 0):
                            b2 = copy.deepcopy(board)
                            score = evaluateBoard.boardScore(tryPlacement.place(b2, i, heldPiece, j))
                            if (type(score) == int and score > bestScore):
                                bestPos = i
                                bestRot = j
                                bestScore = score
                                hold = True
                if (bestScore < -90 and heldPiece == 0):
                    kb = Controller()
                    kb.press('c')
                    kb.release('c')
                    time.sleep(0.05)
                    heldPiece = curPiece
                    curPiece =  nextPiece
                    nextPiece = checkQueue.checkQueue()
                    bestScore = -100000.0
                    for i in range (0, 10):
                        for j in range (0, 4):
                            b2 = copy.deepcopy(board)
                            score = evaluateBoard.boardScore(tryPlacement.place(b2, i, curPiece, j))
                            if (type(score) == int and score > bestScore):
                                bestPos = i
                                bestRot = j
                                bestScore  = score
                                hold = False
                   
                if (hold == False): board = evaluateBoard.clearLines(tryPlacement.place(board, bestPos, curPiece, bestRot))
                else:
                    board = evaluateBoard.clearLines(tryPlacement.place(board, bestPos, heldPiece, bestRot))
                    heldPiece = curPiece

                placePiece.place(bestPos, bestRot, hold)
                curPiece = nextPiece
                time.sleep(0.07)
                 
l = kb.Listener(on_press=press_callback)
l.start()
l.join()