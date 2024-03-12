from enum import Enum

import pyautogui

from player import Player
from utils import Actions, wait_for_timeout


class Quest(Enum):
    SHADOW_BONES = "SHADOW_BONES"
    BRAUGHLMURK_BINDINGS = "BRAUGHLMURK_BINDINGS"


def shadow_bones(player: Player) -> None:
    """
    Starts the shadow bones quest.

    Args:
        player (Player): The player object to use for the quest.
    """
    pyautogui.click(x=960, y=780)  # Go down
    player.wait_for_player_position((1025, 715), (126, 134, 163))

    player.go_left()
    player.go_left()
    player.go_down()
    player.go_right(False)

    player.wait_for_player_position((1625, 210), (217, 69, 43))
    pyautogui.click(x=1625, y=210)  # Enter sewer
    wait_for_timeout((1315, 660), (36, 64, 84), Actions.DUNGEON_ENTRANCE)


def braughlmurk_bindings(player: Player) -> None:
    """
    Starts the braughlmurk bindings quest.

    Args:
        player (Player): The player object to use for the quest.
    """
    player.go_right()
    player.go_right()
    player.go_up()
    player.go_right()
    player.go_right(False)

    player.wait_for_player_position((1625, 210), (217, 69, 43))
    pyautogui.click(x=1625, y=210)  # Enter shipwreck
    wait_for_timeout((960, 650), (20, 42, 46), Actions.DUNGEON_ENTRANCE)


def start_quest(quest: Quest) -> None:
    """
    Starts a quest in braughlmurk cape.

    Args:
        quest (QuestParams): The quest to start.

    Raises:
        ValueError: If the quest is not valid.
    """
    player = Player()
    player.check_screen((575, 335), (38, 38, 51), "initial")
    player.menu_heal()

    if quest == Quest.SHADOW_BONES:
        shadow_bones(player)
    elif quest == Quest.BRAUGHLMURK_BINDINGS:
        braughlmurk_bindings(player)
    else:
        raise ValueError(f"Invalid quest: {quest}")
