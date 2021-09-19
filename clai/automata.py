import math
from typing import Callable, Type, Union

import numpy as np
import numpy.typing as npt


def init(shape: Union[int, tuple[int, int]],
         setting: str = "simple",
         dtype: Type[float] = int, k: int = 2) -> npt.NDArray[float]:
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
    def __init__(self,
                 init: Union[list[float], npt.NDArray[float]],
                 neighbors: list[int],
                 apply: Callable[[list[Union[float, int]]], float]):
        self.generations = [init]
        self.neighbors = neighbors
        self.apply = apply
        self.width = len(init)

    def evolve(self, generations: int = 1) -> None:
        for _ in range(generations):
            next_generation = []
            for i in range(self.width):
                neighbors = []
                left_radius = (len(self.neighbors) - 1) // 2
                right_radius = math.ceil((len(self.neighbors) - 1) / 2)
                for step, j in enumerate(range(-left_radius, right_radius + 1)):
                    neighbors.append(self.generations[-1][(i + j) % self.width] if self.neighbors[step] > 0 else -1)
                next_generation.append(self.apply(neighbors))
            self.generations.append(next_generation)


class CellularAutomaton2D:
    def __init__(self,
                 init: Union[list[list[float]], npt.NDArray[npt.NDArray[float]]],
                 neighbors: list[tuple[int, int]],
                 apply: Callable[[dict[tuple[int, int], float], float], float]):
        self.generations = [init]
        self.neighbors = neighbors
        self.apply = apply
        self.width = len(init[0])
        self.height = len(init)

    def evolve(self, generations: int = 1) -> None:
        for _ in range(generations):
            next_generation = []
            for y in range(self.height):
                next_row = []
                for x in range(self.width):
                    neighbors = {}
                    for neighbor in self.neighbors:
                        dx, dy = neighbor
                        neighbors[neighbor] = self.generations[-1][(y + dy) % self.width][(x + dx) % self.width]
                    next_row.append(self.apply(neighbors, self.generations[-1][y][x]))

                next_generation.append(next_row)

            self.generations.append(next_generation)
