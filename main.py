import pyautogui as pag
import random
import time

try:
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, duration=0.5)  # Move the mouse to the random position
        time.sleep(2)  # Wait for 2 seconds before the next movement

except KeyboardInterrupt:
    print("Mouse movement stopped.")
