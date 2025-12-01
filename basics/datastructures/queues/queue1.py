from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

print(type(queue))

print(queue)

print(queue.pop())
print(queue.popleft())

print(queue)

while( len(queue)>0 ):
    print(queue.popleft() , end=" ")