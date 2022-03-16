from typing import Any, Dict, Tuple, overload

from ._common import ColorValue

THECOLORS: Dict[str, Tuple[int, int, int, int]]

class Color:
    r: int
    g: int
    b: int
    a: int
    cmy: Tuple[float, float, float]
    hsva: Tuple[float, float, float, float]
    hsla: Tuple[float, float, float, float]
    i1i2i3: Tuple[float, float, float]
    __hash__: None  # type: ignore
    __array_struct__: Any
    @overload
    def __init__(self, r: int, g: int, b: int, a: int = 255) -> None: ...
    @overload
    def __init__(self, rgbvalue: ColorValue) -> None: ...
    @overload
    def __getitem__(self, i: int) -> int: ...
    @overload
    def __getitem__(self, s: slice) -> Tuple[int]: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __add__(self, other: Color) -> Color: ...
    def __sub__(self, other: Color) -> Color: ...
    def __mul__(self, other: Color) -> Color: ...
    def __floordiv__(self, other: Color) -> Color: ...
    def __mod__(self, other: Color) -> Color: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __len__(self) -> int: ...
    def __index__(self) -> int: ...
    def __invert__(self) -> Color: ...
    def normalize(self) -> Tuple[float, float, float, float]: ...
    def correct_gamma(self, gamma: float) -> Color: ...
    def set_length(self, length: int) -> None: ...
    def lerp(self, color: ColorValue, amount: float) -> Color: ...
    def premul_alpha(self) -> Color: ...
    @overload
    def update(self, r: int, g: int, b: int, a: int = 255) -> None: ...
    @overload
    def update(self, rgbvalue: ColorValue) -> None: ...
