def biggest_difference(arr):
    result = []
    for a in arr[0:]:
        for b in arr[a:]:
            result.append(min(a - b, b - a))
    return min(result)
print(biggest_difference(range(100)))
