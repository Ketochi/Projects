# BMI calculator
def prompt_menu():
    a=int(input('Input your weignt in Kg:'))
    b=int(input('Input your height in m:'))
    return a,b
def calculator():
    a,b=prompt_menu()
    print('Your weight is {}Kg and your height is {}m\nTherefore your BMI is {}kgm^-2'.format(a,b,a/(b**2)))
    loop()
def loop():
    choice=input('would you like to continue? (Y/N)')
    if choice.upper()=='Y':
        calculator()
    elif choice.upper()=='N':
        print('Okay Bye!')
calculator()