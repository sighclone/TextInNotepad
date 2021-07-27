import pyautogui
import time
import subprocess

pyautogui.FAILSAFE = False

while True:
    taskMgr = pyautogui.getWindowsWithTitle("Task Manager")
    time.sleep(0.5)
    if taskMgr == []:
        pass
    else:
        print("open")
        subprocess.Popen("cancellor.bat")
