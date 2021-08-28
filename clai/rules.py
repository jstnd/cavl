from abc import ABC, abstractmethod
from typing import Any

import numpy as np

from ._utils import base_permutations


class _BaseRule(ABC):
    @abstractmethod
    def apply(self, prev_generation: list[Any]) -> list[Any]:
        raise NotImplementedError()


class Base1DRule(_BaseRule, ABC):
    pass


class WolframCodeRule(Base1DRule):
    def __init__(self, rule: int, radius: int = 1, k: int = 2):
        if radius < 0:
            raise ValueError("WolframCodeRule: radius must be 0 or higher")

        if k < 2 or k > 36:
            raise ValueError("WolframCodeRule: only numbers of states between 2 and 36 are supported")

        self._rule = rule
        self._radius = radius
        self._k = k

        self._validate()
        self._interpret()

    def apply(self, prev_generation: list[int]) -> list[int]:
        width = len(prev_generation)

        next_generation = []
        for i in range(width):
            state = []
            for j in range(-self._radius, self._radius + 1):
                state.append(np.base_repr(prev_generation[(i + j) % width], base=self._k))

            next_generation.append(int(self._states["".join(state)], base=self._k))

        return next_generation

    def _validate(self) -> None:
        if self._rule < 0:
            raise ValueError("WolframCodeRule: rule number must not be negative")

        max_rule = self._get_max_rule()
        if self._rule > max_rule:
            raise ValueError(f"WolframCodeRule: rule number {self._rule} is greater than max rule number: {max_rule}")

    def _interpret(self) -> None:
        permutations = base_permutations(self._k, 2 * self._radius + 1)
        converted = np.base_repr(self._rule, base=self._k).zfill(len(permutations))
        self._states = {p: d for p, d in zip(permutations, converted)}

    def _get_max_rule(self) -> int:
        # see https://en.wikipedia.org/wiki/Wolfram_code
        return self._k ** (self._k ** (2 * self._radius + 1))
