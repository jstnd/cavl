import itertools


class RuleHandler:
    def __init__(self, rule: int):
        self.rule = rule

        self._validate_rule()
        self._interpret_rule()

    def get_next_generation(self, current: list[int]) -> list[int]:
        next_generation = []
        for i in range(len(current)):
            if i == len(current) - 1:
                state = f"{current[i - 1]}{current[i]}{current[0]}"
            else:
                state = f"{current[i - 1]}{current[i]}{current[i + 1]}"
            next_generation.append(int(self._states[state]))

        return next_generation

    def _validate_rule(self) -> None:
        if 0 > self.rule > 255:
            raise Exception("invalid rule passed")

    def _interpret_rule(self) -> None:
        perms = ["".join(b) for b in itertools.product("10", repeat=3)]
        binary = f"{self.rule:08b}"
        self._states = {perm: b for perm, b in zip(perms, binary)}
