from LinkedList import *

""" pop - remove item from top of stack
push - add item to top of stack
peek - return item at top of stack
isEmpty - true if stack is empty """


class Stack(LinkedList):
    def push(self, node):
        # add item to top of stack
        self.add_start(node)
        return self.head

    def pop(self):
        # remove item from top of stack
        if self.isEmpty():
            raise Exception("Can't pop from an empty stack.")
        # set head to node.next, return node
        node = self.head
        self.head = node.next
        return node

    def peek(self):
        # return item at top of stack without removing it
        return self.head

