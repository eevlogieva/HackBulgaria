def count_words(arr):
    result = {}
    if not arr:
        return {}
    else:
        result[arr[0]] = 1
        for word in arr[1:]:
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
        return result
