import orc
import hero
import random


class Fight():
    def __init__(self, hero1, orc1):
        self.hero = hero1
        self.orc = orc1

    def simulate_battle(self):
        attacker = self.attack_first()
        if attacker == self.hero:
            attacked = self.orc
        else:
            attacked = self.hero
        while self.hero.is_alive() and self.orc.is_alive():
            attacked.take_damage(attacker.attack())
            print("The {} took damage {}".format(attacked.name, attacker.attack()))
            attacker, attacked = attacked, attacker

    def attack_first(self):
        first = random.randint(1, 100)
        if first <= 50:
            print("{} is first".format(self.hero.known_as()))
            return self.hero
        else:
            print("{} is first".format(self.orc.name))
            return self.orc
