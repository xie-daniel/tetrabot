import time
from pynput.keyboard import Key, Controller
def place(pos, rot, held):
    kb = Controller()
    if (held == True):
        kb.press('c')
        kb.release('c')
    time.sleep(0.04)
    for i in range (0, rot):
        kb.press(Key.up)
        kb.release(Key.up)
    
    for i in range(0, 6):
        kb.press(Key.left)
        kb.release(Key.left)
    time.sleep(0.04)
    for i in range (0, pos):
        kb.press(Key.right)
        kb.release(Key.right)
    kb.press(Key.space)
    kb.release(Key.space)