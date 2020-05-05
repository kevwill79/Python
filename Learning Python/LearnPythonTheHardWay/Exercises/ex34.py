'''Use Lists as Queues (not in the book)

It is also possible to use a list as a queue, where the first element added is 
the first element retrieved (FIFO - first in first out); however, lists are not 
efficient for this purpose. While appends and pops from the end of list are 
fast, doing inserts or pops from the beginning of a list is slow 
(because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to 
have fast appends and pops from both ends.'''

from collections import deque

queue = deque(["Kevin", "Natasha", "Taitiana", "Kira"])
queue.append("Monica")
queue.append("Mike")
print("The queue:", queue)

queue.popleft()
print("The queue after popleft():", queue)

index = queue[2]
print("Printing what's located at queue[2]:", index)

queue.pop()
print("The queue after pop():", queue)