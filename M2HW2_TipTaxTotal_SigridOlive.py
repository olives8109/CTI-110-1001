# Tip, Tax, and Total
# Calculate the total cost of a meal purchased by using inputs of tip percentage,sales tax percentage, and cost charge of food.
# CTI-110
# Sigrid Olive
# 6/7/2017

#input meal charge cost
meal = float(input('Enter the cost charge of the meal: '))

#input percentage of tip
tip = float(input('Enter the percentage of the tip (in decimal form): '))

#calculate total of the tip
totalTip = (tip * meal)
print('The total of the tip is: ', totalTip)

#input percentage of sales tax
salesTax = float(input('Enter the percentage of the sales tax (in decimal form): '))

#calculate total of the sales tax
totalSalesTax = (salesTax * meal)
print('The total of the sales tax is: ', totalSalesTax)

#calculate total cost of meal
total = meal + (meal*tip) + (meal*salesTax)

#output total cost of meal
print ('The total cost of the meal is: ', total)



