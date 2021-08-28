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
    def __init__(self, rule: Base1DRule, init: Union[list[Any], npt.NDArray[Any]]):
        self._rule = rule
        self.generations = [init]

    def generate(self, generations: int = 1) -> None:
        for _ in range(generations):
            self.generations.append(self._rule.apply(self.generations[-1]))
