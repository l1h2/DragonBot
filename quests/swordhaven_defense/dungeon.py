from player import Player
from utils import CombatMoves, find_rgb_coordinates

from .entrance import start_quest

ENEMIES = {
    (0, 255, 0),
    (217, 83, 33),
    (182, 36, 0),
    (250, 229, 108),
    (203, 214, 212),
    (255, 255, 175),
    (64, 63, 62),
}


def swordhaven_defense() -> None:
    """
    Executes the swordhaven defense quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.ONE,
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
