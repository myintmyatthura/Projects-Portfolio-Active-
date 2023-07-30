class Graph:
    def __init__(self, v) -> None:
        self.vertices = [None] * len(v)
        for i in range(len(v)):
            self.vertices[i] = vertex(v[i])
    def __str__(self):
        return_string =""
        for vertex in self.vertices:
            return_string = return_string + "Vertex " + str(vertex) + "\n"
        return return_string
    def bfs(self, source):
        discovered = []
        discovered.append(source)
        while len(discovered) > 0:
            v = discovered.serve()
            
            
class vertex:
    def __init__(self, id):
        self.id = id
        self.edges = []
    def __str__(self):
        return_string = str(self.id)
        return return_string
class edge:
    def _innit_(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
        
# create a graph with 5 vertices
if __name__ == "__main__":
    vertices = [0,1,2,3,4]
    my_graph = Graph(v=(vertices))
    print(my_graph)
    