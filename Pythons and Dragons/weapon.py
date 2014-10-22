import random


class Weapon():
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        if critical_strike_percent > 1 or critical_strike_percent < 0:
            raise ValueError
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if random.random() > self.critical_strike_percent:
            return True
        return False
