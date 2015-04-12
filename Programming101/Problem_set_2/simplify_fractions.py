def simplify_fraction(fraction):
    min_el = min(fraction)
    max_el = max(fraction)
    divisors = [1, min_el]
    for item in range(2, min_el-1):
        if min_el % item == 0:
            divisors.append(item)
    for item in divisors:
        if max_el % item == 0:
            min_el //= item
            max_el //= item
    return (min_el, max_el)
print(simplify_fraction((63, 462)))
