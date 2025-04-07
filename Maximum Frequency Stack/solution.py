"""
Lenyk Nikita
Problem: Maximum Frequency Stack
"""

from collections import defaultdict


class Node:
    """
    Node class
    """

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedListStack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, val):
        """
        Pushes the value into stack

        Args:
            val: the value to push
        """
        new_node = Node(val, self.top_node)
        self.top_node = new_node
        self.size += 1

    def pop(self):
        """
        Pops the peek element from the stack

        Returns:
            int: the value of the head
        """
        if self.top_node is None:
            return None
        val = self.top_node.val
        self.top_node = self.top_node.next
        self.size -= 1
        return val

    def peek(self):
        """
        Returns the peek element

        Returns:
            The head value
        """
        return self.top_node.val if self.top_node else None

    def is_empty(self):
        """
        Returns if the stack is empty

        Returns:
            bool: True if empty, False otherwise
        """
        return self.top_node is None

    def __len__(self):
        """
        Returns the size of the stack

        Returns:
            int: the size of the stack
        """
        return self.size


class FreqStack:
    """
    FreqStack class
    """

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(LinkedListStack)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        """
        Pushes the value into stack

        Args:
            val (int): the value to push
        """
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].push(val)

    def pop(self) -> int:
        """
        Pops the peek element from the stack

        Returns:
            int: the value of the head
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if self.group[self.maxfreq].is_empty():
            self.maxfreq -= 1
        return val
