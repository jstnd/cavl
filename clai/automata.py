from typing import Callable, Type, Union

import numpy as np
import numpy.typing as npt


def init(shape: Union[int, tuple[int, int]],
         setting: str = "simple",
         dtype: Type[float] = int,
         k: int = 2) -> npt.NDArray[float]:
    if setting == "simple":
        a = np.zeros(shape, dtype=dtype)

        if isinstance(shape, int):
            a[len(a) // 2] = dtype(k - 1)
        else:
            a[a.shape[0] // 2][a.shape[1] // 2] = dtype(k - 1)

        return a
    elif setting == "random":
        return np.random.randint(k, size=shape, dtype=dtype)
    else:
        raise ValueError(f"'{setting}' is not a valid init preset name; supported names are: 'simple', 'random'")


class CellularAutomaton1D:
    def __init__(
            self,
            init: Union[list[float], npt.NDArray[float]],
            neighbors: list[tuple[int, int]],
            apply: Callable[[dict[tuple[int, int]]], float]
    ):
        self.generations = [init]
        self.neighbors = neighbors
        self.apply = apply
        self.width = len(init)

    def evolve(self, generations: int = 1) -> None:
        for _ in range(generations):
            self.generations.append(self._generation())

    def _generation(self) -> list[float]:
        next_generation = []
        for x in range(self.width):
            next_generation.append(self.apply(self._get_neighbors(x)))

        return next_generation

    def _get_neighbors(self, x: int) -> dict[tuple[int, int], float]:
        neighbors = {}
        for neighbor in self.neighbors:
            dx, dy = neighbor
            neighbors[neighbor] = self.generations[(-1 + dy) % len(self.generations)][(x + dx) % self.width]

        return neighbors


class CellularAutomaton2D:
    def __init__(
            self,
            init: Union[list[list[float]], npt.NDArray[npt.NDArray[float]]],
            neighbors: list[tuple[int, int]],
            apply: Callable[[dict[tuple[int, int], float], float], float]
    ):
        self.generations = [init]
        self.neighbors = neighbors
        self.apply = apply
        self.width = len(init[0])
        self.height = len(init)

    def evolve(self, generations: int = 1) -> None:
        for _ in range(generations):
            self.generations.append(self._generation())

    def _generation(self) -> list[list[float]]:
        next_generation = []
        for y in range(self.height):
            next_row = []
            for x in range(self.width):
                next_row.append(self.apply(self._get_neighbors(x, y), self.generations[-1][y][x]))
            next_generation.append(next_row)

        return next_generation

    def _get_neighbors(self, x: int, y: int) -> dict[tuple[int, int], float]:
        neighbors = {}
        for neighbor in self.neighbors:
            dx, dy = neighbor
            neighbors[neighbor] = self.generations[-1][(y + dy) % self.width][(x + dx) % self.width]

        return neighbors
