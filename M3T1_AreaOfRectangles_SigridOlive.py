# Area of Rectangles - Calculates the area of a rectangle.
# CTI-110
# Sigrid Olive
# 06/12/2017


#input length of rectangle 1
l1 = float(input('Enter the length of rectangle 1: '))

#input width of rectangle 1
w1 = float(input('Enter the width of rectangle 1: '))

#input length of rectangle 2
l2 = float(input('Enter the length of rectangle 2: '))

#input width of rectangle 2
w2 = float(input('Enter the width of rectangle 2: '))

#calculates the area of rectangle 1
a1 = l1 * w1
print('The area of rectangle 1 is: ', a1)

#calculates the area of rectangle 2
a2 = l2 * w2
print('The area of rectangle 2 is: ', a2)

#Tells user whether a rectangle has a greater area or if they both have the same area.
if (a1 > a2):
    print ('Retangle 1 has a greater area than Rectangle 2.')
else:
    if (a1 < a2):
        print ('Retangle 2 has a greater area than Rectangle 1.')

    else:
        (a1 == a2)
        print ('Both Retangle 1 and Retangle 2 have the same area.')

    
