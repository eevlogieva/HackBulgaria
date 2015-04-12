def is_an_bn(word):
    if len(word) == 0:
        return True
    count = 0
    index = 0
    while word[index] == 'a':
        count += 1
        index += 1
    while index <= len(word) - 1 and word[index] == 'b':
        count -= 1
        index += 1
    return count == 0
print(is_an_bn("aaabbb"))
