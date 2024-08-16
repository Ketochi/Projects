# craeting a sequence to pick out prime numbers in a range
def prompt_menu():
    a=int(input('Input the starting point of your range '))
    b=int(input('Input the end point of your range '))
    return a,b
def prime():
    a,b = prompt_menu()
    for num in range (a,b+1):
        if num>1:
            for i in range (2,int(num**0.5)+1):
                if num%i==0:
                    break
            else:
                    print(num)
    loop()
def loop():
    choice=input('Would you like to continue :(Y,N)')
    if choice.upper()=='Y':
        prime()
    elif choice.upper()=='N':
        print('Thanks !')
    else:
        print('Invalid Input!')
prime()

