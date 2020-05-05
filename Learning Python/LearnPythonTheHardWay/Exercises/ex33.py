#While-loops

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    
    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)
    
print("The numbers: ")

for num in numbers:
    print(num)
    
#Convert the while-loop to a function call, and replace 6 in the test(i < 6)
print() #just to skip a line

numbers2 = []

def print_numbers(num_range):
    for num in range(num_range):
        print("At the top i is %d" % num)
        numbers2.append(num)
        
        num += 1
        print("Numbers now ", numbers2)
        print("At the bottom i is %d" % num)
        
print("The numbers from the function call: ")
print_numbers(6)

#Add another variable to the function args to get rid of the +1 increment.
#The new arg can be used to control how much the numbers are incremented by

print()

numbers3 = []

def print_numbers_again(num_range, increment_by):
    for num in range(num_range):
        print("At the top i is %d" % (num + increment_by))
        numbers3.append(num + increment_by)
        
        num += increment_by
        
        print("Numbers now ", numbers3)
        print("At the bottom i is %d" % (num + increment_by))
        
print("The numbers from the 2nd function call: ")
print_numbers_again(6, 3)