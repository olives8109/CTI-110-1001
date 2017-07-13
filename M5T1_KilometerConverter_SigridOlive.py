# Kilometer Converter - Converts an input of kilometers into miles
# CTI-110
# Sigrid Olive
# 6/26/2017

# prints what program does
print("This program converts an input of kilometers into miles.")

# defines the variable "kilometers_to_miles" that converts an input of kilometers into miles
def kilometers_to_miles():
    kilometers = int(input("Enter a distance in kilometers: "))
    miles = kilometers * 0.6214
    # prints the output
    print("The number of miles in", + kilometers, "kilometers is: ", + miles)

def main():
    kilometers_to_miles()

main()
