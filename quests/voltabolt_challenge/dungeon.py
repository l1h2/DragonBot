import pyautogui

from player import Player
from utils import CombatMoves

from .entrance import start_quest


def voltabolt_challenge() -> None:
    """
    Executes the voltabolt challenge quest.
    """
    player_moves = [
        CombatMoves.EIGHT,
        CombatMoves.Z,
        CombatMoves.V,
        CombatMoves.C,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.V,
        CombatMoves.ONE,
        CombatMoves.FOUR,
        CombatMoves.THREE,
        CombatMoves.SIX,
    ]

    player = Player(player_moves, pet_moves)
    start_quest()

    player.go_to((740, 395), (234, 206, 166))
    pyautogui.click(880, 540)  # Confirm challenge

    player.go_to((1350, 640), (103, 102, 103))
    player.battle()
