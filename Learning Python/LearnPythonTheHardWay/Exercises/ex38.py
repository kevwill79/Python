#Manipulating lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 thins in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))
    
print("There we go: ", stuff)
print("Let's do some things with stuff.")

print("The first element is: ", stuff[0])
print("The last element is: ", stuff[-1])
print("stuff.pop() gets rid of: ", stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

