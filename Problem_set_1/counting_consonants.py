def count_consonants(string):
    #return len(string) - count_vowels(string)
    string = string.lower()
    consonants = 'bcdfghjklmnpqrstvwxz'
    count = 0
    for letter in string:
        if letter in consonants:
            count += 1
    return count
print(count_consonants("Github is the second best thing, that happened to programmers, after the keyboard!"))
