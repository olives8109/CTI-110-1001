#Body Mass Index - Calculates a person's body mass index and identifies the person as optimal, underweight, or overweight.
# CTI-110
# Sigrid Olive
# 06/12/2017

#
print("This program calculates a person's body mass index.")

#input weight in pounds
weight = float(input("Enter the person's body weight in pounds: "))

#input height in inches
height = float(input("Enter the person's height in inches: "))

#calculates the body mass index (BMI)
BMI = weight * (703/(height * height))
print ("The person's body mass index is: ", BMI)

#identifies person as optimal, underweight or overweight
if (BMI < 18.5):
        print("The person is underweight.")
else:
    if (BMI > 25):
        print("The person is overweight.")
    else: print("The person's weight is considered optimal.")



