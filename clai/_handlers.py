import numpy as np

from ._utils import base_permutations


class RuleHandler:
    def __init__(self, rule: int, num_states: int):
        self.rule = rule
        self.num_states = num_states

        self._validate_rule()
        self._interpret_rule()

    def _validate_rule(self) -> None:
        if self.rule < 0:
            raise ValueError("rule numbers less than 0 are not allowed")

        max_rule = self._get_max_rule()
        if self.rule > max_rule:
            raise ValueError(f"rule number {self.rule} is greater than max rule number: {max_rule}")

    def _interpret_rule(self) -> None:
        permutations = base_permutations(self.num_states, 3)
        converted = np.base_repr(self.rule, base=self.num_states).zfill(len(permutations))
        self.states = {perm: d for perm, d in zip(permutations, converted)}

    def _get_max_rule(self) -> int:
        # see https://en.wikipedia.org/wiki/Wolfram_code
        return self.num_states ** (self.num_states ** 3)
