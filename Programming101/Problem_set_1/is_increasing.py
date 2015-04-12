def is_increasing(seq):
    original = []
    for digit in seq:
        original.append(digit)
    seq.sort()
    print(original)
    print(seq)
    return seq == original and seq[0] != seq[len(seq) - 1]
print(is_increasing([1, 1, 1, 1, 1]))
