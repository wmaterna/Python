import vertex_class


class Graph:
    def __init__(self):
        self.vert_dict = {} #dictionery of id and vertex object
        self.vert_count = 0  #quantity of vertexes

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.vert_count = self.vert_count + 1
        new_vertex = vertex_class.Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

#for directed graph
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

#for undirected graph
    def add_both_edges(self, key1, key2, value):
        self.add_edge(key1,key2,value)
        self.add_edge(key2, key1,value)
