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
from min_heap import*

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
        v_b = self.get_vertex(vertex_b)
        v_a_edge = Edge(vertex_a,vertex_b,weight)
        v_a.edges.append(v_a_edge)
        v_b_edge = Edge(vertex_b,vertex_a,weight)
        v_b.edges.append(v_b_edge)
        
        
        
        
    def get_vertex(self, id):
        for vertex in self.vertices:
            if vertex is not None and vertex.id == id:
                return vertex
        return None

        
    def bfs(self, source):
        # top list
        queue = Queue()
        queue.append(source)
        # bottom list
        visited = Queue()
        while not queue.is_empty():
            #setting current vertex to the first one in the queuq
            current_vertex = queue.serve()
            #adding the current vertex in the bottom list
            if current_vertex not in visited.items:
                visited.append(current_vertex)
                print(current_vertex)
                for edge in current_vertex.edges:
                    neighbor = self.get_vertex(edge.v)
                    if neighbor not in visited.items:
                        queue.append(neighbor)
                        neighbor.distance = current_vertex.distance + 1
                        neighbor.discovered = True
                        neighbor.previous = current_vertex
                        
    def shortest_path_algorithm_bfs(self,source,end):
        """_summary_
        This algorithm will use backtracking to find the shortest path,
        this algorithm loosely uses BFS.
        Time Complexity - O(V+E)

        Args:
            source (Vertex): The source node
            end (Vertex): The end node
            
        """
        # top list
        discovered = Queue()
        discovered.append(source)
        # bottom list
        visited = Queue()
        while not discovered.is_empty():
            #setting current vertex to the first one in the queuq
            u = discovered.serve()
            u.visit_node()
            #adding the current vertex in the bottom list
            if u.visited != True:
                visited.append(u)
                print(u)
                for edge in u.edges:
                    v = self.get_vertex(edge.v)
                    if v.discovered != True:
                        discovered.append(v)
                        v.distance = u.distance + 1
                        v.added_to_queue()
                        v.previous = u
        current_vertex = end
        shortest_path = Stack()
        while current_vertex != source:
            shortest_path.push(current_vertex)
            current_vertex = current_vertex.previous
        shortest_path.push(source.id)
        length = 0
        print("The shortest path is: ",end="")
        while length != shortest_path.__len__():
            print(f"{str(shortest_path.pop())}",end=",")
            
    def dijkstra(self,source,end):    
        source.distance = 0
        discovered = MinHeap(10)
        discovered.add(source,source.distance)
        while discovered.__len__() > 0:
            u = discovered.get_min()
            u.visited = True
            for attribute in u.edges:
                v = self.get_vertex(attribute.v)
                weight = attribute.w
                if v.discovered == False:
                    v.discovered = True
                    v.distance = u.distance + weight
                    v.previous = u
                    discovered.add(v,v.distance)
                elif v.visited == False:
                    if v.distance > u.distance + weight:
                        v.distance = u.distance + weight
                        v.previous = u
                        discovered.add(v,v.distance)
                        
    def print_shortest_path(self,source, end):
        current_node = end
        if current_node == source:
            print(f"{source.id}",end=",")
            return
        self.print_shortest_path(source,current_node.previous)
        print(f"{current_node.id},", end="")
                        
        # path_stack = Stack()
        # current_node = end # end is like the final destination, source->end
        # while current_node != source:
        #     path_stack.push(current_node.id)
        #     current_node = current_node.previous
        # path_stack.push(source.id)
        # print("Shortest Path Is: ", end="")
        # while not path_stack.is_empty():
        #     node_id = path_stack.pop()
        #     if not path_stack.is_empty():
        #         print(f"{node_id},", end="")
        #     else:
        #         print(node_id)
    
            
                        
                
                    
                    
                
    
        # current_vertex = end
        # shortest_path = Stack()
        # while current_vertex != source:
        #     shortest_path.push(current_vertex)
        #     current_vertex = current_vertex.previous
        # shortest_path.push(source.id)
        # length = 0
        # print("The shortest path is: ",end="")
        # while length != shortest_path.__len__():
        #     print(f"{str(shortest_path.pop())}",end=",")
        
                        
   
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
        # distance
        self.distance = 0
        self.previous = None
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
    def return_edge(self):
        return self.v

if __name__ == "__main__":
    my_graph = Graph(15)
    my_graph.add_vertex("A")
    my_graph.add_vertex("E")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_vertex("B")
    my_graph.add_vertex("F")
    my_graph.add_vertex("G")
    my_graph.add_vertex("I")
    my_graph.add_edge("A","B",10)
    my_graph.add_edge("A","C",5)
    my_graph.add_edge("C","B",3)
    my_graph.add_edge("C","D",9)
    my_graph.add_edge("C","E",2)
    my_graph.add_edge("E","F",25)
    my_graph.add_edge("E","G",10)
    my_graph.add_edge("F","I",40)
    my_graph.add_edge("G","I",80)
    source = my_graph.get_vertex("A")
    end = my_graph.get_vertex("I")
    my_graph.dijkstra(source,end)
    my_graph.print_shortest_path(source,end)

    
    
