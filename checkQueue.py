import pynput
from PIL import Image
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
from pynput import keyboard as kb
import time
queue = []
#I L J T S Z O
#1 2 3 4 5 6 7
def checkQueue():
    scr = ImageGrab.grab().load()
    color = scr[1240,300]
    #143, 191, 62 green; 195, 64, 70 red; 192, 169, 74 yel
    #175, 75, 165 pink; 92, 75, 174 blue; 193, 112, 63 orange;
    #82, 198, 157 I piece
    if (color == (143, 192, 62)): return 5 #queue.append(5) #gr S
    elif (color == (196, 64, 71)): return 6 #queue.append(6) #red Z
    elif (color == (197, 175, 83)): return 7 #queue.append(7) #yel O
    elif (color == (176, 75, 166)): return 4 #queue.append(4) #pink T
    elif (color == (93, 75, 175)): return 3 #queue.append(3) #blue J
    elif (color == (194, 113, 63)): return 2 #queue.append(2) #orange L
    elif (color == (87, 200, 161)): return 1 #queue.append(1) #lbl I
    
    #if (color[0] > 135 and color[0] < 145 and color[1] > 185 and color[1] < 195 and color[2] > 60 and color[2] < 68): return 5 #queue.append(5) #gr S
    #elif (color[0] > 190 and color[0] < 200 and color[1] > 62 and color[1] < 68 and color[2] > 64 and color[2] < 75): return 6 #queue.append(6) #red Z
    #elif (color[0] > 180 and color[0] < 196 and color[1] > 160 and color[1] < 178 and color[2] > 60 and color[2] < 80): return 7 #queue.append(7) #yel O
    #elif (color[0] > 170 and color[0] < 180 and color[1] > 70 and color[1] < 80 and color[2] > 160 and color[2] < 170): return 4 #queue.append(4) #pink T
    #elif (color[0] > 90 and color[0] < 95 and color[1] > 70 and color[1] < 80 and color[2] > 170 and color[2] < 1800): return 3 #queue.append(3) #blue J
    #elif (color[0] > 190 and color[0] < 1196 and color[1] > 108 and color[1] < 117 and color[2] > 60 and color[2] < 68): return 2 #queue.append(2) #orange L
    #elif (color[0] > 78 and color[0] < 86 and color[1] > 190 and color[1] < 202 and color[2] > 150 and color[2] < 162): return 1 #queue.append(1) #lbl I
    
    else:
        print("couldnt read")
        print(color)
    return
def checkStart():
    scr = ImageGrab.grab().load()
    color = scr[967,574]
    if (color[0] > 200):
        return True
    else: return False