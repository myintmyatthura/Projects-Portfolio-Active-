""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev, with edits by Jackson Goerner'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic, List
from node import AVLTreeNode
from linked_stack import LinkedStack
import random

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)
        self.range_counter = -1

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        if current is not None:
            return current.height
        return 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        if current is None:
            return 0
        return self.get_height(current.right) - self.get_height(current.left)

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            PARAMETERS:
            the instances of the AVLTree class
            current[AVLTreeNode]: the tree/sub-tree that the item is added into
            key[K]: the key used to insert the item into the tree/sub-tree
            item[I]: the item that is being added into the tree/subtree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Attempts to insert an item into the tree, it uses the Key to insert it
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [AVLTreeNode]: returns the root of the subtree rooted at current
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(CompK), where CompK is the complexity of comparing the keys. Happens when it inserts the item 
            at the root.

            COMPLEXITY FOR WORST CASE:
            O(CompK * D), where D is the depth of the tree and CompK is the complexity of comparing the keys.
            happens when inserting at the bottom of the tree.
        """
        if current is None:  # base case: at the leaf
            current = AVLTreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        current = self.rebalance(current)
        return current

        #raise NotImplementedError()

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            PARAMETERS:
            the instances of the AVLTree class
            current[AVLTreeNode]: the tree/sub-tree that the item is deleted from
            key[K]: the key used to delete the item from the tree/sub-tree
            item[I]: the item that is being deleted from the tree/subtree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            [AVLTreeNode]: returns the root of the subtree rooted at current
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST CASE:
            O(CompK * D), where CompK is the complexity of comparing the keys and D is the depth of the tree. 
            Happens when it deletes the item at the root.

            COMPLEXITY FOR WORST CASE:
            O(CompK * S), where S is the complexity of get successor (see bst.py) and CompK is the complexity 
            of comparing the keys. Happens when deleting the root of the tree.
        """
        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        current = self.rebalance(current)
        return current
        #raise NotImplementedError()

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            PARAMETERS:
            the instances of the AVLTree class
            current[AVLTreeNode]: the root of the sub-tree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            new_root[AVLTreeNode]: returns the node that is now the root of the sub-tree.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables.
        """
        # basically  take right (even child right first )and put left
        r_child = current.right
        r_subchild = r_child.left
        r_child.left = current
        current.right = r_subchild

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        r_child.height = 1 + max(self.get_height(r_child.left), self.get_height(r_child.right))

        return r_child
        #raise NotImplementedError()

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            PARAMETERS:
            the instances of the AVLTree class
            current[AVLTreeNode]: the root of the sub-tree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            returns the new root of the subtree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            new_root[AVLTreeNode]: returns the node that is now the root of the sub-tree.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(1), does not iterate at all, only assigns values to variables.
        """
        # basically  take left and put right
        l_child = current.left
        l_subchild = l_child.right
        l_child.right = current
        current.left = l_subchild

        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        l_child.height = 1 + max(self.get_height(l_child.left), self.get_height(l_child.right))

        return l_child
        #raise NotImplementedError()


    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
            returns the new root of the subtree.
        """
        if self.get_balance(current) >= 2:
            child = current.right
            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)
            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left
            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)
            return self.right_rotate(current)

        return current

    def range_between(self, i: int, j: int) -> List:
        """
            PRECONDITIONS:
            i and j have to be lesser than the total number of nodes in the AVLTree
            i and j have to be positive integers
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            PARAMETERS:
            the instances of the AVLTree class
            i[integer]: a value from 0 to N - 1, with N being the number of nodes in the tree.
            j[integer]: a value from 0 to N - 1, with N being the number of nodes in the tree.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Returns a sorted list of all elements in the tree between the ith and jth indices, inclusive.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            List: a sorted list of all of the elements in the tree between the ith and jth indices, inclusive.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(comp + T), where comp is the complexity of the comparisons and T is the complexity of range_beteen_aux.
        """
        if j > len(self) or i > len(self):
            raise IndexError("more indices than nodes available")

        if j < 0 or i < 0:
            raise IndexError("negative index not allowed")
        """
        elemList = []
        count = 0
        for index in range(i+1,j+2):
            element = self.range_between_aux(index, self.root, count)
            elemList.append(element[0].item)

        return elemList
        """
        #self.arr = LinkedStack()
        self.range_counter = -1
        return self.range_between_aux(self.root, i, j, [])
    #def range_between_aux(self, index, root, count):
    def range_between_aux(self, current: AVLTreeNode, i, j, elements: list):
        """
            PARAMETERS:
            the instances of the AVLTree class
            current[AVLTreeNode]: the sub-tree/tree that we're currently checking for the smallest element
            i[integer]: a value from 0 to N - 1, with N being the number of nodes in the tree.
            j[integer]: a value from 0 to N - 1, with N being the number of nodes in the tree.
            elements[list]: the list of the smallest elements in the AVLTree.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            METHOD DESCRIPTION:
            Returns a sorted list of all elements in the tree between the ith and jth indices, inclusive.
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            RETURN:
            elements[list]: the auxiliary method returns the list of smallest elements in the AVL Tree
            ...____...___...___...___...____...___...___...___...____...___...___...___...____...___...___...
            COMPLEXITY FOR BEST AND WORST CASE:
            O(j - i + log(N))
        """
        #if a >= i and a <= j
        #print("here")
        if current is not None and self.range_counter <= j:
            #print("a")
            #if self.range_counter > i:
            self.range_between_aux(current.left, i, j, elements)
            self.range_counter += 1
            if i <= self.range_counter <= j:
                elements.append(current.item)
            #self.range_counter >= i:
            self.range_between_aux(current.right, i, j, elements)

        #elements = elements[i:j+1]
        #self.range_counter = -1
        return elements
        """

        if root is None:
            return None, count

        left, count = self.range_between_aux(index, root.left, count)

        if left:
            return left, count

        count += 1
        if count == index:
            return root, count

        return self.range_between_aux(index, root.right, count)
        #if current.key > i + 1:
            #self.range_between_aux(current.left, i, j, elements)


        #if i <= current.key <= j + 1:
            #elements.append(current.item)
        #if current.key < j :
            #self.range_between_aux(current.right, i, j, elements)
        #return elements
        """
"""
random.seed(16)
numbers = list(range(1, 15)) # 1 to 100
print(numbers)
tree = AVLTree()
length = random.randint(10, 12) # 10 to 100
for num in numbers[:length]:
    tree[num] = num
tree.draw()
b = tree.range_between(10,10)
print(b)
"""
