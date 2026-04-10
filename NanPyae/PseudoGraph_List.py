## represent graph as adjacency list
## pseudo graph

#   'a':['b','d'], 
#   'b':['a','c'], 
#   'c':['b','d'], 
#   'd':['a','c'], 


class Graph:
    def __init__(self):
        self.vertices = {}  #dictionary
        self.edges = [] #list   => since we use list, no more 2D matrix

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
            self.edges.append((vertex1, vertex2))

    # def display_graph(self):
    #     for row in self.adj_matrix:
    #         print(row)

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')

g.add_edge('a','b')
g.add_edge('a','d')
g.add_edge('b','c')
g.add_edge('c','d')
print(g.vertices)