from enum import Enum

import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


class Quest(Enum):
    SHADOW_BONES = "SHADOW_BONES"
    BRAUGHLMURK_BINDINGS = "BRAUGHLMURK_BINDINGS"


def shadow_bones() -> None:
    """
    Starts the shadow bones quest.
    """
    pyautogui.click(x=875, y=90)  # Enter dungeon
    wait_for_timeout((1040, 700), (52, 48, 47), Actions.DUNGEON_ENTRANCE)


def braughlmurk_bindings() -> None:
    """
    Starts the braughlmurk bindings quest.
    """
    pyautogui.click(x=1100, y=190)  # Enter dungeon
    wait_for_timeout((1530, 500), (9, 9, 8), Actions.DUNGEON_ENTRANCE)


def start_quest(quest: Quest) -> None:
    """
    Starts a quest in braughlmurk cape.

    Args:
        quest (QuestParams): The quest to start.

    Raises:
        ValueError: If the quest is not valid.
    """
    player = Player()

    if quest == Quest.SHADOW_BONES:
        player.check_screen((900, 100), (50, 50, 54), "initial")
        shadow_bones()
    elif quest == Quest.BRAUGHLMURK_BINDINGS:
        player.check_screen((1300, 480), (9, 10, 10), "initial")
        braughlmurk_bindings()
    else:
        raise ValueError(f"Invalid quest: {quest}")
