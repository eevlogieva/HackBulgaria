from dungeon import Dungeon
import unittest


class DungeonTest(unittest.TestCase):
    def test_init(self):
        dungeon = Dungeon("dungeon_map_1.txt")
        self.assertEqual(dungeon.map, "dungeon_map_1.txt")


if __name__ == '__main__':
    unittest.main()
