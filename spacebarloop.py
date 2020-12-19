import pyautogui
import keyboard

run = True

while run:
    pyautogui.hotkey('space')
    if keyboard.is_pressed('q'):
        run = False
  #  