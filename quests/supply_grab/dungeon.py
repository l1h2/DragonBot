import pyautogui

from player import Player
from utils import CombatMoves, Directions

from .entrance import start_quest


def supply_grab() -> None:
    """
    Executes the castle valtrith quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.C,
        CombatMoves.X,
        CombatMoves.V,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.ONE,
        CombatMoves.FOUR,
        CombatMoves.THREE,
        CombatMoves.SIX,
        CombatMoves.FIVE,
    ]
    battle_rgb = (34, 53, 17)
    battle_xy = (1630, 730)
    player = Player(player_moves, pet_moves, battle_rgb=battle_rgb, battle_xy=battle_xy)
    start_quest()
    navigate_map(player)


def navigate_map(player: Player) -> None:
    """
    Traverses the map to get to the goal.

    Args:
        player (Player): The player object.
    """
    pyautogui.click(1515, 90)  # Go to the corner
    while boss_alive() or player.check_for_battle():
        player.battle()
        player.go_up(False)

    player.finish_quest(Directions.down, False)


def boss_alive() -> bool:
    """
    Checks if the boss is still alive.

    Returns:
        bool: True if the boss is still alive, False otherwise.
    """
    return pyautogui.pixel(945, 140) == (48, 37, 37)
