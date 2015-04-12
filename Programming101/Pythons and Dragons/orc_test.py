import orc
import weapon
import unittest


class OrcTest(unittest.TestCase):
    def setUp(self):
        self.orc_master = orc.Orc("OrcMaster", 100, 1.5)

    def test_init(self):
        self.assertEqual(self.orc_master.name, "OrcMaster")
        self.assertEqual(self.orc_master.health, 100)
        self.assertEqual(self.orc_master.berserk_factor, 1.5)

    def test_init_berserk_out_of_range_greater(self):
        an_orc = orc.Orc("Trebblin", 100, 3.4)
        self.assertEqual(an_orc.berserk_factor, 2)

    def test_init_berserk_out_of_range(self):
        an_orc = orc.Orc("Trebblin", 100, -4.3)
        self.assertEqual(an_orc.berserk_factor, 1)

    def test_attack(self):
        an_orc = orc.Orc("Trebblin", 100, 1.5)
        axe = weapon.Weapon("Axe", 32, 0.3)
        an_orc.equip_weapon(axe)
        self.assertEqual(an_orc.attack(), 32 * 1.5)

if __name__ == '__main__':
    unittest.main()
