import random
def newFuhcIgn(number):
    print('$$'*number*random.randint(1,10))
    if number < 0:
        return
    return newFuhcIgn(number - 1)


print(newFuhcIgn(5))