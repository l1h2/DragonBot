import time

import pyautogui

from player import Player


def start_quest() -> None:
    """
    Starts the doomwood defense quest.
    """
    player = Player()
    player.check_screen((1145, 845), (255, 255, 255), "initial")

    pyautogui.click(x=430, y=100)  # Quest menu
    pyautogui.click(x=430, y=200)  # to battle
    time.sleep(1)
