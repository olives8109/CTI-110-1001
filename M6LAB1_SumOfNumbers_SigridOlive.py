# Sum of Numbers - Reads all of the numbers stored inside "numbers.txt" file and calculates their total.
# CTI-110
# Sigrid Olive
# 7/6/2017

def main():
    myFile = open("numbers.txt", "r")
    total_numbers = 0

    for line in myFile:
        print(line)
        total_numbers += (int(line))

    print("The total of all the numbers in this file is: ", + total_numbers)

main()
