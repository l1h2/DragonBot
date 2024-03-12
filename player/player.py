import pyautogui

from utils import RGB, CombatMoves, Directions, DirectionsRGB, Point2

from .combat import Combat
from .exploration import Exploration


class Player(Exploration, Combat):
    """
    ### A class to represent the player.

    Inherits from `Exploration` and `Combat` classes.

    ### Attributes:
    - `player_moves` (list[CombatMoves]): The moves the player will use in battle.
    - `pet_moves` (list[CombatMoves]): The moves the pet will use in battle.
    - `path_rgb` (DirectionsRGB): The RGB color values for the path.
    - `battle_rgb` (RGB): The RGB color value for the battle screen.
    - `battle_xy` (Point2): The (x, y) coordinates to check for battles.
    - `directions` (Directions): The (x, y) coordinates for the directions.

    ### Methods:
    - `check_screen`: Checks if player is in the correct screen.
    - `dungeon_crawl`: Moves the player through the dungeon, battling enemies and finishing the quest.
    """

    def __init__(
        self,
        player_moves: list[CombatMoves] = [],
        pet_moves: list[CombatMoves] = [],
        path_rgb=DirectionsRGB(),
        battle_rgb: RGB = (0, 0, 0),
        battle_xy: Point2 = (1600, 500),
        directions=Directions(),
    ):
        super().__init__(path_rgb, battle_rgb, directions, battle_xy)
        self.player_moves = player_moves
        self.pet_moves = pet_moves

    def check_screen(self, coord: Point2, rgb: RGB, screen: str) -> None:
        """
        Checks if player is in the correct screen.

        Args:
            coord (tuple[int, int]): The (x, y) coordinates to check for the pixel color.
            rgb (tuple[int, int, int]): The RGB color value to check for.
            screen (str): The name of the screen being checked.

        Raises:
            Exception: If the specified pixel color does not appear at the given coordinates.
        """
        if pyautogui.pixel(*coord) == rgb:
            return

        raise Exception(
            "Not in {} screen. Please go to the beginning and try again.".format(screen)
        )

    def dungeon_crawl(self, requires_confirmation: bool = False) -> None:
        """
        Moves the player through the dungeon, battling enemies and finishing the quest.

        Args:
            requires_confirmation (bool, optional): Whether or not the player must confirm the quest completion. Defaults to False.
        """
        next_origin = None
        quest_finished = False

        while not quest_finished:
            try:
                next_origin = self.move(next_origin)

                if self.check_for_battle():
                    self.battle()
                    self.keep_moving(next_origin)

            except Exception as e:
                if str(e) != "No path found":
                    raise e
                if self.find_boss(next_origin):
                    self.battle()
                    self.finish_quest(next_origin, requires_confirmation)
                    quest_finished = True
                else:
                    next_origin = None
