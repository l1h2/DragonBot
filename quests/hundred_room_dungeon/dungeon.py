from player import Player
from utils import CombatMoves, DirectionsRGB

from .entrance import start_quest


def hundred_room_dungeon() -> None:
    """
    Executes the hundred room dungeon quest.
    """
    player_moves = [
        CombatMoves.NINE,
        CombatMoves.V,
        CombatMoves.Z,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.ONE,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.SIX,
    ]
    path_rgb = DirectionsRGB((39, 7, 7), (39, 7, 7), (25, 9, 7), (26, 9, 8))
    battle_rgb = (95, 57, 50)

    player = Player(player_moves, pet_moves, path_rgb, battle_rgb)

    start_quest()
    player.dungeon_crawl(True)
