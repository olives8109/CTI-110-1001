# Random Number File Reader - Reads a series of numbers in the "RNFW.txt" file.
# Adds up all of the numbers in the file and tells user how many numbers were read.
# CTI-110
# Sigrid Olive
# 7/5/2017

def main():
    myFile = open("RNFW.txt", "r")
    total_num = 0
    total_line = 0

    for line in myFile:
        print(line)
        total_num += (int(line))
        total_line += 1
        
    print("The total of all the numbers in the file is: ", + total_num)
    print("The total number of lines is: ", + total_line)
    
main()
