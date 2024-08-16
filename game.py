#A random numbers game
def prompt_menu():
    import random
    score=10
    randomNumber=random.randint(1,10)
    return score,randomNumber
def game():
    score,randomNumber=prompt_menu()
    while True:
        userInput=int(input('Guess:'))
        if userInput==randomNumber:
            print('You are correct you chose {} and your score is {}'.format(userInput,score))
            break
        else:
            print('Try Again')
            score-=1
    loop()
def loop():
    choice=input('Would you like to have another go? (Y/N)')
    if choice.upper()=='Y':
        game()
    elif choice.upper()=='N':
        print('BYE!')
    
game()