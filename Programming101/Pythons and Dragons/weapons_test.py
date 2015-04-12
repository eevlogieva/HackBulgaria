import weapon
import unittest


class WeaponTest(unittest.TestCase):
    def test_init(self):
        axe = weapon.Weapon("Axe", 23, 0.2)
        self.assertEqual(axe.type, "Axe")
        self.assertEqual(axe.damage, 23)
        self.assertEqual(axe.critical_strike_percent, 0.2)

    def test_incorrect_input(self):
        with self.assertRaises(ValueError):
            weapon.Weapon("Axe", 32, 22)

    def test_critical_hit(self):
        axe = weapon.Weapon("Axe", 23, 0.2)
        result = []
        for i in range(1000):
            result.append(axe.critical_hit())
        self.assertTrue(True in result)
        self.assertTrue(False in result)


if __name__ == '__main__':
    unittest.main()
