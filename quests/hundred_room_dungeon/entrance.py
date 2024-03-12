from player import Player


def start_quest() -> None:
    """
    Travels to quest starting location.
    """
    player = Player()
    destination = (1535, 200)
    arrival_rgb = (101, 34, 7)
    arrival_xy = (300, 473)

    player.travel(destination, arrival_xy, arrival_rgb)
