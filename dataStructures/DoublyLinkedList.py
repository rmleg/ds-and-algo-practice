""" Doubly Linked List implementation """


class Node:
    # need the value, next Node, prev Node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        # string representation
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        # start with the first node
        # yield each subsequent node until next node is None
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def isEmpty(self):
        if self.head is None:
            return True

    def add_start(self, new_node):
        if self.isEmpty():
            # if the list is empty, just add as first node
            self.head = new_node
        else:
            # add node to start of LinkedList
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, new_node):
        # add node to end of LinkedList
        # if list is empty, just add the node at the start
        if self.isEmpty():
            self.add_start(new_node)

        else:
            # traverse to end of list
            node = self.head
            while node.next is not None:
                # if next is not None, go to next node
                node = node.next
            # next is None, so add the new node here
            new_node.prev = node
            node.next = new_node

    def add_before(self, target_node, new_node):
        # adds a node before an existing node with a specific data value
        # traverse the list until find node with value of target_node
        node = self.head
        if self.isEmpty():
            raise Exception("List is empty!")
        # if it's the first node, add to beginning of list
        if node.data == target_node.data:
            self.add_start(new_node)
            return self.head

        # otherwise, iterate until we find the target_node
        while node.next is not None:
            if node.next.data == target_node.data:
                # add it here
                new_node.next = node.next
                node.next.prev = new_node
                new_node.prev = node
                node.next = new_node
                return self.head
            node = node.next

        # if no target_node found, raise exception
        raise Exception("No Node with '%s' value exists" % target_node.data)

    def add_after(self, target_node, new_node):
        # adds a node after an existing node with a specific data value
        if self.isEmpty():
            raise Exception("List is empty!")

        for node in self:
            if node.data == target_node.data:
                new_node.next = node.next
                node.next.prev = new_node
                node.next = new_node
                new_node.prev = node
                return self.head
        raise Exception("No Node with '%s' value exists" % target_node.data)

    def remove(self, target_node):
        # Remove target_node
        if self.isEmpty():
            raise Exception("Cannot remove a node from an empty list.")
        # Iterate to find target_node in the list
        node = self.head
        if node.data == target_node.data:
            # if it's the first node in the list, also set a new head
            self.head = node.next
            return self.head

        while node.next is not None:
            if node.next.data == target_node.data:
                # reset next so it skips target_node
                node.next = node.next.next
                return self.head
            node = node.next


# list = DoublyLinkedList()
# list.add_start(Node("1"))
# list.add_start(Node("2"))
# list.remove(Node("1"))
# node = Node("1")
# print(list)
# list.add_end(node)
# print(list)
# print(list)
# list.add_before(Node("1"), Node("2"))
# print(list)
# list.add_start(Node("1"))
# print(list)
# list.add_start(Node("2"))
# list.add_start(Node("1"))
# list.remove(Node("1"))
# list.add_end(Node("blue"))
# list.add_end(Node("purple"))
# list.add_before(Node("1"), Node("clear"))
# print("Add 'hello' before 'purple'")
# list.add_before(Node("purple"), Node("hello"))
# print("Add 'world' after 'purple'")
# purple = Node("purple")
# list.add_after(purple, Node("world"))
# print(list)
# list.remove(purple)
# print(list)
