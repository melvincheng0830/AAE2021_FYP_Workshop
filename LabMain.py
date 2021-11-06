def function1():
    print('This text represent the content of function 1') 
    
    
def function2():
    print('This text represent the content of function 2') 


def function3():
    print('This text represent the content of function 3') 


def function4():
    print('This text represent the content of function 4') 


#The Main function
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)
