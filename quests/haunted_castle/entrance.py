import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


def start_quest() -> None:
    """
    Starts the haunted castle quest.
    """
    player = Player()
    player.check_screen((560, 800), (137, 68, 1), "initial")

    pyautogui.click(x=770, y=560)  # NPC dialogue

    wait_for_timeout((1270, 200), (255, 255, 255), Actions.NPC_DIALOGUE)

    pyautogui.click(x=1270, y=500)  # Heal
    pyautogui.click(x=1270, y=315)  # Quest
    pyautogui.click(x=1270, y=425)  # Haunted Castle
    wait_for_timeout((360, 575), (35, 30, 24), Actions.DUNGEON_ENTRANCE)
