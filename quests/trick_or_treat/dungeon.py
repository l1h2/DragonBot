import time

import pyautogui

from player import Player
from utils import Actions, CombatMoves, wait_for_timeout

from .entrance import start_quest


def trick_or_treating() -> None:
    """
    Goes trick or treating.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.THREE,
        CombatMoves.TWO,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.FIVE,
        CombatMoves.SIX,
    ]
    battle_rgb = (28, 28, 28)
    battle_xy = (1060, 230)
    player = Player(player_moves, pet_moves, battle_rgb=battle_rgb, battle_xy=battle_xy)
    start_quest()
    trick_or_treat(player)


def trick_or_treat(player: Player) -> None:
    """
    Executes the trick or treat quest.

    Args:
        player (Player): The player object.
    """
    player.remove_white_text_bar()
    if not pyautogui.pixelMatchesColor(400, 970, (229, 0, 0)):
        pyautogui.click(x=1400, y=70)  # Heal

    pyautogui.click(x=960, y=400)  # Go to house
    # wait_for_timeout((1200, 800), (165, 133, 40), "house door")
    wait_for_timeout((1200, 800), (56, 69, 73), "house door")

    pyautogui.click(x=1500, y=80)  # Knock on door
    time.sleep(1)

    if pyautogui.pixelMatchesColor(600, 60, (255, 153, 0)):
        pyautogui.click(x=600, y=320)  # Treat
    elif pyautogui.pixelMatchesColor(875, 290, (254, 254, 0)):
        pyautogui.click(x=650, y=350)  # Moglin treat
    elif pyautogui.pixelMatchesColor(865, 290, (254, 254, 0)):
        pyautogui.click(x=650, y=350)  # Alternative moglin treat
    elif pyautogui.pixelMatchesColor(605, 60, (1, 0, 0)):
        pyautogui.click(x=615, y=235)  # Trick
        player.battle()
    else:
        raise ValueError("Unknown response")

    # wait_for_timeout((935, 600), (255, 255, 255), "candy")
    # wait_for_timeout((937, 601), (255, 255, 255), "candy")
    wait_for_timeout((1045, 600), (173, 52, 31), "candy")
    pyautogui.click(x=950, y=600)  # Take candy
