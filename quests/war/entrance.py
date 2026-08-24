import time

import keyboard
import pyautogui

from player import Player


def start_quest() -> None:
    """
    Starts the swordhaven defense quest.
    """
    player = Player()
    player.check_screen((1500, 500), (234, 206, 166), "initial")

    pyautogui.click(1220, 575)  # Waves
    keyboard.press("9")
    pyautogui.click(1275, 575)  # Chain waves
    pyautogui.click(1350, 680)  # Quest
    time.sleep(1)
