from is_increasing import is_increasing


def is_decreasing(seq):
    return not is_increasing(seq) and seq[0] != seq[len(seq) - 1]
print(is_decreasing([1, 2, 3, 4]))
