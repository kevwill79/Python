"""Using List as Stacks (not in the book)

The list methods make it very easy to use a list as a stack, where the last 
element added is the first element retrieved (LIFO - last in first out). To add 
an item to the top of the stack, use append(). To retrieve an item from the top 
of the stack, use pop() without an explicit index."""

stack = [3, 4, 5]
print("Here's the stack:", stack)

stack.append(6)
stack.append(7)
print("Here's the stack after performing append(6) and append(7):", stack)

stack.pop()
print("Here's the stack after performing pop():", stack)

stack.pop()
stack.pop()
print("Here's the stack after performing pop() twice:", stack)