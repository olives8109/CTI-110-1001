# Feet to Inches - Converts an input of feet into inches.
# CTI-110
# Sigrid Olive
# 6/26/2017

# explains what program does
print("This program takes a number of feet and gives out the number of inches in that many feet.")

# defines the variable "feet_to_inches" which will take an input of feet and convert it into inches
def feet_to_inches():
    feet = int(input("Enter a number of feet: "))
    inches = feet*12
    print("The number of inches in", + feet,"feet is: ", + inches)

def main():
    feet_to_inches()

main()
