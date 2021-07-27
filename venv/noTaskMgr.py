import pyautogui
import time
import subprocess

pyautogui.FAILSAFE = False

while True:
    taskMgr = pyautogui.getWindowsWithTitle("Task Manager")
    time.sleep(0.3)
    if taskMgr == []:
        pass
    else:
        print("open")
        shut = subprocess.Popen("cancellor.bat")
        break
shut.wait()
