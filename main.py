import random
def func():
    while True:
        choice = input('1 or 2\n')
        numb = random.randint(1, 2)
        if int(choice) == numb:
            print('You won!')
            quit = input('Want to continue? Y|N\n')
            if quit == 'N':
                break
            elif quit == 'Y':
                True
        else:
            print('You lose')
            quit = input('Want to continue? Y|N\n')
            if quit == 'N':
                break
            elif quit == 'Y':
                True


func()