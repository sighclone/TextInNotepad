import pyautogui
import time
import subprocess

pyautogui.FAILSAFE = False

while True:
    taskMgr = pyautogui.getWindowsWithTitle("Task Manager")
    subprocess.Popen("/cancellor.bat")
    time.sleep(0.5)
