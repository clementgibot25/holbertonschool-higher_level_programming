#!/usr/bin/python3
"""
Module for a singly linked list with sorted insertion
"""


class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data with type checking"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node with type checking"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class with sorted insertion"""

    def __init__(self):
        """Initialize an empty linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position"""
        new_node = Node(value)

        # If list is empty or new node should be at the beginning
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the node before the point of insertion
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert the new node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """String representation of the linked list"""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
