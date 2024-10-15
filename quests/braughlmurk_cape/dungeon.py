import time

from player import Player
from utils import CombatMoves, Directions, DirectionsRGB

from .entrance import Quest, start_quest


def shadow_bones() -> None:
    """
    Executes the shadow bones quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.X,
        CombatMoves.NINE,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.V,
        CombatMoves.ONE,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.SIX,
    ]
    player = Player(player_moves, pet_moves)

    start_quest(Quest.SHADOW_BONES)
    player.go_right()
    player.battle()
    player.go_right()

    player.go_right()
    player.battle()
    player.go_to((1385, 740), (75, 88, 98))
    time.sleep(1)  # Heal
    player.go_up()

    player.go_left()
    player.battle()
    player.go_left()

    player.go_left()
    player.battle()
    player.go_left()

    player.go_left()
    player.battle()
    player.go_left()

    player.go_left()
    player.battle()
    player.go_to((500, 240), (0, 0, 0))

    player.go_up()
    player.battle()
    player.finish_quest(player.directions.down)


def braughlmurk_bindings() -> None:
    """
    Executes the braughlmurk bindings quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.X,
        CombatMoves.NINE,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.V,
        CombatMoves.ONE,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.SIX,
    ]
    player = Player(player_moves, pet_moves)

    start_quest(Quest.BRAUGHLMURK_BINDINGS)
    player.go_to((1450, 620), (49, 58, 71))
    time.sleep(1)  # Heal
    player.go_left()
    player.battle()
    player.go_to((470, 85), (0, 0, 0))

    player.go_left()
    player.battle()
    player.go_to((470, 85), (0, 0, 0))

    player.go_left()
    player.battle()
    player.go_to((500, 60), (0, 0, 0))

    player.go_to((470, 690), (45, 54, 66))
    player.go_to((470, 85), (0, 0, 0))

    player.go_left()
    player.battle()
    player.go_to((500, 60), (0, 0, 0))

    player.go_left()
    player.battle()
    player.go_to((500, 60), (0, 0, 0))

    player.go_left()
    player.battle()
    player.go_up()

    player.go_right()
    player.battle()
    player.go_to((1460, 700), wait=False)
    time.sleep(1)  # Wait for player to reach goal
    player.finish_quest(player.directions.left)
