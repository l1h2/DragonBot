import time

import keyboard
import pyautogui


def select_game_window() -> None:
    """
    Selects the game window by clicking on it.
    """
    pyautogui.click(x=1822, y=132)
    time.sleep(0.5)


def start_recording() -> None:
    """
    Starts recording by clicking on a specific screen and windows recording shortcut.
    """
    keyboard.press_and_release("windows + alt + r")


def stop_recording() -> None:
    """
    Stops recording by clicking on the button.
    """
    pyautogui.click(x=1822, y=132)
