"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)

def calFunction(month=None, year=None, *args):
    # If the user doesn't specify any input, your program should print the calendar for the current month. 
    if month is None and year is None:
        print(calendar.month(now.year,now.month,2,1))
    #If the user specifies one argument, assume they passed in a month and render the calendar for that month of the current year.
    elif year is None:
        print(calendar.month(now.year,month,2,1)) 
    # If the user specifies two arguments, assume they passed in both the month and the year. Render the calendar for that month and year.   
    elif month is not None and year is not None and len(args) == 0:
        print(calendar.month(year,month,2,1))
    else:
        print("If no arguments passed in: print the calendar for the current month.")
        print("If one argument passed in: print the calendar for the passed in month for the current year.")
        print("If two argument passed in: print the calendar for the passed in month and year.")
        print("Otherwise show the instructions.")

# Current month
#calFunction()

# Specific Month
#calFunction(8)

# Specific Year and Month
calFunction(8, 2000)

# Instructions
#calFunction(8, 1900, 1)