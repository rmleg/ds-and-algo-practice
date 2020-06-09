import unittest
from DoublyLinkedList import *


class AddStartTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.list.add_start(Node("1"))

    def tearDown(self):
        self.list = None

    def test_add_start_empty_list(self):
        # Tests adding a node to an empty list
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(str(self.list.head), "1")
        self.assertEqual(self.list.head.next, None)

    def test_add_start(self):
        # Tests adding a node to the start of a list with one node
        self.list.add_start(Node("2"))
        self.assertEqual(str(self.list.head), "2")
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(str(self.list.head.next), "1")
        self.assertEqual(str(self.list.head.next.prev), "2")


class AddEndTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.list.add_end(Node("1"))

    def tearDown(self):
        self.list = None

    def test_add_end_empty_list(self):
        # Tests adding a node to an empty list
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(str(self.list.head), "1")
        self.assertEqual(self.list.head.next, None)

    def test_add_end(self):
        self.list.add_end(Node("2"))
        print(self.list)
        # Tests adding a node to the end of a list with one other node
        self.assertEqual(str(self.list.head), "1")
        self.assertEqual(str(self.list.head.next), "2")
        self.assertEqual(self.list.head.next.next, None)
        self.assertEqual(str(self.list.head.next.prev), "1")
        self.assertEqual(self.list.head.prev, None)


if __name__ == "__main__":
    unittest.main()
