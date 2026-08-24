from player import Player
from utils import CombatMoves, find_rgb_coordinates

from .entrance import start_quest

ENEMIES = {
    (70, 133, 136),  # Flan
    (80, 186, 122),  # Elemental
    (74, 168, 207),  # Elemental 2
    (177, 143, 88),  # Cat
    (0, 140, 255),  # Tog
    (224, 235, 238),  # Skeleton
    (207, 226, 216),  # Mushroom
    (211, 194, 158),  # Golem
    (128, 144, 154),  # Drake
}


def war() -> None:
    """
    Executes war waves.z
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
        CombatMoves.V,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.ONE,
        CombatMoves.SIX,
        CombatMoves.FIVE,
    ]

    player = Player(
        player_moves, pet_moves, battle_xy=(960, 810), battle_rgb=(166, 26, 26)
    )
    start_quest()

    while True:
        try:
            player.check_screen((1500, 500), (234, 206, 166), "initial")
            break
        except ValueError:
            pass

        enemy_coordinates = find_rgb_coordinates(ENEMIES)
        if not enemy_coordinates:
            continue

        player.go_to(enemy_coordinates[0])
        if player.check_for_battle(2):
            player.battle()
        else:
            new_coordinates = (
                enemy_coordinates[0][0] + 100,
                enemy_coordinates[0][1] + 200,
            )
            player.go_to(new_coordinates)
            if player.check_for_battle(2):
                player.battle()
