import random
import time

import pyautogui

from player import Player
from utils import CombatMoves, wait_for_timeout

from .entrance import start_quest


def haunted_castle() -> None:
    """
    Executes the haunted castle quest.
    """
    player_moves = [
        CombatMoves.C,
        CombatMoves.V,
        CombatMoves.Z,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.ONE,
        CombatMoves.FOUR,
        CombatMoves.THREE,
        CombatMoves.SIX,
    ]
    player = Player(player_moves, pet_moves)
    start_quest()
    navigate_castle(player)


def navigate_castle(player: Player) -> None:
    """
    Navigates the haunted castle dungeon.

    Args:
        player (Player): The player object.
    """
    pyautogui.click(x=935, y=520)  # Go up
    player.battle()
    pyautogui.click(x=935, y=520)  # Go up

    wait_for_timeout((970, 300), (57, 0, 0), "castle entrance")
    pyautogui.click(x=1400, y=500)  # Go right
    player.battle()
    pyautogui.click(x=1600, y=500)  # Go right

    wait_for_timeout((1600, 530), (57, 0, 0), "right hallway")
    pyautogui.click(x=1400, y=500)  # Go right
    player.battle()
    pyautogui.click(x=800, y=800)  # Go down

    player.wait_for_player_position((750, 745), (126, 134, 163))
    pyautogui.click(x=1600, y=800)  # Go right
    player.battle()
    pyautogui.click(x=1600, y=600)  # Go right

    wait_for_timeout((1500, 215), (57, 0, 0), "hallway end")
    pyautogui.click(x=375, y=800)  # Go down

    player.wait_for_player_position((395, 795), (133, 156, 169))
    pyautogui.click(x=1600, y=800)  # Go right

    player.wait_for_player_position((1480, 715), (126, 134, 163))
    pyautogui.click(x=1530, y=215)  # Go up
    player.battle()
    pyautogui.click(x=1450, y=130)  # Go up

    wait_for_timeout((445, 150), (57, 0, 0), "stairs")
    pyautogui.click(x=445, y=150)  # Go left
    player.battle()
    pyautogui.click(x=445, y=150)  # Go left
    player.battle()
    pyautogui.click(x=445, y=150)  # Go up

    wait_for_timeout((1400, 485), (69, 0, 0), "top of stairs")
    pyautogui.click(x=960, y=160)  # Go up
    player.battle()
    pyautogui.click(x=960, y=850)  # Go down

    wait_for_timeout((445, 150), (57, 0, 0), "stairs return")
    pyautogui.click(x=1425, y=820)  # Go down

    wait_for_timeout((1500, 215), (57, 0, 0), "hallway end return")
    pyautogui.click(x=1455, y=820)  # Go down

    player.wait_for_player_position((1446, 792), (133, 156, 169))
    pyautogui.click(x=310, y=825)  # Go left

    player.wait_for_player_position((440, 730), (126, 134, 163))
    pyautogui.click(x=280, y=540)  # Go up

    wait_for_timeout((1600, 530), (57, 0, 0), "right hallway return")
    pyautogui.click(x=1042, y=840)  # Go left

    player.wait_for_player_position((1060, 720), (126, 134, 163))
    pyautogui.click(x=290, y=620)  # Go left

    wait_for_timeout((970, 300), (57, 0, 0), "castle entrance return")
    pyautogui.click(x=970, y=300)  # Go up
    player.battle()
    pyautogui.click(x=970, y=300)  # Go up

    wait_for_timeout((960, 170), (72, 54, 46), "main hall")
    pyautogui.click(x=960, y=525)  # Go up
    time.sleep(random.uniform(5, 20))  # Heal
    pyautogui.click(x=1600, y=500)  # Go right
    player.battle()
    pyautogui.click(x=1600, y=500)  # Go right

    wait_for_timeout((1500, 500), (102, 0, 0), "servant quarters")
    pyautogui.click(x=1100, y=500)  # Go right
    player.battle()
    pyautogui.click(x=280, y=500)  # Go left

    wait_for_timeout((960, 170), (72, 54, 46), "main hall return")
    pyautogui.click(x=960, y=525)  # Go left
    time.sleep(random.uniform(5, 20))  # Heal
    pyautogui.click(x=960, y=250)  # Go up
    player.battle()
    pyautogui.click(x=960, y=250)  # Go up

    wait_for_timeout((960, 170), (75, 1, 1), "final room")
    pyautogui.click(x=960, y=250)  # Go up
    player.battle()
