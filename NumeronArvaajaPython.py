# Numeronarvauspeli, koodi muokaten verkosta
import random

guessesTaken = 0

print('Hei! Mikä on nimesi?')
myName = input()

number = random.randint(1, 20)

print('Pelataan!, ' + myName + ', Arvaa luku 1-20 väliltä?')

while guessesTaken < 6:
    print('Arvaa?')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Arvauksesi on liian pieni')

    if guess > number:
        print('Arvauksesi on liian suuri')

    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Hyvä!!! ' + myName + '! Arvasit ajatukseni ' + guessesTaken + ' Pelottavaa!')

if guess != number:
    number = str(number)
    print('Ei, ikävä kyllä väärä numero' + number)
