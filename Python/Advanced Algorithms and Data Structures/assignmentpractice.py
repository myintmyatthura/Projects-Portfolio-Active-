"""
Adjacency Matrix should be used when there are many edges (complete/almost complete) between the nodes.
Adjacency List should be used when there are little edges (not complete) connection between the nodes.         

"""
import time
from min_heap import *

class Cars:
    def __init__(self,name,weight) -> None:
        self.name = name
        self.weight = weight
        
    def __str__(self):
        return f"The minimum is Name:{self.name}, Weight:{self.weight}"
    
if __name__ == "__main__":
    car1 = Cars("Johnny",12)
    car2 = Cars("Kevin",15)
    car3 = Cars("Lily",3)
    car4 = Cars("KK",1)
    heap = MinHeap(6)
    heap.add(car2,2)
    if heap.peek_min_key() > 1:
        heap.get_min()
        heap.add(car4,1)
    print(heap.get_min())
        
    