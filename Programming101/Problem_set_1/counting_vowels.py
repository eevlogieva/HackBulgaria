def count_vowels(string):
    string = string.lower()
    vowels = ['a', 'i', 'e', 'o', 'u', 'y']
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count
print(count_vowels("Python"))
