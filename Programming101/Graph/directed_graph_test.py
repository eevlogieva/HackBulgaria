import unittest
from directed_graph import DirectedGraph


class DirectedClassTest(unittest.TestCase):
    def setUp(self):
        self.new_graph = DirectedGraph()

    def test_init(self):
        self.assertEqual(self.new_graph.graph, {})

    def test_add_edge(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.new_graph.add_edge("Petar", "Georgi")
        self.assertEqual(self.new_graph.graph, {"Ivan": ["Petar"], "Petar": ["Georgi"], "Georgi": []})

    def test_get_neighbours(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.new_graph.add_edge("Petar", "Georgi")
        self.assertEqual(self.new_graph.get_neighbours_for("Ivan"), ["Petar"])
        self.assertEqual(self.new_graph.get_neighbours_for("Petar"), ["Georgi"])

    def test_path_between_direct_neighbours(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.assertTrue(self.new_graph.path_between("Ivan", "Petar"))

    def test_path_between_false(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.new_graph.add_edge("Valeri", "Georgi")
        self.assertFalse(self.new_graph.path_between("Ivan", "Dragan"))
        self.assertFalse(self.new_graph.path_between("Ivan", "Georgi"))

    def test_path_between_distant_neighbour(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.new_graph.add_edge("Petar", "Georgi")
        self.assertTrue(self.new_graph.path_between("Ivan", "Georgi"))

    def test_path_between_cycle(self):
        self.new_graph.add_edge("Ivan", "Petar")
        self.new_graph.add_edge("Petar", "Ivan")
        self.assertTrue(self.new_graph.path_between("Petar", "Ivan"))

    def test_path_between_cycles(self):
        self.new_graph.add_edge("1", "2")
        self.new_graph.add_edge("2", "1")
        self.new_graph.add_edge("2", "3")
        self.new_graph.add_edge("3", "2")
        self.new_graph.add_edge("3", "1")
        self.new_graph.add_edge("2", "4")
        self.new_graph.add_edge("4", "2")
        self.new_graph.add_edge("4", "3")
        self.new_graph.add_edge("4", "1")
        self.new_graph.add_edge("3", "5")
        self.assertTrue(self.new_graph.path_between("1", "5"))


if __name__ == '__main__':
    unittest.main()
