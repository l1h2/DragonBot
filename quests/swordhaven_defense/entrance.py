import time

import pyautogui

from player import Player


def start_quest() -> None:
    """
    Starts the swordhaven defense quest.
    """
    player = Player()
    player.check_screen((1500, 800), (149, 96, 28), "initial")

    pyautogui.click(x=430, y=100)  # Quest menu
    pyautogui.click(x=430, y=135)  # to battle
    time.sleep(1)
