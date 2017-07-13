# Hours to Minutes
# with formatting
# CTI-110
# Sigrid Olive
# 6/7/2017

#convert seconds to hh:mm:ss format

#input number of seconds
totalSeconds = int(input("Number of seconds: "))

print ("You entered " + str(totalSeconds) + " seconds." )

#calculate hours
SECONDS_PER_HOUR = 3600;
SECONDS_PER_MINUTE = 60;

hours = totalSeconds // SECONDS_PER_HOUR

#calculates minutes 
minutes = (totalSeconds // SECONDS_PER_MINUTE) % 60

#calculate seconds 
seconds = totalSeconds % 60

#print output
print ("That is ", hours, "hours,", \
        minutes, " minutes,", \
       "and ", seconds, "seconds.")
