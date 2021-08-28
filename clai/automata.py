from typing import Any, Union

import numpy as np
import numpy.typing as npt

from .rules import Base1DRule


def init(shape: Union[int, tuple[int, int]], setting: str = "simple", dtype: npt.DTypeLike = np.int, k: int = 2) -> npt.NDArray[npt.DTypeLike]:
    if setting == "simple":
        a = np.zeros(shape, dtype=dtype)

        if isinstance(shape, int):
            a[len(a) // 2] = k - 1
        else:
            a[a.shape[0] // 2][a.shape[1] // 2] = k - 1

        return a
    elif setting == "random":
        return np.random.randint(k, size=shape, dtype=dtype)
    else:
        raise ValueError(f"'{setting}' is not a valid init preset name; supported names are: 'simple', 'random'")


class CellularAutomaton1D:
    def __init__(self, rule: Base1DRule, init: Union[list[Any], npt.NDArray[Any]], width: int = 100):
        if len(init) != width:
            raise ValueError("init length must be same as width value (default width is 100)")

        self._rule = rule
        self._width = width
        self.generations = [init]

    def next(self) -> list[Any]:
        self.generations.append(self._rule.apply(self.generations[-1]))
        return self.generations[-1]

    def run(self, generations: int) -> list[Any]:
        for _ in range(generations):
            self.next()

        return self.generations[-1]
