from counting_words import count_words


def unique_words(arr):
    return len(count_words(arr))
print(unique_words(["apple", "apple", "banana"]))
