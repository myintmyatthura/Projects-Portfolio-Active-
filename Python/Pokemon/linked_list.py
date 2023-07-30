""" Linked-node based implementation of List ADT. """
import node
from node import Node
from abstract_list import List, T, Generic

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class LinkedList(List[T]):
    """ List ADT implemented with linked nodes. """
    def __init__(self, dummy_capacity=1) -> None:
        """ Linked-list object initialiser. """
        super(LinkedList, self).__init__()
        self.head = None

    def clear(self):
        """ Clear the list. """
        # first call clear() for the base class
        super(LinkedList, self).clear()
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item

    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        return node.index(self.head, item)

    def __get_node_at_index(self, index: int) -> node.Node[T]:
        """ Get node object at a given position. """
        if 0 <= index and index < len(self):
            return node.get_node_at_index(self.head, index)
        else:
            raise ValueError('Index out of bounds')

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        try:
            previous_node = self.__get_node_at_index(index-1)
        except ValueError as e:
            if self.is_empty():
                raise ValueError('List is empty')
            elif index == 0:
                item = self.head.item
                self.head = self.head.next
            else:
                raise e
        else:
            item = previous_node.next.item
            previous_node.next = previous_node.next.next
        self.length -= 1
        return item

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        new_node = node.Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.__get_node_at_index(index - 1)
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.length += 1
        
    def __iter__(self):
        return LinkedListIterator(self.head)
        
class LinkedListIterator(Generic[T]):
    def __init__(self,node:Node[T]) -> None:
        self.current = node
        
    def __iter__(self):
        return self
    
    def __next__(self) -> T:
        if self.current is not None:
            item = self.current.item
            self.current = self.current.next
            return item
        else:
            raise StopIteration
        
        
# list_1 = LinkedList(4)
# list_1.insert(0,1)
# list_1.insert(1,2)
# list_1.insert(2,3)
# list_1.insert(3,4)
# # [1,2,3,4]
# it1 = iter(list_1)
# print(next(it1))
# # 1
# print(next(it1))
# # 2
# print(next(it1))
# # 3
# print(next(it1))
# # 4
    


