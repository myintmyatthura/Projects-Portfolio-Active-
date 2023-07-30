#djikstra
from ast import Tuple
from typing import Generic, TypeVar

from referential_array import ArrayR

T = TypeVar('T')

class MinHeap:
    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        self.length = 0
        self.the_array = [None] * (max(self.MIN_CAPACITY, max_size) + 1)

    def __len__(self) -> int:
        return self.length

    def is_full(self) -> bool:
        return self.length + 1 == len(self.the_array)
    
    def is_empty(self) -> bool:
        return self.length == 0

    def rise(self, k: int) -> None:
        """
        Rise element at index k to its correct position
        :pre: 1 <= k <= self.length
        """
        item = self.the_array[k]
        while k > 1 and item[0] < self.the_array[k // 2][0]:
            self.the_array[k] = self.the_array[k // 2]
            k = k // 2
        self.the_array[k] = item

    def add(self, obj, key) -> bool:
        """
        Swaps elements while rising
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = (key, obj)
        self.rise(self.length)
        return key

    def sink(self, k: int) -> None:
        """ Make the element at index k sink to the correct position.
            :pre: 1 <= k <= self.length
            :complexity: ???
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if item[0] <= self.the_array[min_child][0]:
                break
            self.the_array[k] = self.the_array[min_child]
            k = min_child

        self.the_array[k] = item
    def smallest_child(self, k: int) -> int:
        """
        Returns the index of k's child with smallest key value.
        :pre: 1 <= k <= self.length // 2
        """
        if 2 * k == self.length or \
                self.the_array[2 * k][0] < self.the_array[2 * k + 1][0]:
            return 2 * k
        else:
            return 2 * k + 1
        
    

    def get_min(self):
        """ 
        Remove (and return) the minimum element from the heap.
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.the_array[1] = self.the_array[self.length+1]
            self.sink(1)
        return min_elt[1]
    
    def peek_min_key(self):
        """ 
         the key of the minimum element in the heap without removing it.
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        return min_elt[0]

        


# class MinHeap(Generic[T]):
#     MIN_CAPACITY = 1

#     def __init__(self, max_size: int) -> None:
#         self.length = 0
#         self.the_array = ArrayR(max(self.MIN_CAPACITY, max_size) + 1)

#     def __len__(self) -> int:
#         return self.length

#     def is_full(self) -> bool:
#         return self.length + 1 == len(self.the_array)

#     def rise(self, k: int) -> None:
#         """
#         Rise element at index k to its correct position
#         :pre: 1 <= k <= self.length
#         """
#         item = self.the_array[k]
#         while k > 1 and item < self.the_array[k // 2]:
#             self.the_array[k] = self.the_array[k // 2]
#             k = k // 2
#         self.the_array[k] = item

#     def add(self, element: T) -> bool:
#         """
#         Swaps elements while rising
#         """
#         if self.is_full():
#             raise IndexError

#         self.length += 1
#         self.the_array[self.length] = element
#         self.rise(self.length)

    # def smallest_child(self, k: int) -> int:
    #     """
    #     Returns the index of k's child with smallest value.
    #     :pre: 1 <= k <= self.length // 2
    #     """
        
    #     if 2 * k == self.length or \
    #             self.the_array[2 * k] < self.the_array[2 * k + 1]:
    #         return 2 * k
    #     else:
    #         return 2 * k + 1

#     def sink(self, k: int) -> None:
#         """ Make the element at index k sink to the correct position.
#             :pre: 1 <= k <= self.length
#             :complexity: ???
#         """
#         item = self.the_array[k]

#         while 2 * k <= self.length:
#             min_child = self.smallest_child(k)
#             if item <= self.the_array[min_child]:
#                 break
#             self.the_array[k] = self.the_array[min_child]
#             k = min_child

#         self.the_array[k] = item
        
#     def get_min(self) -> T:
#         """ 
#         Remove (and return) the minimum element from the heap.
#         """
#         if self.length == 0:
#             raise IndexError

#         min_elt = self.the_array[1]
#         self.length -= 1
#         if self.length > 0:
#             self.the_array[1] = self.the_array[self.length+1]
#             self.sink(1)
#         return min_elt
    

if __name__ == '__main__':
    # Create a new min heap with a maximum size of 10
    min_heap = MinHeap(10)

    # Add some elements to the heap
    min_heap.add(5)
    min_heap.add(3)
    min_heap.add(7)
    min_heap.add(1)

    # Test the get_min method
    assert min_heap.get_min() == 1
    assert min_heap.get_min() == 3
    assert min_heap.get_min() == 5
    assert min_heap.get_min() == 7

    # Test the is_full method
    assert not min_heap.is_full()

    # Add more elements to the heap
    for i in range(10):
        min_heap.add(i)

    # Test the is_full method again
    assert min_heap.is_full()

    # Test the get_min method again
    for i in range(10):
        assert min_heap.get_min() == i

    print('All tests passed!')

        
