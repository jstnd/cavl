import numpy as np

from .rules import Base1DRule


class CellularAutomaton1D:
    def __init__(self, rule: Base1DRule, init: list[int] = None, width: int = 100):
        self._rule = rule
        self._width = width
        self.generations = []

        if init is None:
            a = np.zeros(width, dtype=int)
            a[width // 2] = 1
            self.generations.append(a)
        else:
            if len(init) < width:
                fill = width - len(init)
                self.generations.append(np.pad(init, (fill // 2, fill // 2 + (1 if fill % 2 == 1 else 0))))
            elif len(init) > width:
                raise ValueError("length of given initial state bigger than given width (default width is 100)")
            else:
                self.generations.append(init)

    def next(self) -> list[int]:
        self.generations.append(self._rule.apply(self.generations[-1]))
        return self.generations[-1]

    def run(self, generations: int) -> list[int]:
        for _ in range(generations):
            self.next()

        return self.generations[-1]
