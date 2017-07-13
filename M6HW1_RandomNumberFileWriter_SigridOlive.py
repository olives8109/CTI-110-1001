# Random Number File Writer - Writes a series of numbers to a file.
# CTI-110
# Sigrid Olive
# 7/5/2017

import random

def main():

    hold_file = int(input("How many random numbers will the file hold? "))
    
    myFile = open("RNFW.txt", "w")
    for line in range(hold_file):
        num = random.randint(1,500)
        myFile.write(str(num) + '\n')
        print(num)

    myFile.close()
main()

