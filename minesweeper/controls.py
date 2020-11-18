import pyautogui
import time
from minesweeper.models import Point

def switch_window():
    pyautogui.keyDown("alt")
    pyautogui.keyDown("tab")
    time.sleep(0.1)
    pyautogui.keyUp("tab")
    pyautogui.keyUp("alt")

def screenshot():
    return pyautogui.screenshot()

def mouse_click(point: Point):
    pyautogui.moveTo(*point)