import numpy as np

from ._handlers import RuleHandler


class CellularAutomaton1D:
    def __init__(self, rule: int, init: list[int] = None, width: int = 100):
        self._rule = rule
        self._width = width

        self.generations = []

        if init is None:
            fill = width - 1
            self.generations.append(np.pad([1], (fill // 2, fill // 2 + (1 if fill % 2 == 1 else 0))))
        else:
            if len(init) < width:
                fill = width - len(init)
                self.generations.append(np.pad(init, (fill // 2, fill // 2 + (1 if fill % 2 == 1 else 0))))
            elif len(init) > width:
                raise Exception("length of given initial state bigger than given width (default width is 100)")
            else:
                self.generations.append(init)

        self._handler = RuleHandler(rule)

    def next(self) -> list[int]:
        next_generation = []
        for i in range(self._width):
            if i == self._width - 1:
                state = f"{self.generations[-1][i - 1]}{self.generations[-1][i]}{self.generations[-1][0]}"
            else:
                state = f"{self.generations[-1][i - 1]}{self.generations[-1][i]}{self.generations[-1][i + 1]}"

            next_generation.append(int(self._handler.states[state]))

        self.generations.append(next_generation)
        return self.generations[-1]

    def run(self, generations: int) -> list[int]:
        for _ in range(generations):
            self.next()

        return self.generations[-1]
