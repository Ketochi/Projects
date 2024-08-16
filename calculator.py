#This is a simple calculator
def prompt_menu():
    a=float(input('Input the first intger :'))  #a and b would be your first and second numbers
    b=float(input('Input the second integer: '))
    #Present the user with operations and allow them to choose what ooeration to run
    print('What operation wouls you like to carry out\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Root\n7.Division with remainder')
    choice=int(input('What number bears the operation you would like to run? : '))
    return a,b,choice
def calculate():
    a,b,choice=prompt_menu()
    if choice==1:
        print('Sum: {}+{}={}'.format(a,b,a+b))
    elif choice==2:
        print('Difference: {}-{}={}'.format(a,b,a-b))
    elif choice==3:
        print('Product: {}*{}={}'.format(a,b,a*b))
    elif choice==4:
        try:
            print('Quotient: {}/{}={}'.format(a,b,a/b))
        except:
            print('You cannot divide by 0!')
    elif choice==5:
        print('Power: {}^{}={}'.format(a,b,a**b))
    elif choice==6:
        print('Root: {}^(1/{})={}'.format(a,b,round(a**(1/b))))
    elif choice==7:
        try:
            print('Divide with remainder: {}/{}={}. remainder of {}'.format(a,b,a//b,a%b))
        except:
            print('You cannot divide by 0!')
    else:
        print('Inavlid choice!')
    loop()
def loop():
    choice=input('Would you likr to keep calculating?: (Y/N)')
    if choice.upper()=='Y':
        calculate()
    elif choice.upper()=='N':
        print('Okay Good Bye!')
    else:
        print('Invalid Selection!')
    

calculate()