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

    _attack_xy = (960, 810)
    _attack_rgb = (166, 26, 26)
    _victory_xy = (975, 189)
    _victory_rgb = (254, 228, 236)

    def __init__(
        self, player_moves: list[CombatMoves], pet_moves: list[CombatMoves]
    ) -> None:
        self.player_moves = player_moves
        self.pet_moves = pet_moves

    @property
    def need_heal(self) -> bool:
        """
        Returns True if the player needs to use a healing potion.
        """
        return pyautogui.pixel(450, 970) != (229, 0, 0)

    def battle(self) -> None:
        """
        Perform combat turns until the battle is won.
        """
        turn = 0
        in_battle = True
        used_heal = False

        while in_battle:
            turn += 1

            # if self.need_heal and not used_heal:
            #     in_battle = self._defensive_turn()
            #     used_heal = True
            #     turn -= 1
            #     continue

            in_battle = self._combat_turn(self.player_moves, turn)

            if not in_battle:
                break

            in_battle = self._combat_turn(self.pet_moves, turn)

        keyboard.press("space")  # End battle
        self._post_battle()

    def _wait_for_turn(self) -> None:
        """
        Waits for the player's turn in combat.
        """
        wait_for_timeout(self._attack_xy, self._attack_rgb, Actions.COMBAT_TURN)

    def _select_move(self, moves: list[CombatMoves], turn: int) -> None:
        """
        Selects a move to perform in combat.

        Args:
            moves (list[CombatMoves]): The moves available.
            turn (int): The current turn number.
        """
        if len(moves) >= turn:
            move = moves[turn - 1]
        else:
            move = CombatMoves.ATTACK

        self._use_move(move)

    def _use_move(self, move: CombatMoves) -> None:
        """
        Performs a move in combat.

        Args:
            move (CombatMoves): The move to perform.
        """
        while pyautogui.pixel(*self._attack_xy) == self._attack_rgb:
            time.sleep(0.3)
            keyboard.press(move.value)

    def _check_victory(self) -> bool:
        """
        Checks if the battle has been won.

        Returns:
            bool: True if the battle has been won, False otherwise.
        """
        while pyautogui.pixel(*self._attack_xy) != self._attack_rgb:
            if pyautogui.pixel(*self._victory_xy) == self._victory_rgb:
                return True
        return False

    def _combat_turn(self, moves: list[CombatMoves], turn: int) -> bool:
        """
        Performs a combat turn.

        Args:
            moves (list[CombatMoves]): The list of moves available to the player or pet.
            turn (int): The current turn number.

        Returns:
            bool: True if the battle is still ongoing, False if the battle has been won.
        """
        self._wait_for_turn()
        self._select_move(moves, turn)
        return not self._check_victory()

    def _defensive_turn(self):
        player_heal = CombatMoves.THREE
        pet_heal = CombatMoves.SIX

        in_battle = self._combat_turn([player_heal], 1)

        if not in_battle:
            return in_battle

        in_battle = self._combat_turn([pet_heal], 1)
        return in_battle

    def _post_battle(self) -> None:
        """
        Checks if the player has leveled up and other battle rewards.
        """
        time.sleep(1)
        while pyautogui.pixel(960, 1000) == (0, 0, 0):
            # keyboard.press(ExploreActions.ACCEPT.value)  # Level up and rewards
            pyautogui.click(x=960, y=800)  # Level up and rewards

            time.sleep(0.5)
