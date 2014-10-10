def is_int_palindrome(n):
    print(len(str(n)))
    half1 = str(n)[0:len(str(n)) // 2]
    if len(str(n)) % 2 == 0:
        half2 = str(n)[len(str(n)):len(str(n)) // 2 - 1:-1]
    else:
        half2 = str(n)[len(str(n)):len(str(n)) // 2:-1]
    return half1 == half2
print(is_int_palindrome(999))
