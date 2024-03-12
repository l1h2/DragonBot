import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


def start_quest() -> None:
    """
    Starts the supply grab quest.
    """
    player = Player()
    player.check_screen((560, 485), (34, 0, 43), "initial")

    pyautogui.click(x=1100, y=740)  # Heal
    pyautogui.click(x=1500, y=500)  # Supply Grab
    wait_for_timeout((370, 810), (217, 69, 43), Actions.DUNGEON_ENTRANCE)
