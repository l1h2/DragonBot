import keyboard
import pyautogui

from player import Player
from utils import CombatMoves, ExploreActions, wait_for_timeout

from .entrance import start_quest


def castle_valtrith() -> None:
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
    battle_rgb = (28, 28, 28)
    battle_xy = (1060, 230)
    player = Player(player_moves, pet_moves, battle_rgb=battle_rgb, battle_xy=battle_xy)
    start_quest()
    navigate_castle(player)


def navigate_castle(player: Player) -> None:
    """
    Navigates the castle valtrith dungeon.

    Args:
        player (Player): The player object.
    """
    player.go_right(False)
    player.battle()
    player.go_right(False)

    wait_for_timeout((750, 270), (84, 0, 0), "castle entrance")
    player.go_right(False)
    player.battle()
    player.go_right(False)

    wait_for_timeout((950, 750), (60, 48, 31), "first hallway")
    player.go_right(False)
    player.battle()
    player.go_right(False)

    wait_for_timeout((750, 280), (88, 0, 0), "pillar hallway")
    while not player.check_for_battle():
        keyboard.press(ExploreActions.JUMP.value)
        player.go_right(False)

    player.battle()
    player.go_right(False)

    wait_for_timeout((900, 800), (0, 0, 0), "broken hallway")
    player.go_right(False)
    while pyautogui.pixel(845, 715) == (0, 0, 0):
        pass
    keyboard.press(ExploreActions.JUMP.value)

    wait_for_timeout((1055, 300), (204, 204, 153), "last hallway")
    player.go_right(False)
    player.battle()
    player.go_right(False)

    wait_for_timeout((1400, 450), (8, 8, 8), "inner entrance")
    player.go_right(False)
    player.battle()
    player.go_right(False)

    wait_for_timeout((1355, 620), (152, 163, 163), "final room")
    player.go_right(False)
    player.battle()
