#This is a Guess the Number game.
import random

GussesTaken=0

print('Hello!What is your name?')
myName=input()

number=random.randint(1,5)
print('Well,'+myName+',I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess') #Four spaces in front of "print"
    guess=input()
    guess=int(guess)

    if guess<number: #Eight spaces in front of "print"
        print('Your guess is too low.')
    if guess>number:
        print('Your guess is too hight.')

    if guess==number:
       break

if guess==number:
   guessesTaken=str(guessesTaken+1)
   print('Goodjob,'+myName+'!You guessed my number in '+guessesTaken+' guesses!')

if guess!=number:
   number=str(number)
   print('Nope. The number I was thinking of was'+ number +'.')