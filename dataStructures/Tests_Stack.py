import unittest
from Stack import *


class PushTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_single_push(self):
        self.assertEqual(self.stack.head, None)
        self.stack.push(Node("1"))
        self.assertEqual(self.stack.head.data, "1")
        self.assertEqual(self.stack.head.next, None)

    def test_multi_push(self):
        self.stack = Stack()
        for i in range(0, 5):
            self.stack.push(Node(str(i)))
        self.assertEqual(self.stack.head.data, "4")
        self.assertEqual(self.stack.head.next.data, "3")


class PopTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        for i in range(0, 5):
            # push strings 0 through 4 to the stack
            self.stack.push(Node(str(i)))

    def tearDown(self):
        self.stack = None

    def test_multi_pop(self):
        # pop each off and check the order
        self.assertEqual(self.stack.pop().data, "4")
        self.assertEqual(self.stack.pop().data, "3")
        self.assertEqual(self.stack.pop().data, "2")
        self.assertEqual(self.stack.pop().data, "1")
        self.assertEqual(self.stack.pop().data, "0")
        # should raise an exception when stack is empty
        self.assertRaises(Exception, self.stack.pop)


class PeekTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        for i in range(0, 5):
            # push strings 0 through 4 to the stack
            self.stack.push(Node(str(i)))

    def tearDown(self):
        self.stack = None

    def test_peek(self):
        self.assertEqual(self.stack.peek().data, "4")
        self.stack.pop()
        self.assertEqual(self.stack.peek().data, "3")
        # empty the stack
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)


if __name__ == "__main__":
    unittest.main()
