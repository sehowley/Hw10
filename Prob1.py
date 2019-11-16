##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import matplotlib.pyplot as plt
from datetime import datetime #for formatting dates

'''
I am leaving the organization of this problem largely up to you.
Feel free to break it up into sub-parts or functions as you see
fit. Or don't. Whatever makes the most sense to you. Were I
doing it myself, I'd probably break it up into two functions,
one for reading in the data and doing the data processing
and then one for creating the actual plot, but follow your heart :)

A note and some examples on using datetime.strptime(). It takes
two arguments: both of which are strings. The first in the string
that describes the date and time, and the second is a string that
describes the format of the date. All the formats codes can be 
found by following the link in the HW pdf.

Examples:

    >>> datetime.strptime('11/07/19 4:00', '%m/%d/%y %H:%M')
    datetime.datetime(2019,11,7,4,0)
    >>> datetime.strptime('11-07-2019 5:23:34', '%m-%d-%Y %H:%M:%S')
    datetime.datetime(2019,11,7,5,23,34)


Make sure you use .savefig to save your figure as Conditions.png
at the end of your script (but BEFORE the plt.show()!!).
'''

filename = "Conditions.csv"

def read_data():
    f = open(filename, 'r')
    raw_list = []
    for line in f:
        raw_list.append(line)
