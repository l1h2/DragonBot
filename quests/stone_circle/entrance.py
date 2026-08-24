from player import Player


def start_quest() -> None:
    """
    Starts the stone circle quest.
    """
    player = Player()
    player.check_screen((570, 470), (98, 95, 34), "initial")

    player.go_right()
    player.go_right()
    player.go_right()
    player.go_to((1650, 360), (0, 0, 0))
    player.go_right()
    player.go_right()
    player.go_up()
