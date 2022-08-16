import subprocess

import pygetwindow
import time
import mouse
from pyautogui import press, typewrite

from typing import Final

import Keyboard
import Mouse


def wait(seconds=0.3):
    time.sleep(seconds)


def write(text):
    for letter in text:
        typewrite(letter)
        wait(0.02)


def open_mail():
    path: Final = 'mail.google.com/mail'

    chrome = open_chrome()
    if not chrome.isMaximized:
        chrome.maximize()
    mouse.drag(40, 10, 40, 100, absolute=True, duration=0.5)
    wait()
    mouse.drag(0, 0, -50, 0, absolute=False, duration=0.5)
    wait()
    mouse.click(Mouse.LEFT_CLICK)
    write(path)
    press(Keyboard.ENTER)


def open_chrome():
    path: Final = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    subprocess.Popen(path)
    wait()
    return pygetwindow.getActiveWindow()


def main():
    open_mail()


if __name__ == '__main__':
    main()
