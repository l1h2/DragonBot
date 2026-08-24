from player import Player
from utils import CombatMoves

from .entrance import start_quest


def haunted_castle() -> None:
    """
    Executes the haunted castle quest.
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
    player.go_up()
    player.battle()
    player.go_up()

    player.go_right()
    player.battle()
    player.go_to((1600, 500))

    player.go_right()
    player.battle()
    player.go_to((800, 800), (75, 88, 98))
    player.go_to((1600, 800))
    player.battle()
    player.go_right()

    player.go_to((375, 800), (75, 88, 98))
    player.go_to((1550, 800), (153, 168, 174))
    player.go_to((1580, 100))
    player.battle()
    player.go_to((1450, 130))

    player.go_to((445, 150))
    player.battle()
    player.go_to((445, 150))
    player.battle()
    player.go_to((445, 150))

    player.go_up()
    player.battle()
    player.go_down()

    player.go_to((1425, 820))

    player.go_to((1460, 800), (75, 88, 98))
    player.go_to((445, 815), (75, 88, 98))
    player.go_left()

    player.go_to((1050, 815), (75, 88, 98))
    player.go_to((290, 620))

    player.go_up()
    player.battle()
    player.go_up()

    player.go_right()
    player.battle()
    player.go_to((1600, 500))

    player.go_right()
    player.battle()
    player.go_to((280, 500))

    player.remove_white_text_bar()
    player.go_up()
    player.battle()
    player.go_up()

    player.remove_white_text_bar()
    player.go_up()
    player.battle()
