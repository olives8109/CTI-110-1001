# Age Classifier - Classifies a person as an infant, a child, a teenager, or an adult based on age.
# CTI-110
# Sigrid Olive
# 06/12/2017

#input a person's age
age = float(input("How old is the person? "))

#classifies the person as an infant, a child, a teenager, or an adult
if (age <= 1):
    print("The person is an infant. ")
elif (age <= 13):
        print("The person is a child. ")
elif (age < 20 ):
        print("The person is a teenager. ")
else:
    print("The person is an adult. ")
            
