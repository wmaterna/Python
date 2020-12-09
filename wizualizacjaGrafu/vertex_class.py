
class Vertex:
    def __init__(self, node):
        self.id = node #label of vertex
        self.adjacent = {} #dicionery key - vertex object, value - cost


    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
