import time

import keyboard
import pyautogui

from utils import Actions, CombatMoves, wait_for_timeout


class Combat:
    """
    ### Represents a combat scenario in the game.

    ### Attributes:
    - `player_moves` (list[CombatMoves]): The moves the player will use in battle.
    - `pet_moves` (list[CombatMoves]): The moves the pet will use in battle.

    ### Methods:
    - `battle`: Perform combat turns until the battle is won.
    """

    __attack_xy = (960, 810)
    __attack_rgb = (166, 26, 26)
    __victory_xy = (975, 189)
    __victory_rgb = (254, 228, 236)

    def __init__(
        self, player_moves: list[CombatMoves], pet_moves: list[CombatMoves]
    ) -> None:
        self.player_moves = player_moves
        self.pet_moves = pet_moves

    def battle(self) -> None:
        """
        Perform combat turns until the battle is won.
        """
        turn = 0
        in_battle = True

        while in_battle:
            turn += 1

            in_battle = self.__combat_turn(self.player_moves, turn)

            if not in_battle:
                break

            in_battle = self.__combat_turn(self.pet_moves, turn)

        keyboard.press("space")  # End battle
        self.__check_level_up()

    def __wait_for_turn(self) -> None:
        """
        Waits for the player's turn in combat.
        """
        wait_for_timeout(self.__attack_xy, self.__attack_rgb, Actions.COMBAT_TURN)

    def __select_move(self, moves: list[CombatMoves], turn: int) -> None:
        """
        Selects a move to perform in combat.

        Args:
            moves (list[CombatMoves]): The moves available.
            turn (int): The current turn number.
        """
        if len(moves) > turn:
            move = moves[turn - 1]
        else:
            move = CombatMoves.ATTACK

        while pyautogui.pixel(*self.__attack_xy) == self.__attack_rgb:
            time.sleep(0.3)
            keyboard.press(move.value)

    def __check_victory(self) -> bool:
        """
        Checks if the battle has been won.

        Returns:
            bool: True if the battle has been won, False otherwise.
        """
        while pyautogui.pixel(*self.__attack_xy) != self.__attack_rgb:
            if pyautogui.pixel(*self.__victory_xy) == self.__victory_rgb:
                return True
        return False

    def __combat_turn(self, moves: list[CombatMoves], turn: int) -> bool:
        """
        Performs a combat turn.

        Args:
            moves (list[CombatMoves]): The list of moves available to the player or pet.
            turn (int): The current turn number.

        Returns:
            bool: True if the battle is still ongoing, False if the battle has been won.
        """
        self.__wait_for_turn()
        self.__select_move(moves, turn)
        return not self.__check_victory()

    def __check_level_up(self) -> None:
        """
        Checks if the player has leveled up and clicks the level up button if so.
        """
        if pyautogui.pixel(1626, 863) == (44, 47, 54):
            return

        time.sleep(1)
        while pyautogui.pixel(960, 1000) == (0, 0, 0):
            pyautogui.click(x=960, y=800)  # Level up
            time.sleep(0.5)
