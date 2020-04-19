#
# Example file for working with date information
#

from datetime import date
from datetime import datetime
from datetime import time

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is:", today)

    # print out the date's individual components
    print("Date components:", today.month, today.day, today.year)
    
    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday # is:", today.weekday())
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    print("Today which is a: ", days[today.weekday()])
     
    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print(today)
    t = datetime.time(datetime.now())
    print(t)
    
    
    # Get the current time


  
if __name__ == "__main__":
    main();