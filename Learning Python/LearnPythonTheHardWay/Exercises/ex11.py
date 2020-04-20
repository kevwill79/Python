#When using python 3.x add the "end" argument to the print function
#Whatever you provide as the "end" argument is going to be the terminator

print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print("So you are %r old, %r tall, and %r heavy" %(
    age, height, weight))