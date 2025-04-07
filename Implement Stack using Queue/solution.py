class Node:
    """
    Node class
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Queue class
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        """
        Enqueues the value into queue
        """
        new_node = Node(value)
        if not self.front:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """
        Dequeues the peek element from the queue

        Raises:
            IndexError: if index front is None

        Returns:
            the value of the front
        """
        if not self.front:
            raise IndexError()
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return value

    def peek(self):
        """
        Returns the peek element

        Raises:
            IndexError: if front is empty

        Returns:
            The front value
        """
        if not self.front:
            raise IndexError()
        return self.front.value

    def is_empty(self):
        """
        Returns True if the queue is empty

        Returns:
            bool: True if the queue is empty
        """
        return self.size == 0

    def get_size(self):
        """
        Returns the size of the queue

        Returns:
            int: the size of the queue
        """
        return self.size


class MyStack:
    """
    MyStack class
    """

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        """
        Pushes the element into stack
        """
        self.q.enqueue(x)
        for _ in range(self.q.get_size() - 1):
            self.q.enqueue(self.q.dequeue())

    def pop(self) -> int:
        """
        Pops the peek element from the stack
        """
        if self.q.is_empty():
            raise IndexError()
        return self.q.dequeue()

    def top(self) -> int:
        """
        Returns the peek element
        """
        if self.q.is_empty():
            raise IndexError()
        return self.q.peek()

    def empty(self) -> bool:
        """
        Checks if stack is empty
        """
        return self.q.is_empty()
