import orc
import hero
import random


class Fight():
    def __init__(self, hero1, orc1):
        self.hero = hero1
        self.orc = orc1

    def simulate_battle(self):
        attacker = self.attack_first()
        attacked = [self.hero, self.orc].remove(attacker)

        print(attacked)
        if attacked == self.hero:
            attacker = self.orc
        while self.hero.is_alive() and self.orc.is_alive():
            attacked.take_damage(attacker.attack())
            print("The {} took damage {}".format(attacked, attacker.attack()))
            self.change_turn(attacker, attacked)

    def attack_first(self):
        first = random.randint(1, 100)
        if first <= 50:
            print("{} is first".format(self.hero.attack()))
            return self.hero
        else:
            print("{} is first".format(self.orc.attack()))
            return self.orc

    def change_turn(self, attacker, attacked):
        if attacker == self.hero:
            attacker = self.orc
            attacked = self.hero
        else:
            attacked = self.orc
            attacker = self.hero
