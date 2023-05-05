
import pathlib
from typing import Callable, Dict, Tuple, Union

MaterialSpec = Union[str, float, Tuple[float, float], Callable]
PathType = pathlib.Path | str
