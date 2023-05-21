import numpy as np

from typing import List


def move_polar_rad_copy(pos: List(float), angle: float, length: float) -> np.ndarray:
    """Returns the points of a position (pos) with angle, by shifted by certain.

    length.

    Args:
        pos: position.
        angle: in radians.
        length: extension length in um.
    """
    c = np.cos(angle)
    s = np.sin(angle)
    return pos + length * np.array([c, s])
