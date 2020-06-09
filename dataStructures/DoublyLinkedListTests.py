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
        # Tests adding a node to the end of a list with one other node
        self.assertEqual(str(self.list.head), "1")
        self.assertEqual(str(self.list.head.next), "2")
        self.assertEqual(self.list.head.next.next, None)
        self.assertEqual(str(self.list.head.next.prev), "1")
        self.assertEqual(self.list.head.prev, None)


class AddBeforeTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        for i in range(0, 5):
            self.list.add_end(Node(str(i)))

    def tearDown(self):
        self.list = None

    def test_add_before_first_node(self):
        self.list.add_before(Node("0"), Node("new"))
        self.assertEqual(str(self.list.head), "new")
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(str(self.list.head.next), "0")
        self.assertEqual(str(self.list.head.next.prev), "new")

    def test_add_before_middle_node(self):
        self.list.add_before(Node("3"), Node("2.5"))
        # traverse to node '3'
        test_node = None
        for node in self.list:
            if node.data == "3":
                test_node = node
                break
        self.assertEqual(test_node.data, "3")
        self.assertEqual(test_node.prev.data, "2.5")
        self.assertEqual(test_node.prev.next.data, "3")
        self.assertEqual(test_node.prev.prev.data, "2")
        self.assertEqual(test_node.next.data, "4")


class AddAfterTests(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        for i in range(0, 5):
            self.list.add_end(Node(str(i)))

    def tearDown(self):
        self.list = None

    def test_add_after_first_node(self):
        self.list.add_after(Node("0"), Node("0.5"))
        self.assertEqual(self.list.head.data, "0")
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(self.list.head.next.data, "0.5")
        self.assertEqual(self.list.head.next.prev.data, "0")
        self.assertEqual(self.list.head.next.next.data, "1")
        self.assertEqual(self.list.head.next.next.prev.data, "0.5")

    # def test_add_before_middle_node(self):
    #     self.list.add_before(Node("3"), Node("2.5"))
    #     # traverse to node '3'
    #     test_node = None
    #     for node in self.list:
    #         if node.data == "3":
    #             test_node = node
    #             break
    #     self.assertEqual(test_node.data, "3")
    #     self.assertEqual(test_node.prev.data, "2.5")
    #     self.assertEqual(test_node.prev.next.data, "3")
    #     self.assertEqual(test_node.prev.prev.data, "2")
    #     self.assertEqual(test_node.next.data, "4")


if __name__ == "__main__":
    unittest.main()
