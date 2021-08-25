import numpy as np

from ._handlers import RuleHandler


class CellularAutomaton1D:
    def __init__(self, rule: int, init: list[int] = None, width: int = 100, num_states: int = 2):
        if num_states < 2 or num_states > 36:
            raise ValueError("only numbers of states between 2 and 36 are allowed")

        self._handler = RuleHandler(rule, num_states)
        self._width = width
        self._num_states = num_states
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
        next_generation = []
        for i in range(self._width):
            left = np.base_repr(self.generations[-1][i - 1], base=self._num_states)
            center = np.base_repr(self.generations[-1][i], base=self._num_states)

            if i == self._width - 1:
                right = np.base_repr(self.generations[-1][0], base=self._num_states)
            else:
                right = np.base_repr(self.generations[-1][i + 1], base=self._num_states)

            state = f"{left}{center}{right}"

            next_generation.append(int(self._handler.states[state], base=self._num_states))

        self.generations.append(next_generation)
        return self.generations[-1]

    def run(self, generations: int) -> list[int]:
        for _ in range(generations):
            self.next()

        return self.generations[-1]
