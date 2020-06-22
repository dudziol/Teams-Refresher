import pyautogui
import time

#Objective: Practice scripting and problem solving, python syntax - especially objects, git


#0 Check (continously) if the user did not move the pointer for at least 4 minutes


#1 Create range from rel pos of the pointer
#2 Find place outside range created in #1 which is available (not hovering over something) AND not in the lower right corner (notifications)
#3 Move the pointer to position established in #2
#4 Draw a square, click 5 times, -> #1. #2, #3 -> click 5 times

a = 120
width, height = pyautogui.size()

for i in range (a):

    time.sleep(240)
    pyautogui.moveTo(width - 100, 100, duration=0.5)

    for i in range (5):
        pyautogui.click()
        time.sleep(2)

    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.5)
        pyautogui.moveRel(0, 100, duration=0.5)
        pyautogui.moveRel(-100, 0, duration=0.5)
        pyautogui.moveRel(0, -100, duration=0.5)

    for i in range (5):
        pyautogui.click()
        time.sleep(2)

    pyautogui.moveTo(width - 100, height - 100, duration=0.5)