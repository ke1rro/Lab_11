class MyQueue:

    def __init__(self):
        self.elems = []


    def push(self, x: int) -> None:
        self.elems.append(x)

    def pop(self) -> int:
        self.elems.reverse()
        popped_elem = self.elems.pop()
        self.elems.reverse()
        return popped_elem

    def peek(self) -> int:
        self.elems.reverse()
        peeked_elem = self.elems[-1]
        self.elems.reverse()
        return peeked_elem

    def empty(self) -> bool:
        return len(self.elems) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()