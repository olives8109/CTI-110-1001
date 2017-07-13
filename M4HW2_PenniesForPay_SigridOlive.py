# PenniesForPay - Calculates amount of money a person earned over a period of time with a salary of one penny a day.
# CTI-110
# Sigrid Olive
# 6/19/2017

# explains what program does
print("This program will calculate the amunt of money a person earns at a salary of one penny per day, doubling the salary each day that passes.")

# ask for number of days
days = int(input("How many days has the person worked? "))
totalEarned = 0

# calculate the total salary earned after a number of days
for days in range(0,days):
    salary = ((2)**days)/100
    print (salary)
    totalEarned += salary

print("The total salary is: ", totalEarned)
