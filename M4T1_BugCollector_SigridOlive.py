# Bug Collector - Collects total number of bugs over a course of 5 days, then displays the total.
# CTI-110
# Sigrid Olive
# 6/15/2017

# explains what the program does
print("This program calculates the sum of bugs collected over the course of 5 days.")

# initialize an accumulator variable
bugsTotal = 0.0

# get number of bugs collected an add them to the total number
for counter in range (1,6): # range of (6-1) 5 days, can also use just 5
# input number of bugs collected on a day
    bugsCollected = int(input("How many bugs were collected on this day? "))
    bugsTotal = bugsTotal + bugsCollected

# display total number of of bugs collected
print("The total number of bugs collected over the course of 5 days is: ", bugsTotal)
