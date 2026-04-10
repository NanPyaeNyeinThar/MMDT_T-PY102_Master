## represent graph as matrix
## undirected graph

class Graph:
    def __init__(self, vertices=None):
        if vertices is None:
            vertices = []
    
        self.vertices = vertices

        #creating 2D matrix
        self.adj_matrix = [[0]*len(vertices) for _ in range (len(vertices))]
        print(self.adj_matrix)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            index1 = self.vertices.index(vertex1)
            index2 = self.vertices.index(vertex2)

            # for undirected graph
            self.adj_matrix[index1][index2] = 1
            self.adj_matrix[index2][index1] = 1

    #display by graph version (print row of matrix)
    def display_graph(self):
        for row in self.adj_matrix:
            print(row)

vertices = ['a', 'b', 'c', 'd']
g = Graph(vertices)
# g.add_edge('a', 'b')
# g.add_edge('a', 'd')
# g.add_edge('b', 'c')    
# g.add_edge('c', 'd')
# print(g.adj_matrix)

g.display_graph()
#                   index2
#               a   b   c   d
#  index1   a  | 0   1   0   1 |
#           b  | 1   0   1   0 |
#           c  | 0   1   0   1 |
#           d  | 1   0   1   0 |   
