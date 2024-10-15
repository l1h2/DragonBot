import time
from enum import Enum

import pyautogui

from .game_objects import RGB, Point2


class Actions(Enum):
    """
    A class containing constants for different bot actions.
    """

    COMBAT_TURN = "combat turn"
    DUNGEON_ENTRANCE = "dungeon entrance"
    MENU_SCREEN = "menu screen"
    NPC_DIALOGUE = "NPC dialogue"
    QUEST_COMPLETE = "quest complete"
    QUEST_COMPLETE_CONFIRMATION = "quest complete confirmation"
    QUEST_RESTART = "quest restart"
    REWARD_SCREEN = "reward screen"
    SCREEN_TRANSITION = "screen transition"
    PLAYER_MOVEMENT = "player movement"
    TRAVEL_MAP = "travel map"


def wait_for_timeout(
    coord: Point2, rgb: RGB, action: Actions | str, timeout: int = 5
) -> None:
    """
    Waits for a specific pixel color to appear on the screen at the given coordinates.

    Args:
        coord (tuple[int, int]): The (x, y) coordinates to check for the pixel color.
        rgb (tuple[int, int, int]): The RGB color value to wait for.
        action (Actions | str): The action being performed while waiting for the timeout.
        timeout (int, optional): The maximum time to wait in seconds. Defaults to 15.

    Raises:
        TimeoutError: If the specified pixel color does not appear within the timeout period.
    """
    if isinstance(action, Actions):
        action = action.value

    start_time = time.time()
    end_time = start_time + timeout
    while pyautogui.pixel(*coord) != rgb:
        if time.time() > end_time:
            raise TimeoutError(f"Timed out waiting for {action} at {time.time()}.")
