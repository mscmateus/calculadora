operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for nultiplication
/ for division
''')

number_1 = int(input('Enter yout first number:'))
number_2 = int(input('Enter yout second number:'))

if operation == '+':
   print('{} + {} = '.format(number_1, number_2))
   print(number_1 + number_2)
#Subtraction
elif operation == '-':
   print('{}-{} = '.format(number_1, number_2))
   print(number_1 - number_2)
#Multiplication
elif operation == '*':
   print('{}*{} = '.format(number_1, number_2))
   print(number_1 * number_2)
#Division
elif operation == '/':
   print('{}/{} = '.format(number_1, number_2))
   print(number_1 + number_2)
else:
   print('You have not typed a valid operator, please run the program again.')
