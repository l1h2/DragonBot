from dataclasses import dataclass
from enum import Enum

Point2 = tuple[int, int]
RGB = tuple[int, int, int]


@dataclass
class Directions:
    up: Point2 = (925, 40)
    down: Point2 = (960, 840)
    left: Point2 = (280, 630)
    right: Point2 = (1645, 615)


@dataclass
class DirectionsRGB:
    up: RGB = (0, 0, 0)
    down: RGB = (0, 0, 0)
    left: RGB = (0, 0, 0)
    right: RGB = (0, 0, 0)


class CombatMoves(Enum):
    HEALING_POTION = "n"
    WEAPON_SPECIAL = "R"
    Z = "z"
    X = "x"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    ATTACK = "space"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    ZERO = "0"
    C = "c"
    V = "v"
    TRINKET = "t"
    MANA_POTION = "m"
    PREVIOUS_FOE = "left"
    NEXT_FOE = "right"
    CYCLE_FOE = "tab"


class Menus(Enum):
    INVENTORY = "i"
    INVENTORY_CLICK = (840, 950)
    INVENTORY_CLOSE_CLICK = (670, 940)
    DRAGON_AMULET = "h"
    DRAGON_AMULET_CLICK = (960, 950)
    DRAGON_AMULET_CLOSE_CLICK = (960, 930)
    JOURNAL = "j"
    JOURNAL_CLICK = (1050, 950)
    JOURNAL_CLOSE_CLICK = (960, 970)
    OPTIONS = "esc"
    OPTIONS_CLICK = (960, 1020)
    OPTIONS_CLOSE_CLICK = (960, 970)
