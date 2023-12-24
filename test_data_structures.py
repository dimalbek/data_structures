import unittest

import data_structures


class TestStaticArray(unittest.TestCase):
    def setUp(self):
        self.array = data_structures.StaticArray(5)

    def test_set_get(self):
        self.array.set(0, 5)
        self.assertEqual(self.array.get(0), 5)

        self.array.set(1, 10)
        self.assertEqual(self.array.get(1), 10)

        self.array.set(4, 20)
        self.assertEqual(self.array.get(4), 20)


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.array = data_structures.DynamicArray()

    def test_append(self):
        self.array.append(5)
        self.assertEqual(self.array.get(0), 5)

    def test_insert(self):
        self.array.insert(0, 5)
        self.assertEqual(self.array.get(0), 5)

    def test_delete(self):
        self.array.append(5)
        self.array.append(10)
        self.array.delete(0)
        self.assertEqual(self.array.get(0), 10)


import unittest


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = data_structures.SinglyLinkedList()

    def test_append(self):
        self.list.append(1)
        self.assertEqual(self.list.get_head().value, 1)
        self.assertEqual(self.list.get_tail().value, 1)

    def test_insert(self):
        self.list.append(1)
        self.list.insert(0, 2)  # Insert at the beginning
        self.assertEqual(self.list.get_head().value, 2)
        self.list.insert(1, 3)  # Insert in the middle
        self.assertEqual(self.list.find(3).value, 3)

    def test_delete(self):
        self.list.append(1)
        self.list.append(2)
        self.list.delete(1)
        self.assertEqual(self.list.get_head().value, 2)

    def test_find(self):
        self.list.append(1)
        self.assertEqual(self.list.find(1).value, 1)

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.append(1)
        self.assertEqual(self.list.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(1)
        self.assertFalse(self.list.is_empty())

    def test_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.reverse()
        self.assertEqual(self.list.get_head().value, 2)
        self.assertEqual(self.list.get_tail().value, 1)


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = data_structures.DoublyLinkedList()

    def test_append(self):
        self.list.append(1)
        self.assertEqual(self.list.get_head().value, 1)
        self.assertEqual(self.list.get_tail().value, 1)

    def test_insert(self):
        self.list.append(1)
        self.list.insert(0, 2)  # Insert at the beginning
        self.assertEqual(self.list.get_head().value, 2)
        self.list.insert(1, 3)  # Insert in the middle
        self.assertEqual(self.list.find(3).value, 3)

    def test_delete(self):
        self.list.append(1)
        self.list.append(2)
        self.list.delete(1)
        self.assertEqual(self.list.get_head().value, 2)

    def test_find(self):
        self.list.append(1)
        self.assertEqual(self.list.find(1).value, 1)

    def test_size(self):
        self.assertEqual(self.list.size(), 0)
        self.list.append(1)
        self.assertEqual(self.list.size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.append(1)
        self.assertFalse(self.list.is_empty())

    def test_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.reverse()
        self.assertEqual(self.list.get_head().value, 2)
        self.assertEqual(self.list.get_tail().value, 1)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = data_structures.Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = data_structures.BinarySearchTree()

    def test_insert_search(self):
        self.bst.insert(5)
        node = self.bst.search(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 5)

    def test_delete(self):
        self.bst.insert(5)
        self.bst.delete(5)
        node = self.bst.search(5)
        self.assertIsNone(node)

    def test_inorder_traversal(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.inorder_traversal(), sorted(values))

    def test_preorder_traversal(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.preorder_traversal(), [5, 3, 2, 4, 7, 6, 8])

    def test_postorder_traversal(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.postorder_traversal(), [2, 4, 3, 6, 8, 7, 5])

    def test_level_order_traversal(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.level_order_traversal(), [5, 3, 7, 2, 4, 6, 8])

    def test_minimum_maximum(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.minimum().value, min(values))
        self.assertEqual(self.bst.maximum().value, max(values))

    def test_size(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.size(), len(values))

    def test_is_empty(self):
        self.assertTrue(self.bst.is_empty())
        self.bst.insert(1)
        self.assertFalse(self.bst.is_empty())

    def test_height(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertEqual(self.bst.height(), 3)

    def test_is_valid_bst(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            self.bst.insert(value)
        self.assertTrue(self.bst.is_valid_bst())


if __name__ == "__main__":
    unittest.main()
