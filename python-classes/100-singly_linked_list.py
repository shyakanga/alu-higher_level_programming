#!/usr/bin/python3
"""Module that defines a Node and a SinglyLinkedList class.

This module provides data structures for managing an ordered singly linked
list of integers.
"""


class Node:
    """Represents a node in a singly linked list.

    Attributes:
        __data (int): The integer value stored in the node.
        __next_node (Node or None): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): Value to store in the node.
            next_node (Node or None, optional): Next node reference.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data stored in the node.

        Returns:
            int: The stored integer value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data value with validation.

        Args:
            value (int): The value to store.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the reference to the next node.

        Returns:
            Node or None: The next node or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node reference with validation.

        Args:
            value (Node or None): Reference to the next node.

        Raises:
            TypeError: If value is neither None nor a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list sorted in increasing order."""

    def __init__(self):
        """Initializes an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Defines string representation of the linked list.

        Returns:
            str: Each node data on a new line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node in increasing sorted position.

        Args:
            value (int): Value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
