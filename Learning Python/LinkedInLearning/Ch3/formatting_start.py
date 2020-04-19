#
# Example file for formatting time and date output
#

from datetime import datetime
from time import strftime
from _datetime import date

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()
    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y"))  #4 digit year
    print(now.strftime("The current year is: %y"))  #2 digit year
    print(now.strftime("The current month is: %B")) #full spelling of month
    print(now.strftime("The current month is: %b")) #abbreviated month
    print(now.strftime("The current day is: %D"))   #full date mm/dd/yyyy
    print(now.strftime("The current day is: %d"))   #day of the month only
    print(now.strftime("The current day is: %a"))   #abbreviated weekday
    print(now.strftime("The current day is: %A"))   #full weekday spelling
    
    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date: %x"))
    print(now.strftime("Locale time: %X"))
    
    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-hour time: %H:%M"))


if __name__ == "__main__":
    main();
