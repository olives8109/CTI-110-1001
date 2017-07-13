# Debugging - Rewrite #4 on page 115 with proper alignment and indentation.
# CTI-110
# Sigrid Olive
# 6/13/2017

#input test score
score = int(input("What is the test score? "))

#classify the letter grade based on score input
if score >= 90:
    letterGrade = "A"
elif score >= 80:
    letterGrade = "B"
elif score >= 70:
    letterGrade = "C"
elif score >= 60:
    letterGrade = "D"
else:
    letterGrade = "F."
    print ("Grade is below the lowest value checked.")

#print out what the letter grade is
print ("The letter grade is: ", letterGrade)
