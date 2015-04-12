import entity
import weapon
import unittest


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.entity = entity.Entity("Troll", 120)

    def test_init(self):
        self.assertEqual(self.entity.name, "Troll")
        self.assertEqual(self.entity.health, 120)

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 120)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage_int(self):
        self.entity.take_damage(10)
        self.assertEqual(self.entity.health, 110)

    def test_take_damage_float(self):
        self.entity.take_damage(10.33)
        self.assertEqual(self.entity.health, 109.67)

    def test_take_damage_greater_than_health(self):
        self.entity.take_damage(120)
        self.assertFalse(self.entity.health)

    def test_take_healing_when_dead(self):
        self.entity.health = 0
        self.assertFalse(self.entity.take_healing(120))

    def test_take_healing_successful(self):
        self.entity.take_damage(80)
        self.assertTrue(self.entity.take_healing(120))
        self.assertEqual(self.entity.health, 120)

    def test_has_weapons(self):
        self.assertFalse(self.entity.has_weapon())

    def test_equip_weapon(self):
        axe = weapon.Weapon("Axe", 23, 0.3)
        self.entity.equip_weapon(axe)
        self.assertTrue(self.entity.has_weapon())
        self.assertEqual(self.entity.weapon, axe)

    def test_disgard_old_weapon(self):
        axe = weapon.Weapon("Axe", 23, 0.3)
        self.entity.equip_weapon(axe)
        sword = weapon.Weapon("Sword", 32, 0.5)
        self.entity.equip_weapon(sword)
        self.assertEqual(self.entity.weapon, sword)

    def test_attack(self):
        axe = weapon.Weapon("Axe", 23, 0.3)
        self.entity.equip_weapon(axe)
        self.assertIn(self.entity.attack(), [23, 46])

    def test_attack_has_no_weapon(self):
        self.assertEqual(self.entity.attack(), 0)

if __name__ == '__main__':
    unittest.main()
