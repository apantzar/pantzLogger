#!/usr/bin/env python
import pynput.keyboard


# process to catch the key
def process_key_press(key):
    print(key)


keyboardListener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboardListener:
    keyboardListener.join()
