import unittest
import fight
import orc
import hero
import weapon


class FightTest(unittest.TestCase):
    def setUp(self):
        self.orc_one = orc.Orc("Trebble", 100, 3.4)
        self.hero_one = hero.Hero("Dork", 100, "DragonSlayer")
        self.orc_one.weapon = weapon.Weapon("Axe", 20, 0.2)
        self.hero_one.weapon = weapon.Weapon("Sword", 10, 0.8)
        self.fight_one = fight.Fight(self.hero_one, self.orc_one)

    def test_init(self):
        self.assertEqual(self.fight_one.orc, self.orc_one)
        self.assertEqual(self.fight_one.hero, self.hero_one)

    def test_attack_first(self):
        lst = []
        for i in range(10):
            lst.append(self.fight_one.attack_first())
        self.assertTrue(self.orc_one in lst and self.hero_one in lst)

    def test_end_battle(self):
        self.fight_one.simulate_battle()
        hero_alive = self.fight_one.hero.is_alive()
        orc_alive = self.fight_one.orc.is_alive()
        self.assertTrue((hero_alive and not orc_alive) or (orc_alive and not hero_alive))

    #def test_two_equally_strong_opponents(self):
     #   arr = []
      #  for i in range(50):


if __name__ == '__main__':
    unittest.main()
