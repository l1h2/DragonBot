from player import Player
from utils import CombatMoves, find_rgb_coordinates

from .entrance import start_quest

ENEMIES = {
    (255, 178, 13),
    (244, 244, 2),
    (29, 23, 21),
    (204, 0, 0),
    (217, 173, 22),
    (98, 55, 106),
    (0, 137, 173),
}


def doomwood_defense() -> None:
    """
    Executes the doomwood defense quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.X,
        CombatMoves.EIGHT,
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
    player = Player(player_moves, pet_moves)
    start_quest()

    while True:
        enemy_coordinates = find_rgb_coordinates(ENEMIES)
        if not enemy_coordinates:
            break

        player.go_to(enemy_coordinates[0])
        player.battle()
