x = int(input('Please enter x: '))
y = int(input('Please enter y: '))
operator = input('Do you want to add(+), subtract(-), multiply(*), or divide(/)?: ')

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

# Now that we have defined our relative functions. This is the operational logic of our program.

if operator == 'add' :
    print('Addition of ', x, ' and ', y, ' is ', addition(x, y))
elif operator == 'subtract' :
    print('Subtraction of ', x, ' and ', y, ' is ', subtraction(x, y))
elif operator == 'multiply' :
    print('Multiplication of  of ', x, ' and ', y, ' is ', multiplication(x, y))
elif operator == 'divide':
    print('Addition of ', x, ' and ', y, ' is ', division(x, y))
else:
    print('Operator Gonzo! Try Again')

# print('Addition is ' , addition(4, 4))
# print('Subtraction is ' , subtraction(4, 4))
# print('Multiplication is ' , multiplication(4, 4))
# print('Division is ' , division(4, 4))
