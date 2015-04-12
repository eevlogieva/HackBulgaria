from fractions import gcd


def lcm(a, b):
        return (a * b) // gcd(a, b)


class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def eq_denominators(self, other):
        denominator = lcm(self.denominator, other.denominator)
        print(denominator)
        self.nominator *= denominator / self.denominator
        other.nominator *= denominator / other.denominator
        self.denominator = denominator
        other.denominator = denominator

    def __eq__(self, other):
        self.eq_denominators(other)
        if self.nominator == other.nominator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __add__(self, other):
        self.eq_denominators(other)
        result = Fraction(self.nominator + other.nominator, self.denominator)
        return result

    def __sub__(self, other):
        self.eq_denominators(other)
        result = Fraction(self.nominator - other.nominator, self.denominator)
        return result

    def __lt__(self, other):
        self.eq_denominators(other)
        return self.nominator < other.nominator

    def __gt__(self, other):
        self.eq_denominators(other)
        return self.nominator > other.nominator
