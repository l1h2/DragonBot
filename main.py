from quests import Quest, Quests
from utils import select_game_window, start_recording, stop_recording


def main(quest: Quest, repeat: int = 0, record: bool = False) -> None:
    """
    Main function to execute a quest.

    Args:
        quest (Quest): The quest to be executed.
        repeat (int): The number of times to repeat the quest.
        record (bool): Whether to record the quest execution.
    """

    counter = 0
    select_game_window()
    try:
        if record:
            start_recording()
        for _ in range(repeat + 1):
            quest.start_quest()
            counter += 1
            print("Quests completed:", counter)
            quest.wait_to_restart()

    except Exception as e:
        print("Process terminated:", e)

    finally:
        if record:
            stop_recording()


if __name__ == "__main__":
    quest = Quest(Quests.HUNDRED_ROOM_DUNGEON)
    repeat = 7
    record = True

    main(quest, repeat, record)
