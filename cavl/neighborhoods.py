def moore(radius: int = 1) -> list[tuple[int, int]]:
    neighbors = []
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if x == 0 and y == 0:
                continue
            neighbors.append((x, y))

    return neighbors


def von_neumann(radius: int = 1) -> list[tuple[int, int]]:
    neighbors = []
    for i, y in enumerate(range(-radius, 1)):  # top half of neighborhood + middle row
        for x in range(-i, i + 1):
            if x == 0 and y == 0:
                continue

            neighbors.append((x, y))

    for i, y in enumerate(range(1, radius + 1), start=-radius + 1):  # bottom half of neighborhood
        for x in range(i, -i + 1):
            neighbors.append((x, y))

    return neighbors
