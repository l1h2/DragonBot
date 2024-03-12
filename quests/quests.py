from dataclasses import dataclass
from typing import Callable

from utils import RGB, Actions, Point2, wait_for_timeout

from .braughlmurk_cape import braughlmurk_bindings, shadow_bones
from .castle_valtrith import castle_valtrith
from .haunted_castle import haunted_castle
from .hundred_room_dungeon import hundred_room_dungeon


@dataclass
class QuestParams:
    """
    ### A class representing the quest starting parameters.

    ### Attributes:
    - `function` (Callable): The function to be called to execute the quest.
    - `coord` (tuple[int, int]): The coordinates of the start screen pixel to check.
    - `rgb` (tuple[int, int, int]): The RGB color value of the start screen pixel to check.
    """

    function: Callable
    coord: Point2
    rgb: RGB


class Quests:
    """
    A class representing different quests in the game and their respective
    start screen coordinates and RGB values.
    """

    HAUNTED_CASTLE = QuestParams(haunted_castle, (560, 800), (137, 68, 1))
    SHADOW_BONES = QuestParams(shadow_bones, (1555, 830), (12, 10, 8))
    BRAUGHLMURK_BINDINGS = QuestParams(braughlmurk_bindings, (1555, 830), (12, 10, 8))
    HUNDRED_ROOM_DUNGEON = QuestParams(hundred_room_dungeon, (870, 35), (130, 164, 242))
    CASTLE_VALTRITH = QuestParams(castle_valtrith, (830, 200), (234, 210, 176))


class Quest:
    """
    Config for the quest to be performed by the bot.
    """

    def __init__(self, quest: QuestParams):
        self.quest_function = quest.function
        self.start_screen_coord = quest.coord
        self.start_screen_rgb = quest.rgb

    def start_quest(self) -> None:
        """
        Starts the quest by calling the quest_function.
        """
        self.quest_function()

    def wait_to_restart(self) -> None:
        """
        Waits for the quest to restart after done by checking the start
        screen coordinates for the start screen RGB value.
        """
        wait_for_timeout(
            self.start_screen_coord, self.start_screen_rgb, Actions.QUEST_RESTART
        )
