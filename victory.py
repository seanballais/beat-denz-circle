import math
import time

import pyautogui


time.sleep(3)
size = pyautogui.size()
origin = (0, 81,)
width = size.width
height = size.height - origin[1]

center = ( width // 2 + origin[0], height // 2 + origin[1] )
radius = 300

for degrees in range(0, 721):
    degrees = degrees / 2
    radians = math.radians(degrees)
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    mousePos = (x + center[0], y + center[1],)
    pyautogui.click(*mousePos)
