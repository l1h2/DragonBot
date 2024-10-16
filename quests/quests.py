from dataclasses import dataclass
from typing import Callable

from utils import RGB, Actions, Point2, wait_for_timeout

from .battle_spire import battle_spire
from .braughlmurk_cape import braughlmurk_bindings, shadow_bones
from .castle_valtrith import castle_valtrith
from .crypt_of_the_lost_order import crypt_of_the_lost_order_dungeon
from .haunted_castle import haunted_castle
from .hundred_room_dungeon import hundred_room_dungeon
from .supply_grab import supply_grab
from .trick_or_treat import trick_or_treating


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
    SHADOW_BONES = QuestParams(shadow_bones, (900, 100), (50, 50, 54))
    BRAUGHLMURK_BINDINGS = QuestParams(braughlmurk_bindings, (1300, 480), (9, 10, 10))
    HUNDRED_ROOM_DUNGEON = QuestParams(hundred_room_dungeon, (870, 35), (130, 164, 242))
    CASTLE_VALTRITH = QuestParams(castle_valtrith, (830, 200), (234, 210, 176))
    SUPPLY_GRAB = QuestParams(supply_grab, (560, 485), (34, 0, 43))
    CRYPT_OF_THE_LOST_ORDER = QuestParams(
        crypt_of_the_lost_order_dungeon, (870, 35), (130, 164, 242)
    )
    BATTLE_SPIRE = QuestParams(battle_spire, (1000, 100), (0, 0, 225))
    TRICK_OR_TREAT = QuestParams(trick_or_treating, (600, 800), (159, 152, 95))


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
