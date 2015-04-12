def interpret_western_sign(day, month):
    zodiac_signs = [
                    "capricorn", "aquarius", "pisces", "aries",
                    "taurus", "gemini", "cancer", "leo",
                    "virgo", "libra", "scorpio", "sagittarius"
                    ]
    dates_separators = [20, 19, 20, 20, 20, 20, 22, 22, 22, 22, 21, 21]
    if day > dates_separators[month - 1]:
        # here we should return the next month's sign, so sign_index = month
        # but if the month is 12 we want the index
        # to be 0, so we take month % 12
        sign_index = month % 12
    else:
        sign_index = month - 1
    return zodiac_signs[sign_index]


def interpret_chinese_sign(year):
    chinese_zodiac_signs = [
                            "rat", "ox", "tiger", "rabbit", "dragon", "snake",
                            "horse", "sheep", "monkey", "rooster", "dog", "pig"
                            ]
    sign_index = (year - 1900) % 12
    return chinese_zodiac_signs[sign_index]


def interpret_both_signs(day, month, year):
    western = interpret_western_sign(day, month)
    chinese = interpret_chinese_sign(year)
    return (western, chinese)
