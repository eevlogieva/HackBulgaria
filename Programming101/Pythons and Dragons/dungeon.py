from hero import Hero
from orc import Orc


class Dungeon():
    def __init__(self, filename):
        self.map = filename

    def print_map(self):
        file = open(self.map, 'r')
        content = file.read().split("\n")
        for item in content[:(len(content)-1)]:
            print(item)
        file.close()

    def spawn(self, player_name, entity):
        file = open(self.map, 'r')
        content = file.read().split("\n")
        for item in content[:(len(content)-1)]:
            for char, index in enumerate(item):
                if char == "S":
                    char = "H"
                    item[index] = "H"
                    print(char)
                if char == "S" and entity is Orc:
                    char = "O"
        file.close()
        file = open(self.map, 'w')
        file.write("\n".join(content))
        file.close()


def main():
    map1 = Dungeon("dungeon_map_1.txt")
    orc = Orc("Trebs", 120, 1.5)
    map1.spawn("player_1", orc)
    map1.print_map()

if __name__ == '__main__':
    main()
