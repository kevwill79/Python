#
# Example file for working with functions
#

# define a basic function
def funct1():
    print("I am a function")
    
# function that takes arguments
def funct2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x * x * x

# function with default value for an argument
def power(num, x = 1):
    result = 1
    
    for i in range(x):
        result = result * num
    
    return result

#function with variable number of arguments
def multiAdd(*args):
    result = 0
    
    for arg in args:
        result = result + arg
        
    return result

#function with a formal arg list and variable arg list 
#--> var arg list must be last
def multiAdd2(num, *args):
    result = num
    
    for arg in args:
        result = result + arg

    return result
#===============================================================================
# #Just calls funct1
# funct1()
# 
# #Outputs the string and the keyword None --> 
# #because the funct doesn't return a value
# print(funct1())
# 
# #funct is not being executed (no parentheses) 
# #just printing the val of the funct def itself
# print(funct1)
# 
# funct2(10, 20)
# print(funct2(10, 20))
# print(funct2)
#===============================================================================

#===============================================================================
# print(cube(3))
# 
# x = cube(2)
# print(x)
#===============================================================================

#===============================================================================
# print(power(2))
# print(power(2, 3))
# print(power(x = 3, num = 2))
#===============================================================================

print(multiAdd(4, 5, 10, 4))
print(multiAdd(2, 3))

print(multiAdd2(1, 2, 3, 4))
print(multiAdd2(1,))