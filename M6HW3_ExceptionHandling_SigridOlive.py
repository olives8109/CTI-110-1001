# Average of Numbers/Exception Handing - Calculates the average of the inetegers
# in the "numbers.txt" file and calculates their average, then handles IOError
# exceptions and ValueError Exceptions.
# CTI110
# Sigrid Olive
# 7/6/2017

def main():

        try:
            
            myFile = open("numbers.txt", "r")
            total_number = 0
            total_line = 0
            total_average = 0

            for line in myFile:
                print(line)
                total_line += 1
                total_number += (int(line))
                total_average = total_number / total_line

            print("\n")
            print("The average of all the numbers in this file is: ", + total_average)
            
        
        except IOError:
            print("\n")
            print("An error occured trying to read the file.")
        except ValueError:
            print("\n")
            print("Non-numeric data found in the file.")
        except:
            print("\n")
            print("An error occured.")
main()
