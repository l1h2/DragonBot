from player import Player
from utils import CombatMoves, Directions, DirectionsRGB

from .entrance import Quest, start_quest


def shadow_bones() -> None:
    """
    Executes the shadow bones quest.
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
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.SIX,
    ]
    path_rgb = DirectionsRGB((36, 64, 84), (36, 64, 84), (36, 64, 84), (36, 64, 84))
    battle_rgb = (67, 46, 2)

    player = Player(player_moves, pet_moves, path_rgb, battle_rgb)

    start_quest(Quest.SHADOW_BONES)
    player.dungeon_crawl()


def braughlmurk_bindings() -> None:
    """
    Executes the braughlmurk bindings quest.
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
    path_rgb = DirectionsRGB((29, 24, 19), (24, 45, 48), (33, 28, 22), (25, 21, 16))
    battle_rgb = (31, 20, 9)
    battle_xy = (300, 200)
    directions = Directions(up=(980, 50), down=(1020, 840))

    player = Player(
        player_moves, pet_moves, path_rgb, battle_rgb, battle_xy, directions
    )

    start_quest(Quest.BRAUGHLMURK_BINDINGS)
    player.dungeon_crawl()
