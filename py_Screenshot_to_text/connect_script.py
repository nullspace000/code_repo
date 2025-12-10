import pyautogui
import time
from pynput.keyboard import Key, Controller

print("The window with the test should be on the next alt+tab")
input("Press ENTER when the condition is met: ")

keyboard = Controller()

# Press and hold keys
keyboard.press(Key.alt)
keyboard.press(Key.tab)

time.sleep(1)  # how long to hold

# Release keys
keyboard.release(Key.alt)
keyboard.release(Key.tab)

time.sleep(1)  # wait 1 seccond for alt tab ui to disapear

# define the region: (left, top, width, height)
region = (0, 140, 1920, 820)
screenshot = pyautogui.screenshot(region=region)

screenshot.save("question.png")
#This automatically snips the selected area without opening Snipping Tool.

