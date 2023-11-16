#!/usr/bin/env python3
pack = [2,3,4,5,6,7,8,9,10,11] * 4

import random
random.shuffle(pack)

count = 0
dealer_count = 0

def play_blackjack():
    count = 0
    dealer_count = 0
    #Dealer side:
    dealer_current = pack.pop()
    dealer_count += dealer_current
    print ("Dealer have %d" %dealer_count)
    dealer_current = pack.pop()

    for x in range(2):
        current = pack.pop()
        count += current
        if (count > 21 and current == 11):
            print ('Ace rounded to 1')
            count -= 10
        print ("You got %d" %current)
    print ("You have %d points" %count)

    choice = input('Hit? y/n\n')
    while (choice == 'y'):
        current = pack.pop()
        print('You\'ve got: %d' %current)
        count += current
        if (count > 21 and current == 11):
            print ('Ace rounded to 1')
            count -= 10
        if count > 21:
            print('You\'ve lost with %d points' %count)
            break
        elif count == 21:
            print ('Blackjack, %d points' %count)
            break
        else:
            print ('You have %d points' %count)
            choice = input('Hit? y/n\n')
    if choice == 'n':
        print('You ended the game with %d ponts' %count)
    if (dealer_count == 21 and count == 21):
        print ("Draw, two blackjacks")
    elif (count > 21):
        pass
    else:
        dealer_count += dealer_current
        print ("Dealer secret card was %d" %dealer_current)
        print ("Dealer have %d" %dealer_count)
        while (dealer_count < 17):
            dealer_current = pack.pop()
            dealer_count += dealer_current
            print ("Dealer took %d" %dealer_current)
            print ("Dealer have %d" %dealer_count)
        if (dealer_count == count):
            print ("It's a draw")
        elif (dealer_count > 21):
            print ("You won, because dealer is over 21")
        elif (21-dealer_count < 21-count):
            print ("You lost beacouse dealer is closer")
        else:
            print ("You won, because you are closer")

if __name__ == "__main__":
    while True:
        match input('Play blackjack? '):
            case 'y':
                play_blackjack()
            case 'n':
                print ('See Ya')
                break
            case _:
                print('Invalid input!')