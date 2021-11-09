def addfunction(int1, int2):
    return int1 + int2


def subfunction(int1, int2):
    return int1 - int2


def demoaddfunction():
    return print('Addition function not ready\n')


def demosubfunction():
    return 1
    print('Subtraction function not ready\n')

print('Calculator programme\n')
while 1:
    input1 = input('Enter first number:')
    input2 = input('Enter second number:')
    input3 = input('Enter operator (1 for +, 2 for -)')
    if int(input3) == 1:
        demoaddfunction()
    elif int(input3) == 2:
        demosubfunction()
