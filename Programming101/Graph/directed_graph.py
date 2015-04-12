class DirectedGraph:
    marked = []

    def __init__(self):
        self.graph = {}

    def add_edge(self, nodeA, nodeB):
        if nodeA in self.graph:
            self.graph[nodeA].append(nodeB)
            if nodeB not in self.graph:
                self.graph[nodeB] = []
        else:
            self.graph[nodeA] = [nodeB]
            self.graph[nodeB] = []

    def get_neighbours_for(self, node):
        return self.graph[node]

    def path_between(self, nodeA, nodeB):
        self.marked.append(nodeA)
        if nodeB in self.graph[nodeA]:
            return True
        if not self.graph[nodeA]:
            return False
        for node in self.graph[nodeA]:
            if node not in self.marked:
                if self.path_between(node, nodeB):
                    return True
                return False
