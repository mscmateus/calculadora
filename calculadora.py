def calculate():
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

   again()

def again():
   calc_again = input('''
Do you want to calculate again?
Please type Y for yes or N for NO.
''')
   if calc_again.upper() == 'Y':
      calculate()
   elif calc_again.upper() == 'N':
      print('See you later.')
   else:
      again()

calculate()