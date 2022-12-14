print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("**** Thread Safe Queues - Priority Queue *****")

# importing argparse, LifoQueue, PriorityQueue, Queue and threading
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

from dataclasses import dataclass, field
from enum import IntEnum