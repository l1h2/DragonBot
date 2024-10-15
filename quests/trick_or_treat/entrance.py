from player import Player


def start_quest() -> None:
    """
    Starts the trick or treat quest.
    """
    player = Player()
    player.check_screen((600, 800), (159, 152, 95), "initial")
