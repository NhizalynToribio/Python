print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")


from queues import Queue

# fifo enqueue statement
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

# fifo dequeue statement
fifo.dequeue()
'1st'
fifo.dequeue()
'2nd'
fifo.dequeue()
'3rd'