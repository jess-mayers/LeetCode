def linear_search(l: list, target: int) -> int:
    for i, v in enumerate(l):
        if v == target:
            return i
    # not found
    return -1
