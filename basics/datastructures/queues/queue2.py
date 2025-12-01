from queue import Queue

queue = Queue()

queue.put(1) # enqueue → 1
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)

print(queue)

print(queue.get())  # dequeue → 1
print(queue.get())  # dequeue → 2

print(queue)

while( not queue.empty() ):
    print(queue.get())