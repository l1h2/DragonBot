import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


def start_quest() -> None:
    """
    Starts the castle valtrith quest.
    """
    player = Player()
    player.check_screen((1000, 100), (0, 0, 225), "initial")

    pyautogui.click(x=990, y=400)  # NPC dialogue
    wait_for_timeout((1500, 740), (109, 75, 29), Actions.NPC_DIALOGUE)

    pyautogui.click(x=960, y=400)  # Join
    wait_for_timeout((300, 800), (48, 96, 47), Actions.DUNGEON_ENTRANCE)
