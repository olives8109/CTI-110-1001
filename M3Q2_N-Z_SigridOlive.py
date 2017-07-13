# Question M3Q2_N-Z
# CTI-110
# Sigrid Olive
# 6/13/2017

#input temperature of water sample
sample = float(input("What is the temperature of the water sample in Celsius? "))

#classify if sample is ice, liquid water, or steam
if sample <= 0:
    grade = "ICE."
elif sample <= 100:
    grade = "LIQUID WATER."
else:
    grade = "STEAM."

#print out what the type of the sample is
print ("The type of the sample is: ", grade)
