print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")


from collections import deque


class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

