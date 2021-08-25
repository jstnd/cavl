import itertools


def base_permutations(base: int, length: int) -> list[str]:
    digits = "ZYXWVUTSRQPONMLKJIHGFEDCBA9876543210"
    return ["".join(d) for d in itertools.product(digits[36 - base:], repeat=length)]

