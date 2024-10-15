import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


def start_quest() -> None:
    """
    Starts the castle valtrith quest.
    """
    player = Player()
    player.check_screen((830, 200), (234, 210, 176), "initial")

    pyautogui.click(x=1100, y=500)  # Heal
    pyautogui.click(x=1100, y=600)  # Castle Valtrith
    wait_for_timeout((520, 200), (255, 255, 255), Actions.DUNGEON_ENTRANCE)
