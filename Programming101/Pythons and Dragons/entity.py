import weapon


class Entity():
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return bool(self.health)

    def take_damage(self, damage_points):
        if damage_points < self.health:
            self.health -= damage_points
        else:
            self.health = 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.health + healing_points >= self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        else:
            self.health += healing_points
        return True

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def equip_weapon(self, weapon1):
        self.weapon = weapon1

    def attack(self):
        if self.weapon is None:
            return 0
        if self.weapon.critical_hit():
            return 2 * self.weapon.damage
        else:
            return self.weapon.damage
