from bst import BinarySearchTree
from node import TreeNode
import random
import unittest

__author__ = "Saksham Nagpal"


class TestBST(unittest.TestCase):
    """ Testing BST only functionality. """

    def setUp(self):
        self.successor = {}

    def check_invariant(self, current: TreeNode) -> bool:
        if current is not None and current.left is not None:
            # checking the invariant
            self.assertGreater(current.key, current.left.key, 'Invariant does not hold for node {0} as current.key = {1} while current.left.key = {2}'.format(current, current.key, current.left.key))
            # calling for left child
            self.check_invariant(current.left)

        if current is not None and current.right is not None:
            self.assertLess(current.key, current.right.key, 'Invariant does not hold for node {0} as current.key = {1} while current.right.key = {2}'.format(current, current.key, current.right.key))
            # calling for right child
            self.check_invariant(current.right)

        return True

    def testInvariant(self):
        numbers = list(range(1, 100))
        for attempt in range(10):
            random.shuffle(numbers)

            tree = BinarySearchTree()
            self.setUp()  # clearing the cache
            length = random.randint(10, 100)
            for num in numbers[:length]:
                tree[num] = num

            self.assertTrue(self.check_invariant(tree.root), 'The invariant does not hold!')

    def testDelete(self):
        numbers = list(range(1, 100))
        for attempt in range(10):
            random.shuffle(numbers)

            tree = BinarySearchTree()
            self.setUp()  # clearing the cache
            length = random.randint(10, 100)
            sorted_array = []
            for num in numbers[:length]:
                tree[num] = num
                sorted_array.append(num)

            to_delete = numbers[:(length // 2)]
            random.shuffle(to_delete)
            for n in to_delete:
                del tree[n]

            self.assertTrue(self.check_invariant(tree.root), 'The invariant does not hold after node deletion!')

    def testMinimal(self):
        random.seed(16)
        numbers = list(range(1, 100))

        tree = BinarySearchTree()
        self.setUp()  # clearing the cache
        length = random.randint(10, 100)
        sorted_array = []
        for num in numbers[:length]:
            tree[num] = num
            sorted_array.append(num)

        to_delete = numbers[:(length // 2)]
        random.shuffle(to_delete)
        for n in to_delete:
            del tree[n]
        returned_node = tree.get_minimal(tree.root)
        self.assertEqual((returned_node.key, returned_node.item), (29, 29), "Get minimal failed")

    def testSuccessor(self):
        random.seed(16)
        numbers = list(range(1, 100))

        tree = BinarySearchTree()
        self.setUp()  # clearing the cache
        length = random.randint(10, 100)
        sorted_array = []
        for num in numbers[:length]:
            tree[num] = num
            sorted_array.append(num)

        to_delete = numbers[:(length // 2)]
        random.shuffle(to_delete)
        for n in to_delete:
            del tree[n]
        returned_node = tree.get_minimal(tree.root)
        self.assertEqual((returned_node.key, returned_node.item), (29, 29), "Get successor test failed")

    def testInOrder(self):
        numbers = list(range(1, 100))
        for attempt in range(10):
            random.shuffle(numbers)

            tree = BinarySearchTree()
            self.setUp()  # clearing the cache
            length = random.randint(10, 100)
            sorted_array = []
            for num in numbers[:length]:
                tree[num] = num
                sorted_array.append(num)

            sorted_array.sort()  # creating a properly sorted array
            array = [key for key in tree]  # using out treesort

            self.assertEqual(array, sorted_array, 'In-Order traversal produces a wrong order: {0}'.format(array))

if __name__ == "__main__":
    unittest.main()