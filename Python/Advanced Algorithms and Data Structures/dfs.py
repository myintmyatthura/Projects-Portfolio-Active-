"""
note that BFS is not unique, ABC can also be ACB
Complexity O(V+E) because each vertex is visited 
Each edge is visited twice
Space Complexity is O(V+E)
USES A QUEUE
"""
from typing import Generic, TypeVar
from referential_array import ArrayR, T
from stack_adt import Stack
from queue_adt import Queue

class Graph:
    def __init__(self, v:int):
        # array
        self.vertices =[None]*v
        #[None,None,None,None,None]
    
    def add_vertex(self,vertex):
        new_vertex = Vertex(vertex)
        for space in range(len(self.vertices)):
            if self.vertices[space] is None:
                self.vertices[space]=new_vertex
                return    
        raise ValueError("Ran out of Space in Graph")
        
    def add_edge(self,vertex_a,vertex_b,weight):
        # remember to add a validation method
        v_a = self.get_vertex(vertex_a)
        new_edge = Edge(vertex_a,vertex_b,weight)
        v_a.edges.append(new_edge)
        
        
        
        
    def get_vertex(self, id):
        for vertex in self.vertices:
            if vertex is not None and vertex.id == id:
                return vertex
        return None

        
    def dfs(self, source):
        stack = Stack()
        stack.push(source)
        visited = Stack()
        print("Depth First Search: ", end="")
        while not stack.is_empty():
            current_vertex = stack.pop()
            if current_vertex not in visited.items:
                visited.push(current_vertex)
                print(f"{current_vertex}",end=",")
                for edge in current_vertex.edges:
                    neighbor = self.get_vertex(edge.v)
                    if neighbor not in visited.items:
                        stack.push(neighbor)
    
    def __str__(self):
        return_string = ""
        for vertex in self.vertices: 
            if vertex is not None:
            # printing each vertex in the list
                return_string = return_string+"Vertex "+str(vertex) + " has edges: "
                for edge in vertex.edges:
                    return_string += str(edge) + " "
                return_string += "\n"
        return return_string
        
            
            

class Vertex:
    def __init__(self,id):
        # list
        self.id = id
        self.edges = []
        # for traversal
        self.discovered = False
        self.visited = False
    def __str__(self):
        return_string = str(self.id)
        return return_string
    def added_to_queue(self):
        self.discovered = True
    def visit_node(self):
        self.visited = True

class Edge:
    def __init__(self, u,v,w):
        self.u = u
        self.v = v
        self.w = w
    def __str__(self):
        return f"[{self.v}]"

if __name__ == "__main__":
    my_graph = Graph(7)
    my_graph.add_vertex("A")
    my_graph.add_vertex("E")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_vertex("B")
    my_graph.add_edge("A","C",2)
    my_graph.add_edge("C","D",2)
    my_graph.add_edge("D","E",2)
    my_graph.add_edge("A","B",2)
    my_graph.add_edge("B","A",3)
    
    print(my_graph)
    bfs_vertex = my_graph.get_vertex("A")
    
    output = my_graph.dfs(bfs_vertex)
   
    
    
