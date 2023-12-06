import pyautogui
import time
from pynput.mouse import Listener
import json

screen_width, screen_height = pyautogui.size()
click_coordinates = []

click_occurred = False
def on_click(x, y, button, pressed):
    global click_occurred
    if pressed:
        print(f"Mouse clicked at (x={x}, y={y})")
        click_coordinates.append((x, y))
        click_occurred = True

def ListenForClick():
    with Listener(on_click=on_click) as listener:
        while not click_occurred:
            pass  # Do nothing until the first click occurs
        listener.stop()
        listener.join()

def RunCalibration():
    global click_occurred
    print("Calibration started.")
    time.sleep(0.5)
    print("First, search something with bing, like: asd.")
    time.sleep(0.5)

    print("Please click on the search bar and press enter.")
    ListenForClick()
    click_occurred = False

    print("Please click on the remove search X button in the search bar.")
    ListenForClick()
    click_occurred = False    

    print("Please press CTRL + SHIFT + I.")
    print("Please press CTRL + SHIFT + M.")

    print("Please click on the phone selector near the URL bar.")
    ListenForClick()
    click_occurred = False 

    print("Please select a phone (Iphone 14 pro Max reccomended).")
    ListenForClick()
    click_occurred = False 

    print("Please click in the search bar, type in something then press enter.")
    ListenForClick()
    click_occurred = False 

    print("Please click in the search bar.")
    ListenForClick()
    click_occurred = False

    print("Please click on the remove search X button.")
    ListenForClick()
    click_occurred = False 

    with open('positionData.json', 'w') as file:
        json.dump(click_coordinates, file)