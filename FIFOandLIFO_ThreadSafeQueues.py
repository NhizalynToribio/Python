print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("**** Thread Safe Queues - FIFO & LIFO *****")

import argparse
from queue import LifoQueue, PriorityQueue, Queue
import threading

from random import randint
from time import sleep

from random import choice, randint

from itertools import zip_longest

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel


QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}


def main(args):
    buffer = QUEUE_TYPES[args.queue]()

    producers = [
        Producer(args.producer_speed, buffer, PRODUCTS)
        for _ in range(args.producers)
    ]

    consumers = [
        Consumer(args.consumer_speed, buffer)
        for _ in range(args.consumers)
    ]

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()


