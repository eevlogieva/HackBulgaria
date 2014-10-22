import unittest
import fight
import orc
import hero
import weapon


class FightTest(unittest.TestCase):
    def test_init(self):
        orc_one = orc.Orc("Trebble", 100, 3.4)
        hero_one = hero.Hero("Dork", 120, "DragonSlayer")
        fight_one = fight.Fight(hero_one, orc_one)
        self.assertEqual(fight_one.orc, orc_one)
        self.assertEqual(fight_one.hero, hero_one)

    ''''def test_attack_first(self):
        orc_one = orc.Orc("Trebble", 100, 3.4)
        hero_one = hero.Hero("Dork", 120, "DragonSlayer")
        axe = weapon.Weapon("Axe", 20, 1)
        orc_one.equip_weapon(axe)
        sword = weapon.Weapon("Sword", 30, 1)
        hero_one.equip_weapon(sword)
        fight_one = fight.Fight(hero_one, orc_one)
        lst = []
        for i in range(10):
            lst.append(fight_one.attack_first())
        self.assertTrue(orc_one in lst and hero_one in lst)'''

    def test_end_battle(self):
        orc_one = orc.Orc("Trebble", 100, 3.4)
        hero_one = hero.Hero("Dork", 120, "DragonSlayer")
        axe = weapon.Weapon("Axe", 20, 1)
        orc_one.equip_weapon(axe)
        sword = weapon.Weapon("Sword", 30, 1)
        hero_one.equip_weapon(sword)
        fight_one = fight.Fight(hero_one, orc_one)
        fight_one.simulate_battle()
        hero_alive = fight_one.hero.is_alive()
        orc_alive = fight_one.orc.is_alive()
        self.assertTrue((hero_alive and not orc_alive) or (orc_alive and not hero_alive))

if __name__ == '__main__':
    unittest.main()
