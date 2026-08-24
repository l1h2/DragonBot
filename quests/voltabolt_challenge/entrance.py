import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


def start_quest() -> None:
    """
    Starts the swordhaven defense quest.
    """
    player = Player()
    player.check_screen((620, 380), (153, 153, 153), "initial")

    pyautogui.click(855, 545)  # Heal
    pyautogui.click(855, 360)  # Return
    pyautogui.click(855, 420)  # Quest
    wait_for_timeout((1570, 680), (53, 36, 26), Actions.DUNGEON_ENTRANCE)
