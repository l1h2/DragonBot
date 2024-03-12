import time
from dataclasses import dataclass

import pyautogui

from utils import (
    RGB,
    Actions,
    Directions,
    DirectionsRGB,
    Menus,
    Point2,
    wait_for_timeout,
)


@dataclass
class Node:
    """
    A node representing a branch in the maze.
    """

    origin: Point2
    unvisited_directions: list[Point2]
    visited_directions: list[Point2]
    current_depth: int
    backtrack: bool


class Exploration:
    """
    ### A class representing the player's exploration actions.

    ### Attributes:
    - `path_rgb` (RGB): The RGB color value of the path.
    - `battle_rgb` (RGB): The RGB color value of the battle screen.
    - `battle_xy` (Point2): The (x, y) coordinates of the battle screen.
    - `directions` (Directions): The directions to move in.

    ### Methods:
    - `go_up`: Moves the player up.
    - `go_down`: Moves the player down.
    - `go_left`: Moves the player left.
    - `go_right`: Moves the player right.
    - `menu_heal`: Opens the journal menu and heal.
    - `travel`: Travels to the specified destination on the travel map.
    - `move`: Moves the player in the next available direction.
    - `check_for_battle`: Checks for a battle on the screen.
    - `keep_moving`: Moves the player in the opposite direction of the origin.
    - `find_boss`: Searches for boss in a dead end.
    - `finish_quest`: Finishes the quest by completing the dungeon and claiming the reward.
    """

    def __init__(
        self,
        path_rgb: DirectionsRGB,
        battle_rgb: RGB,
        directions: Directions,
        battle_xy: Point2,
    ):
        self.path_rgb = path_rgb
        self.battle_rgb = battle_rgb
        self.battle_xy = battle_xy
        self.directions = directions

        self.__active_nodes: list[Node] = []
        self.__current_depth: int = 1

    def go_up(self, wait: bool = True) -> None:
        """
        Moves the player up.

        Args:
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        self.__go(self.directions.up, wait)

    def go_down(self, wait: bool = True) -> None:
        """
        Moves the player down.

        Args:
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        self.__go(self.directions.down, wait)

    def go_left(self, wait: bool = True) -> None:
        """
        Moves the player left.

        Args:
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        self.__go(self.directions.left, wait)

    def go_right(self, wait: bool = True) -> None:
        """
        Moves the player right.

        Args:
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        self.__go(self.directions.right, wait)

    def wait_for_player_position(self, coord: Point2, rgb: RGB) -> None:
        """
        Waits for the player to reach the specified position without screen transition.

        Args:
            coord (tuple[int, int]): The (x, y) coordinates of the position to reach.
            rgb (tuple[int, int, int]): The RGB color value when position is reached.
        """
        while pyautogui.pixel(*coord) != rgb:
            pass

    def menu_heal(self, close: bool = True) -> None:
        """
        Opens the journal menu and heal.

        Args:
            close (bool, optional): Whether to close the journal menu after healing. Defaults to True.
        """
        # Keyboard presses are inconsistent to handle the journal menu
        pyautogui.click(*Menus.JOURNAL_CLICK.value)
        wait_for_timeout((1500, 150), (234, 206, 166), Actions.MENU_SCREEN)
        pyautogui.click(x=770, y=930)  # Heal
        if close:
            pyautogui.click(*Menus.JOURNAL_CLOSE_CLICK.value)

    def travel(
        self,
        destination: Point2,
        arrival_xy: Point2,
        arrival_rgb: RGB,
        book1: bool = True,
    ) -> None:
        """
        Travels to the specified destination on the travel map.

        Args:
            destination (tuple[int, int]): The (x, y) coordinates of the destination to travel to.
            arrival_xy (tuple[int, int]): The (x, y) coordinates of the arrival screen.
            arrival_rgb (tuple[int, int, int]): The RGB color value of the arrival screen.
            book1 (bool, optional): Whether to open book 1 or book 3. Defaults to True.
        """
        self.menu_heal(close=False)
        self.__travel_map(book1)
        self.__fly(destination, arrival_xy, arrival_rgb)

    def move(self, origin: Point2 | None = None) -> Point2:
        """
        Moves the player in the next available direction.

        Args:
            origin (tuple[int, int], optional): The (x, y) coordinates of the origin. Defaults to None.

        Returns:
            tuple[int, int]: The next origin to move from.
        """
        time.sleep(0.1)  # Wait for screen transition
        self.__remove_white_text_bar()
        available_directions = self.__get_directions(origin)
        self.__check_for_branches(origin, available_directions)
        next_direction = self.__update_active_nodes(available_directions[0])
        return self.__move_and_update_origin(next_direction)

    def check_for_battle(self) -> bool:
        """
        Checks for a battle on the screen.

        Returns:
            bool: True if a battle is found, False otherwise.
        """
        time.sleep(0.6)
        if pyautogui.pixel(*self.battle_xy) == self.battle_rgb:
            pyautogui.click(*self.directions.left)
            return True
        else:
            return False

    def keep_moving(self, origin: Point2, wait: bool = True) -> None:
        """
        Moves the player in the opposite direction of the origin.

        Args:
            origin (tuple[int, int]): The (x, y) coordinates of the origin.
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        direction_map = {
            self.directions.up: self.go_down,
            self.directions.down: self.go_up,
            self.directions.left: self.go_right,
            self.directions.right: self.go_left,
        }
        direction_map[origin](wait)

    def find_boss(self, origin: Point2) -> bool:
        """
        Searches for boss in a dead end.

        Args:
            origin (tuple[int, int]): The (x, y) coordinates of the origin.

        Returns:
            bool: True if the boss is found, False otherwise.
        """
        self.keep_moving(origin, wait=False)
        time.sleep(1)
        found_boss = self.check_for_battle()
        if not found_boss:
            self.__active_nodes[-1].backtrack = True
        return found_boss

    def finish_quest(self, origin: Point2, requires_confirmation: bool) -> None:
        """
        Finishes the quest by completing the dungeon and claiming the reward.

        Args:
            origin (tuple[int, int]): The (x, y) coordinates of the origin.
            requires_confirmation (bool): Whether the quest completion requires confirmation.
        """
        self.__active_nodes.clear()
        self.keep_moving(origin, wait=False)

        if requires_confirmation:
            wait_for_timeout(
                (960, 430), (217, 69, 43), Actions.QUEST_COMPLETE_CONFIRMATION
            )
            pyautogui.click(x=960, y=430)

        wait_for_timeout((1200, 400), (234, 206, 166), Actions.QUEST_COMPLETE)
        pyautogui.click(x=960, y=800)

        wait_for_timeout((1020, 850), (83, 25, 14), Actions.REWARD_SCREEN)
        pyautogui.click(x=960, y=800)

    def __go(self, direction: Point2, wait: bool = True) -> None:
        """
        Moves the player in the specified direction.

        Args:
            direction (tuple[int, int]): The (x, y) coordinates of the direction to move in.
            wait (bool, optional): Whether to wait for a screen transition after moving. Defaults to True.
        """
        pyautogui.click(*direction)
        if wait:
            wait_for_timeout((1600, 800), (0, 0, 0), Actions.SCREEN_TRANSITION)

    def __travel_map(self, book1: bool = True) -> None:
        """
        Opens the travel map.

        Args:
            book1 (bool, optional): Whether to open book 1 or book 3. Defaults to True.
        """
        if book1:
            pyautogui.click(x=600, y=300)  # Book 1
        else:
            pyautogui.click(x=600, y=700)  # Book 3
        pyautogui.click(x=960, y=770)  # Travel map
        wait_for_timeout((500, 750), (51, 118, 53), Actions.TRAVEL_MAP)

    def __fly(self, destination: Point2, arrival_xy: Point2, arrival_rgb: RGB) -> None:
        """
        Flies to the specified destination on the travel map.

        Args:
            destination (tuple[int, int]): The (x, y) coordinates of the destination to fly to.
            arrival_xy (tuple[int, int]): The (x, y) coordinates of the arrival screen.
            arrival_rgb (tuple[int, int, int]): The RGB color value of the arrival screen.
        """
        pyautogui.click(*destination)  # Choose destination
        pyautogui.click(x=1500, y=775)  # Confirm destination
        wait_for_timeout(arrival_xy, arrival_rgb, Actions.DUNGEON_ENTRANCE)

    def __remove_white_text_bar(self) -> None:
        """
        Removes the white text bar from the screen.
        """
        if pyautogui.pixel(1200, 50) != (255, 255, 255):
            return

        pyautogui.click(x=1200, y=50)  # Remove white text bar
        time.sleep(0.1)

    def __get_directions(self, origin: Point2 | None) -> list[Point2]:
        """
        Gets the available directions to move in from the current position.

        Args:
            origin (tuple[int, int] | None): The (x, y) coordinates of the current position.

        Returns:
            list[tuple[int, int]]: The available directions to move in.

        Raises:
            Exception: If no path is found.
        """
        available_directions = [
            direction
            for direction, rgb in zip(
                [
                    self.directions.up,
                    self.directions.down,
                    self.directions.left,
                    self.directions.right,
                ],
                [
                    self.path_rgb.up,
                    self.path_rgb.down,
                    self.path_rgb.left,
                    self.path_rgb.right,
                ],
            )
            if pyautogui.pixel(*direction) == rgb and direction != origin
        ]

        if not available_directions:
            raise Exception("No path found")
        return available_directions

    def __check_for_branches(
        self, origin: Point2 | None, directions: list[Point2]
    ) -> None:
        """
        Checks for branches in the path and adds them to the active nodes list.

        Args:
            origin (tuple[int, int] | None): The (x, y) coordinates of the current position.
            directions (list[tuple[int, int]]): The available directions to move in.
        """
        if not (len(directions) > 1 and self.__current_depth > 0):
            return

        self.__active_nodes.append(
            Node(
                origin=origin,
                unvisited_directions=directions,
                visited_directions=[],
                current_depth=0,
                backtrack=False,
            )
        )

    def __update_active_nodes(self, direction: Point2) -> Point2:
        """
        Updates the active nodes list after moving in a direction.

        Args:
            direction (tuple[int, int]): Available direction to move in.

        Returns:
            tuple[int, int]: The next direction to move in.
        """
        if not self.__active_nodes:
            return direction

        active_node = self.__active_nodes[-1]
        new_direction = None

        if active_node.current_depth == 0:
            if len(active_node.unvisited_directions) > 0:
                new_direction = active_node.unvisited_directions.pop()
                active_node.backtrack = False
                active_node.visited_directions.append(new_direction)
            else:
                new_direction = active_node.origin
                self.__active_nodes.pop()
                self.__active_nodes[-1].backtrack = True

        if self.__active_nodes[-1].backtrack:
            self.__active_nodes[-1].current_depth -= 1
        else:
            self.__active_nodes[-1].current_depth += 1
        self.__current_depth = self.__active_nodes[-1].current_depth
        return new_direction or direction

    def __move_and_update_origin(self, direction: Point2) -> Point2:
        """
        Moves the player in the specified direction.

        Args:
            direction (tuple[int, int]): The (x, y) coordinates of the direction to move in.

        Returns:
            tuple[int, int]: The next origin to move from.
        """
        direction_map = {
            self.directions.up: (self.go_up, self.directions.down),
            self.directions.down: (self.go_down, self.directions.up),
            self.directions.left: (self.go_left, self.directions.right),
            self.directions.right: (self.go_right, self.directions.left),
        }

        move_func, next_origin = direction_map[direction]
        move_func()
        return next_origin
