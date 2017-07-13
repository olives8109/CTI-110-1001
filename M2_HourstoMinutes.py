# Hours to Minutes
# with formatting
# CTI-110
# Sigrid Olive
# 6/7/2017

#convert minutes to hh:mm format

#input number of minutes
totalMinutes = int(input("Number of minutes: "))

print ("You entered " + str(totalMinutes) + " minutes." )

#calculate hours
hours = totalMinutes // 60
#print ("That is ", hours, " hours.")

#calculates minutes only
minutes = totalMinutes % 60
#print("and ", minutes, " minutes.")

#print output
print ("That is ", hours, "hours", \
       "and ", minutes, " minutes.")
