'''List Comprehensions (not in book)

List comprehensions provide a concise way to create lists. Common applications 
are to make new lists where each element is the result of some operations 
applied to each member of another sequence or iterable, or to create a 
subsequence of those elements that satisfy a certain condition.'''

squares = []
for x in range(10):
    squares.append(x**2)
    
print("Print 0 - 9 squared:", squares)

#A more concise and readable way
squares = [x**2 for x in range(10)]
print("Print 0-9 squared again:", squares)

'''List Comprehension syntax

[ expression for item in list if conditional ]

A list comprehension consists of brackets containing an expression followed 
by a for clause, then zero or more for or if clauses. The result will be a new 
list resulting from evaluating the expression in the context of the for and if 
clauses which follow it. For example, this listcomp combines the elements of 
two lists if they are not equal:'''