#
# Example file for working with loops
#

def main():
    x = 0
    
    # define a while loop
    #===========================================================================
    # while(x < 5):
    #     print(x)
    #     x = x + 1
    #===========================================================================
    
    #===========================================================================
    # # define a for loop
    # for x in range(5, 10):
    #     print(x)
    # 
    # # use a for loop over a collection
    # days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    # 
    # for day in days:
    #     print(day) 
    #===========================================================================
    
    # use the break and continue statements
    #===========================================================================
    # for x in range(4, 9):
    #     #if(x == 7): break
    #     
    #     if(x % 2 == 0): continue
    #     
    #     print(x)
    # 
    #===========================================================================
    
    #using the enumerate() function to get index 
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    
    for i, day in enumerate(days):
        print(i, day)

if __name__ == "__main__":
    main()
