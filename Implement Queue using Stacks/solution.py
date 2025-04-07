"""
Lenyk Nikita
Problem: Implement Queue using Stacks
"""

class Nonde:
    """
    Node class
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Stack class
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        """
        Pushes the value into stack

        Args:
            value: the value to push
        """
        new_node = Nonde(value, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        """
        Pops the peek element from the stack
        Raises:
            IndexError: if index head is None

        Returns:
            Value: the value of the head
        """
        if self.head is None:
            raise IndexError()
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        """
        Returns the peek element

        Raises:
            IndexError: if head is empty

        Returns:
            The head value
        """
        if self.head is None:
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self):
        """
        Checks if stack is empty

        Returns:
            bool: True if empty False Otherwise
        """
        return self.head is None


class MyQueue:
    """
    Queue implementation using 2 stacks
    """
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        """
        Pushes the element into queue

        Args:
            x (int): The value to push into queue
        """
        self.in_stack.push(x)

    def pop(self) -> int:
        """
        Removes and returns the element at the front of the queue.

        Returns:
            int: The front element in FIFO order.
        """
        self.shift_stacks()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Returns the peek of the queue"""
        self._shift_stacks()
        return self.out_stack.peek()

    def empty(self) -> bool:
        """Checks if queue is empty"""
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def _shift_stacks(self):
        """Transfers all elements from `in_stack` to `out_stack` to maintain queue order"""
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())