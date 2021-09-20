import numpy as np

from ._utils import base_permutations


class General1DRule:
    def __init__(self, rule: int, radius: int = 1, k: int = 2):
        if radius < 0:
            raise ValueError(f"{self.__class__.__name__}: radius must be 0 or higher")

        if k < 2 or k > 36:
            raise ValueError(f"{self.__class__.__name__}: only numbers of states between 2 and 36 are supported")

        self._rule = rule
        self._radius = radius
        self._k = k

        self._validate()
        self._interpret()

        self.neighbors = [1] * (2 * radius + 1)

    def apply(self, neighbors: list[int]) -> int:
        state = "".join(np.base_repr(i, base=self._k) for i in neighbors)
        return int(self._states[state], base=self._k)

    def _validate(self) -> None:
        if self._rule < 0:
            raise ValueError(f"{self.__class__.__name__}: rule number must not be negative")

        max_rule = self._get_max_rule()
        if self._rule > max_rule:
            raise ValueError(f"{self.__class__.__name__}: rule number {self._rule} is greater than max rule number: {max_rule}")

    def _interpret(self) -> None:
        permutations = base_permutations(self._k, 2 * self._radius + 1)
        converted = np.base_repr(self._rule, base=self._k).zfill(len(permutations))
        self._states = {p: d for p, d in zip(permutations, converted)}

    def _get_max_rule(self) -> int:
        # see https://en.wikipedia.org/wiki/Wolfram_code
        return self._k ** (self._k ** (2 * self._radius + 1))


class Totalistic1DRule(General1DRule):
    def apply(self, neighbors: list[int]) -> int:
        total = sum(neighbors)
        return int(self._rule_table[total], base=self._k)

    def _interpret(self) -> None:
        max_total = (self._k - 1) * (2 * self._radius + 1)
        totals = [*range(max_total, -1, -1)]
        converted = np.base_repr(self._rule, base=self._k).zfill(len(totals))
        self._rule_table = {t: d for t, d in zip(totals, converted)}

    def _get_max_rule(self) -> int:
        # see https://mathworld.wolfram.com/TotalisticCellularAutomaton.html
        return self._k ** ((self._k - 1) * (2 * self._radius + 1) + 1)
