import numpy as np

from ._handlers import RuleHandler


class CellularAutomaton1D:
    def __init__(self, rule: int, init: list[int] = None, width: int = 100):
        self._rule = rule
        self._width = width

        if init is None:
            fill = width - 1
            self._board = np.pad([1], (fill // 2, fill // 2 + (1 if fill % 2 == 1 else 0)))
        else:
            if len(init) < width:
                fill = width - len(init)
                self._board = np.pad(init, (fill // 2, fill // 2 + (1 if fill % 2 == 1 else 0)))
            elif len(init) > width:
                raise Exception("length of given initial state bigger than given width (default width is 100)")
            else:
                self._board = init

        self._handler = RuleHandler(rule)

    def next(self) -> list[int]:
        self._board = self._handler.get_next_generation(self._board)
        return self._board

    def run(self, generations: int) -> list[int]:
        for _ in range(generations):
            self.next()

        return self._board
