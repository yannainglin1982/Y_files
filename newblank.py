import sys

def collatz(n):
    while n>1:
        print(n, end=',')
        if (n % 2):
            n = 3*n + 1
        else:
            n = n//2
        print(1,end=' ')

try:
    n = int(input('Enter n: '))
except ValueError:
    print('Please enter a valid INTEGER.')
except NameError(n):
    print('Error')
    print('Try Again!')


playAgain='yes'

while playAgain=='yes' or playAgain=='y':
    sequence=str(collatz(n))
    print('Result:(sequence)')

    break









