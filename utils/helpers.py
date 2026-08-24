import cv2
import numpy as np
import pyautogui
import pytesseract

from utils import RGB, Point2


def find_rgb_coordinates(
    target_rgb: set[RGB],
    start_xy: Point2 = (270, 25),
    end_xy: Point2 = (1650, 850),
) -> tuple[Point2, RGB] | None:
    """
    Finds the coordinates of a specific RGB color on the screen.

    Args:
        target_rgb (set[RGB]): The target RGB colors to search for.
        start_xy (Point2, optional): The starting (x, y) coordinates to search from. Defaults to (270, 25).
        end_xy (Point2, optional): The ending (x, y) coordinates to search to. Defaults to (1650, 850).

    Returns:
        tuple[Point2, RGB] | None: The (x, y) coordinates and the RGB value of the first target RGB color found, or None if not found
    """
    region = (*start_xy, end_xy[0] - start_xy[0], end_xy[1] - start_xy[1])
    screenshot = pyautogui.screenshot(region=region)

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel = screenshot.getpixel((x, y))
            if pixel in target_rgb:
                return (x + start_xy[0], y + start_xy[1]), pixel

    return None


def get_reward_text(start_xy: Point2 = (690, 280), end_xy: Point2 = (1290, 320)) -> str:
    region = (*start_xy, end_xy[0] - start_xy[0], end_xy[1] - start_xy[1])
    screenshot = pyautogui.screenshot(region=region)

    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    reward_text: str = pytesseract.image_to_string(gray_image)
    return reward_text.strip()
