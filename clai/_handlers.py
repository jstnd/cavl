import itertools


class RuleHandler:
    def __init__(self, rule: int):
        self.rule = rule

        self._validate_rule()
        self._interpret_rule()

    def _validate_rule(self) -> None:
        if self.rule < 0 or self.rule > 255:
            raise Exception("invalid rule passed")

    def _interpret_rule(self) -> None:
        perms = ["".join(b) for b in itertools.product("10", repeat=3)]
        binary = f"{self.rule:08b}"
        self.states = {perm: b for perm, b in zip(perms, binary)}
