import time

import pyautogui

from player import Player
from utils import Actions, CombatMoves, DirectionsRGB, Point2, wait_for_timeout

from .entrance import start_quest

EXIT_XY = (1200, 590)
FLOORS = {
    1: DirectionsRGB((14, 13, 14), (34, 31, 32), (47, 44, 46), (48, 45, 47)),
    2: DirectionsRGB((11, 10, 11), (27, 24, 26), (38, 35, 38), (38, 36, 39)),
    3: DirectionsRGB((8, 7, 9), (21, 18, 21), (29, 26, 31), (29, 27, 31)),
    4: DirectionsRGB((7, 6, 8), (17, 15, 19), (24, 22, 27), (25, 22, 28)),
    5: DirectionsRGB((6, 5, 7), (14, 12, 16), (20, 17, 23), (20, 18, 23)),
}


def crypt_of_the_lost_order_dungeon() -> None:
    """
    Executes the Crypt of the Lost Order dungeon quest.
    """
    player_moves = [
        CombatMoves.THREE,
        CombatMoves.TWO,
        CombatMoves.ONE,
        CombatMoves.Z,
        CombatMoves.V,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.ONE,
        CombatMoves.THREE,
        CombatMoves.FOUR,
        CombatMoves.FIVE,
        CombatMoves.SIX,
    ]
    path_rgb = FLOORS[1]
    battle_xy = (1500, 975)
    battle_rgb = (174, 0, 0)

    player = Player(player_moves, pet_moves, path_rgb, battle_rgb, battle_xy)

    start_quest()
    __dungeon_crawl(player)


def __dungeon_crawl(player: Player) -> None:
    """
    Moves the player through the dungeon, battling enemies and finishing the quest.

    Args:
        player (Player): The player object.
    """
    origin: Point2 | None = None
    quest_finished = False
    found_lever = False
    found_exit = False
    return_path: list[Point2] = []
    current_floor = 1

    while not quest_finished:
        try:
            time.sleep(0.1)  # Wait for screen transition

            if current_floor != 5:
                if not found_lever:
                    found_lever = __look_for_lever(current_floor)

                if found_exit:
                    if not found_lever:
                        __update_return_path(return_path, origin, player)
                    else:
                        return_path.append(origin)
                        __return_to_exit(player, return_path, current_floor)
                        found_lever = False
                        found_exit = False
                        origin = None
                        current_floor += 1

            origin = player.move(origin)

            if player.check_for_battle():
                player.battle()
                player.keep_moving(origin)

        except ValueError:
            if __found_chest(current_floor):
                __open_chest(player)

            elif current_floor != 5:
                found_exit = __look_for_exit(player, current_floor)
                if found_exit and found_lever:
                    found_lever = False
                    found_exit = False
                    origin = None
                    current_floor += 1
                    continue

            if player.find_boss(origin):
                player.battle()
                __complete_quest(player, origin)
                quest_finished = True

            origin = None


def __found_chest(current_floor: int) -> bool:
    """
    Checks if the chest has been found.

    Returns:
        bool: Whether the chest has been found or not.
    """
    floor_chest_rgb = {
        1: (153, 89, 16),
        2: (133, 71, 13),
        3: (114, 53, 10),
        4: (104, 44, 9),
        5: (94, 35, 8),
    }
    if pyautogui.pixel(960, 490) == floor_chest_rgb[current_floor]:
        return True
    else:
        return False


def __open_chest(player: Player) -> None:
    """
    Opens the chest and collects the loot.

    Args:
        player (Player): The player object.
    """
    pyautogui.click(960, 490)  # Open chest
    time.sleep(1.2)

    if player.check_for_battle():
        player.battle()
        pyautogui.click(960, 490)  # Open chest

    wait_for_timeout((1580, 850), (255, 246, 85), Actions.REWARD_SCREEN)
    pyautogui.click(700, 275)  # Select loot
    wait_for_timeout((1400, 420), (225, 185, 149), Actions.REWARD_SCREEN)
    pyautogui.click(1350, 820)  # Collect loot
    wait_for_timeout((800, 460), (234, 206, 166), Actions.REWARD_SCREEN)
    pyautogui.click(875, 550)  # Confirm reward
    wait_for_timeout((1300, 1000), (233, 207, 165), Actions.REWARD_SCREEN)


def __look_for_lever(current_floor: int) -> bool:
    """
    Looks for the floor lever in the room.

    Args:
        current_floor (int): The current level of the dungeon

    Returns:
        bool: Whether the lever was found or not.
    """
    floor_lever_rgb = {
        1: (62, 0, 0),
        2: (50, 0, 0),
        3: (38, 0, 0),
        4: (32, 0, 0),
    }

    if pyautogui.pixel(1060, 435) != floor_lever_rgb[current_floor]:
        return False

    pyautogui.click(980, 540)  # Pull lever
    time.sleep(1.2)
    return True


def __look_for_exit(player: Player, current_floor: int) -> bool:
    """
    Looks for exit to the next level of the dungeon.

    Args:
        player (Player): The player object.
        current_floor (int): The current floor of the dungeon

    Returns:
        bool: Whether the exit was found or not.
    """
    floor_exit_rgb = {
        1: (69, 64, 62),
        2: (56, 51, 51),
        3: (42, 38, 41),
        4: (36, 32, 36),
    }
    if pyautogui.pixel(*EXIT_XY) == (0, 0, 0):  # Found open door
        __go_down_stairs(player, current_floor)
        return True
    elif pyautogui.pixel(*EXIT_XY) == floor_exit_rgb[current_floor]:
        return True

    return False


def __update_return_path(
    return_path: list[Point2], origin: Point2, player: Player
) -> None:
    """
    Updates the return path to the exit.

    Args:
        return_path (list[Point2]): The current return path to the exit.
        origin (Point2): The last path taken.
        player (Player): The player object.
    """
    if origin is None:
        return

    opposite_direction = {
        player.directions.up: player.directions.down,
        player.directions.down: player.directions.up,
        player.directions.left: player.directions.right,
        player.directions.right: player.directions.left,
    }

    if not return_path:
        return_path.append(origin)
        return

    if origin == opposite_direction[return_path[-1]]:
        return_path.pop()
        return

    return_path.append(origin)


def __return_to_exit(
    player: Player, return_path: list[Point2], current_floor: int
) -> None:
    """
    Returns to the exit after finding the lever.

    Args:
        player (Player): The player object.
        return_path (list[Point2]): The return path to the exit.
        current_floor (int): The current floor of the dungeon
    """
    if not return_path:
        return

    direction_map = {
        player.directions.up: player.go_up,
        player.directions.down: player.go_down,
        player.directions.left: player.go_left,
        player.directions.right: player.go_right,
    }

    while return_path:
        player.remove_white_text_bar()
        direction_map[return_path.pop()]()

    __go_down_stairs(player, current_floor)


def __go_down_stairs(player: Player, current_floor: int) -> None:
    """
    Moves the player down the stairs to the next level of the dungeon.

    Args:
        player (Player): The player object.
        current_floor (int): The current floor of the dungeon
    """
    pyautogui.click(*EXIT_XY)  # Go down stairs

    try:
        wait_for_timeout((1600, 800), (0, 0, 0), Actions.SCREEN_TRANSITION)
    except TimeoutError as e:
        print("Missed stairs transition:", e)  # Log the error

    time.sleep(0.1)  # Wait for screen transition
    player.reset_navigation(FLOORS[current_floor + 1])

    if pyautogui.pixel(*player.directions.right) == player.path_rgb.right:
        pyautogui.click(970, 660)
        player.wait_for_player_position((965, 640), (133, 156, 169))
        pyautogui.click(1515, 655)
        player.wait_for_player_position((1515, 655), (65, 77, 85))


def __complete_quest(player: Player, origin: Point2) -> None:
    """
    Completes the quest after defeating the boss.

    Args:
        player (Player): The player object.
        origin (Point2): The origin of the player.
    """
    __find_goal(player, origin)
    wait_for_timeout((1000, 600), (25, 20, 16), Actions.QUEST_COMPLETE_CONFIRMATION)
    pyautogui.click(960, 250)  # Complete quest

    wait_for_timeout((1200, 400), (234, 206, 166), Actions.QUEST_COMPLETE)
    pyautogui.click(x=960, y=800)

    wait_for_timeout((1020, 850), (83, 25, 14), Actions.REWARD_SCREEN)
    pyautogui.click(x=960, y=800)


def __find_goal(player: Player, origin: Point2) -> None:
    """
    Finds the goal of the dungeon.

    Args:
        player (Player): The player object.
        origin (Point2): The origin of the player.

    Returns:
        bool: Whether the goal was found or not.
    """
    if origin == player.directions.right or origin == player.directions.left:
        pyautogui.click(975, 500)

    elif origin == player.directions.up or origin == player.directions.down:
        player.keep_moving(origin)
