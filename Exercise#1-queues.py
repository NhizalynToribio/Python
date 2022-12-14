print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("************ Stacks And Queues *****************")


# Importing deque And Refactoring
from collections import deque


class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

# FIFO QUEUE TESTING (enqueue and dequeue)
# fifo enqueue statement
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# fifo dequeue statement
print("This section will show the FIFO QUEUE")
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())


# FIFO QUEUE TESTING with for loop
fifo_1 = Queue("1st", "2nd", "3rd")
print("This section will show the FIFO QUEUE")
print("The elements:", len(fifo))

for element in fifo_1:
    print(element)

print("The elements", len(fifo_1))


# Class Queue and Input Statement
print("\nThis section will show the FIFO QUEUE")
user1= input("Enter the first element: ")
user2 = input("Enter the second element: ")
user3 = input("Enter the third element: ")

fifo_2 = Queue(user1, user2, user3)
print("The Elements:", len(fifo_2))
inputnumber = 1

while True:
    for element in fifo_2:
        print("Input No. "f"{inputnumber}:", element)
        inputnumber = inputnumber + 1
    break

print("The Elements:", len(fifo_2))

# Stack Data Type
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# LIFO QUEUE TESTING (for loop)
print("Testing of LIFO QUEUE")
lifo = Stack("1st", "2nd", "3rd")

for element in lifo:
    print("This is the element", element)


# LIFO QUEUE TESTING WITH INPUT
print("Second Test of LIFO QUEUE")
lifo_1= []
# Input element
lifo_input1 = input("Enter the first element: ")
lifo_input2 = input("Enter the second element: ")
lifo_input3 = input("Enter the third element: ")

lifo_1.append(lifo_input1)
lifo_1.append(lifo_input2)
lifo_1.append(lifo_input3)

print("Third Element:" , lifo_1.pop())
print("Second Element:" , lifo_1.pop())
print("First Element:" , lifo_1.pop())


# Priority Queue and Heap and Heappush
from heapq import heappush

print("Priority Queue with Head and Heappush (First Test)")
fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print("This is the fruits element list:", fruits)


# Heappush with input statement
print("Second Test of Priority Queue with Heap and Heappush")
fruit_list = []
fruitinput1 = input("Enter the first fruit: ")
fruitinput2 = input("Enter the second fruit: ")
fruitinput3 = input("Enter the third fruit: ")

heappush(fruit_list, fruitinput1)
heappush(fruit_list, fruitinput2)
heappush(fruit_list, fruitinput3)
print("List of fruits:", fruit_list)



# Heappop and showing the output
from heapq import heappop
print("First Test")
print("Fruits from the List: ", heappop(fruits))

print("Final output of First Test in the fruit list: ", fruits)

print("Second Test")
print("Fruits from the List: ", heappop(fruit_list))
print("Final output of Second Test in the fruit list: " , fruit_list)



# Tuples Statement
print("First test in Tuples")
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print("The first person go before the second person:", person1 < person2)
print("The second person go before the third person:", person2 < person3)


# Priority Queue Data Type
from collections import deque
from heapq import heappop, heappush

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)


# PRIORITY QUEUE DATA TYPE
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

print("First Test of Priority Queue Data Type")
messages = PriorityQueue()

messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(" Messages starting at Critical to Neutral")
print("Messages: ", messages.dequeue())

print("Messages: ",messages.dequeue())

print("Messages: ",messages.dequeue())

print("Messages: ",messages.dequeue())


# Corner Cases In the Priority Queue

from collections import deque
from heapq import heappop, heappush
from itertools import count


class PriorityQueue1(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]


# Data Classes
from dataclasses import dataclass


@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

# Messages
messages = PriorityQueue1()

messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))



