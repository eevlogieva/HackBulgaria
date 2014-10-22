from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__set_berserk_factor(berserk_factor)

    def __set_berserk_factor(self, berserk_factor):
        if berserk_factor > 1 and berserk_factor < 2:
            self.berserk_factor = berserk_factor
        elif berserk_factor > 2:
            self.berserk_factor = 2
        else:
            self.berserk_factor = 1

    def attack(self):
        return Entity.attack(self) * self.berserk_factor
