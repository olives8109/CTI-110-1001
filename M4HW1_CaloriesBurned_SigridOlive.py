# Calories Burned - Calculates the number of calories burned at a rate of burning 4.2 calories per minute.
# CTI-110
# Sigrid Olive
# 6/15/2017

#explains what program does
print("This program displays the number of calories burned at a rate of 4.2.")
print("\n")

totalCalories = 0.0 #total calories burned
totalMinutes = 0.0 # total minutes 
startTime = 10 # intial start time
endTime = 35 # end time (5 minutes after 30, so it stops at 30)
increment = 5 # increments of 5 minutes

# table heading
print('Minutes Exercised \tCalories Burned')
print('----------------------------------------')

# calculates total number of calories burned after an input of minutes spent exercising
for minutes in range (startTime, endTime, increment):
    rate = 4.2
    caloriesBurned = rate * minutes
    print(minutes, '\t \t \t', format(caloriesBurned,'.1F'))
    totalCalories += caloriesBurned
    totalMinutes += minutes

# prints the number of calories burned after inputing the number of minutes spent exercising
print("\n")
print( "After", totalMinutes, "minutes of exercise,", totalCalories, "calories were burned.")
