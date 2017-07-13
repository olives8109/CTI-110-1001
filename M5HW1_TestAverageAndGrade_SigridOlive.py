# Test Average and Grade - Displays a letter grade for each inputed test grade and displays the total average
# CTI-110
# Sigrid Olive
# 6/26/2017

# prints what program does
print("This program will display a letter grade for a test grade and then calculates the average of all test scores inputed.")
print("\n")

# call the determine_grade and calc_average funtions
def main():
    score1 = int(input("Enter the first test score: "))
    score2 = int(input("Enter the second test score: "))
    score3 = int(input("Enter the third test score: "))
    score4 = int(input("Enter the fourth test score: ")) 
    score5 = int(input("Enter the fifth test score: "))

    print("The letter grade for the first test is: ", determine_grade(score1))
    print("The letter grade for the second test is: ", determine_grade(score2))
    print("The letter grade for the third test is: ", determine_grade(score3))
    print("The letter grade for the fourth test is: ", determine_grade(score4))
    print("The letter grade for the fifth test is: ", determine_grade(score5))

    average = calc_average(score1, score2, score3, score4, score5)
    print("The average grade for all the test scores is: ", + average) 

# defines the variable "determine_grade" which should accept 5 test scores and calculate the average
def determine_grade(score):
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade
	    
# defines the variable "calc_average" which should give an average of the total test scores
def calc_average(score1, score2, score3, score4, score5):
    total = (score1 + score2 + score3 + score4 + score5)
    return total / 5

main()
