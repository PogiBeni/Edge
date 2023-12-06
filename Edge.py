import time
import pyautogui
import random
import json
import os
from Calibrator import RunCalibration

filename = 'positionData.json'

if os.path.exists(filename):
    print('Starting the script')
else:
    print('The position file does not exist.')
    print('Starting calibration.')
    RunCalibration()
    print('Starting the script')

def move_and_click(xPos, yPos):

    # Move the mouse to the calculated position and click
    pyautogui.moveTo(xPos, yPos, duration=0.3)
    pyautogui.click()

#Get data
with open('data.json', 'r') as file:
    data = json.load(file)

with open('positionData.json', 'r') as file:
        clickPositions = json.load(file)
#Shuffle data
random.shuffle(data)


desktopSearch = int(input("Enter the value for desktop searches(number): "))
mobileSearch = int(input("Enter the value for mobile searches(number): "))

for i in range(desktopSearch):
    move_and_click(clickPositions[0][0],clickPositions[0][1])

    pyautogui.typewrite(data[i])
    pyautogui.press('enter')

    wait_time = random.uniform(4, 7)
    time.sleep(wait_time)

    # Press delete on search
    #26.48,7.92
    move_and_click(clickPositions[1][0],clickPositions[1][1])

pyautogui.hotkey('ctrl', 'shift', 'i')
time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'm')
#telefon választo
#33.36, 5.97
move_and_click(clickPositions[2][0],clickPositions[2][1])
#mobil kiválasztása
#32.23, 17.22
move_and_click(clickPositions[3][0],clickPositions[3][1])
#random helper search
#34.34, 10.97
move_and_click(clickPositions[4][0],clickPositions[4][1])
pyautogui.typewrite("teszt")
pyautogui.press('enter')
time.sleep(0.5)

for i in range(desktopSearch +1, mobileSearch + desktopSearch +1):
    #31.09, 12.15
    move_and_click(clickPositions[5][0],clickPositions[5][1])

    pyautogui.typewrite(data[i])
    pyautogui.press('enter')

    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    #37.23, 12.15
    move_and_click(clickPositions[5][0],clickPositions[5][1])

    #Press delete on search
    #43.83, 12.15
    move_and_click(clickPositions[6][0],clickPositions[6][1])

print("Loop finished")
