print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")

# queues.py

from collections import deque


class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Second Code
from queues import Queue

# fifo enqueue statement
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# fifo dequeue statement
fifo.dequeue()

fifo.dequeue()

fifo.dequeue()


# Third Code

from collections import deque


class Queue: