#List Methods practice (not in the book)

list1 = [0, 1, 2, 3, 4]
print("Original list:", list1, "\n")

#Append - add item to the end of the list
list1.append(5)
print("List appended with the number 5:", list1, "\n")

#Extend - extend list by appending all items from the "iterable"
list1.extend("abcde")
print("List extended to include 'abcde:'", list1, "\n")

#Insert - insert an item at a given position
list1.insert(6, 6)
print("Inserted the number 6 at the 6th index:", list1, "\n")

#Remove - remove the first item from the list whose value = arg given
list1.remove(6)
print("Removed the number 6 from the list:", list1, "\n")

#Pop - remove the item at the given postion in the list and return it
#If no index is specified pop() removes and returns the last item in the list
list1.pop(6)
print("Popped the item in the 6th position of the list:", list1, "\n")
list1.pop()
print("Popped the last item in the list:", list1, "\n")

#Clear - removes all items from the list
list1.clear()
print("Cleared the list:", list1, "\n")

#Index - return zero-based index index in the list of the first item whose value
#is equal to arg provided
list1 = ["a", "b", "c", "d", "a", "a"]  
num = list1.index("c")
print("Display the index number of 'c' from the list:", num, "\n")

#Count - return the number of times arg provided appears in the list
num = list1.count("a")
print("Counted the number of times 'a' appears in the list:", num, "\n")

#Sort - sort the items of the list in place
#Has two optional arguments which must be specified as keyword arguments.
list1.sort()
print("Sort the list:", list1, "\n")
list1.sort(key=str.lower, reverse=True)
print("Customized the sorting. key=str.lower and reverse=True:", list1, "\n")

#Reverse - reverse the elements of the list in place
print("Here's the list again:", list1, "\n")
list1.reverse()
print("Here's the list reversed:", list1, "\n")

#Copy - return a shallow copy of the list
list2 = list1.copy()
print("This is list #2, it's just a copy of list #1:", list2, "\n")
    