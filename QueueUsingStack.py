from unittest import TestCase, main

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []
        self._stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self._queue): self._stack.append(self._queue.pop())
        self._queue.append(x)
        while len(self._stack): self._queue.append(self._stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self._queue.pop() if len(self._queue) else None

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._queue[-1] if len(self._queue) else None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self._queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class testQueue(TestCase):
    def test_push(self):
        queue = MyQueue()
        queue.push(1)
        self.assertEqual(queue.peek(), 1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
    
    def test_pop(self):
        queue = MyQueue()
        queue.push(1)
        self.assertEqual(queue.pop(), 1)
        queue.push(2)
        self.assertEqual(queue.peek(), 2)
    
    def test_peek(self):
        queue = MyQueue()
        queue.push(3)
        queue.push(4)
        self.assertEqual(queue.peek(),3)
    
    def test_empty(self):
        queue = MyQueue()
        self.assertTrue(queue.empty())
        queue.push(1)
        self.assertFalse(queue.empty())

if __name__ == "__main__":
    main()
