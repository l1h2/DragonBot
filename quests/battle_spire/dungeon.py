import time

import pyautogui

from player import Player
from utils import Actions, CombatMoves, wait_for_timeout

from .entrance import start_quest


def battle_spire() -> None:
    """
    Executes the castle valtrith quest.
    """
    player_moves = [
        CombatMoves.ONE,
        CombatMoves.EIGHT,
        CombatMoves.Z,
        CombatMoves.X,
        CombatMoves.V,
        CombatMoves.C,
        CombatMoves.FIVE,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.ONE,
        CombatMoves.SIX,
        CombatMoves.FIVE,
    ]
    battle_rgb = (28, 28, 28)
    battle_xy = (1060, 230)
    player = Player(player_moves, pet_moves, battle_rgb=battle_rgb, battle_xy=battle_xy)
    start_quest()
    fight(player)


def fight(player: Player) -> None:
    """
    Executes the five rounds for the battle spire quest

    Args:
        player (Player): The player object.
    """
    finished_battles = False
    battle = 0

    while not finished_battles:
        pyautogui.click(x=450, y=680)  # Heal
        pyautogui.click(x=450, y=550)  # Join battle

        battle += 1
        player.battle()
        wait_for_timeout((300, 700), (48, 96, 47), Actions.DUNGEON_ENTRANCE)
        time.sleep(0.5) if battle < 5 else time.sleep(1)

        try:
            player.check_screen((1000, 600), (234, 206, 166), "rewards")
            finished_battles = True
        except ValueError:
            pass

    pyautogui.click(x=960, y=800)  # Finish quest
    wait_for_timeout((660, 630), (201, 208, 209), Actions.REWARD_SCREEN)
    pyautogui.click(x=960, y=800)  # Claim rewards
