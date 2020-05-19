###########################
# mindnightclicker        #
# by Fireflew Development #
###########################

# press ESC to exit the program

import time
import pynput
from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()

def click(x,y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    print('clicked at {0}'.format(
        mouse.position))

def keymapping(key): #just follow the form below with all the other keys
    if key.char == 'q':
        click(704,399) #player1
    if key.char == 'u':
        click(946,632) #propose
        time.sleep(0.1) #need to wait a little bit or else wont process click
        click(790,631) #accept

def on_press(key):
    print(mouse.position)
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        keymapping(key)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
