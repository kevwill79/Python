# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
#===============================================================================
# f = "abc"
# print(f)
# 
# # # ERROR: variables of different types cannot be combined
# print("this is a string " + str(123))
#===============================================================================

# Global vs. local variables in functions
def someFunction():
    #To use the global f in the function
    global f
    f = "def"
    print(f)
    
someFunction()
print(f)

#Delete's variable f previous declaration
del f

#Now f is 8. Without f = 8 we would get an error because we deleted f
f = 8
print(f)
