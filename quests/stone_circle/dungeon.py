import keyboard
import pyautogui

from player import Player
from utils import Actions, CombatMoves, get_reward_text, wait_for_timeout
from utils.game_objects import ExploreActions

from .entrance import start_quest

BAD_REWARDS = {
    "Flamestone Staff",
    "Force of Nature",
    "Flamestone Shiv",
    "Dagger of the forest",
    "Flamestone Blade",
    "The Greenman's Blade",
}


def stone_circle() -> None:
    """
    Executes the stone circle quest.
    """
    player_moves = [
        CombatMoves.Z,
        CombatMoves.V,
        CombatMoves.C,
        CombatMoves.SIX,
        CombatMoves.SIX,
    ]
    pet_moves = [
        CombatMoves.SEVEN,
        CombatMoves.V,
        CombatMoves.ONE,
        CombatMoves.FOUR,
        CombatMoves.THREE,
        CombatMoves.SIX,
    ]
    battle_xy = (1300, 530)
    battle_rgb = (220, 198, 109)

    player = Player(
        player_moves,
        pet_moves,
        battle_rgb=battle_rgb,
        battle_xy=battle_xy,
    )
    start_quest()

    while not player.check_for_battle(0):
        keyboard.press(ExploreActions.MOVE_UP.value)

    keyboard.release(ExploreActions.MOVE_UP.value)

    player.battle()
    player.go_up(False)

    wait_for_timeout((1200, 400), (234, 206, 166), Actions.QUEST_COMPLETE)
    pyautogui.click(x=960, y=800)

    wait_for_timeout((1020, 850), (83, 25, 14), Actions.REWARD_SCREEN)
    reward = get_reward_text()

    if reward not in BAD_REWARDS:
        print(f"Getting Reward: {reward}")
        pyautogui.click(x=960, y=800)
    else:
        pyautogui.click(x=960, y=850)
        pyautogui.click(x=870, y=550)
