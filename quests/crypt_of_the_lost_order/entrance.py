from player import Player


def start_quest() -> None:
    """
    Travels to quest starting location.
    """
    player = Player()
    destination = (875, 400)
    arrival_rgb = (69, 64, 62)
    arrival_xy = (300, 400)

    player.travel(destination, arrival_xy, arrival_rgb)
