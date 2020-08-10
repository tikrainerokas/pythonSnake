import random
number = random.randint(0,9)
spejimai=0
print ("Welcome to a guessing game ")
guessed_number = input("Choose a number from 0 to 9 ")
while (guessed_number != number):

    if int(guessed_number) < number and not int(guessed_number)+1 == number:
        spejimai+=1
        print ("Your guess was too low")
    if int(guessed_number) > number and not int(guessed_number)-1 == number:
        print ("Your guess was too high")
        spejimai += 1
    if int(guessed_number)+1 == number:
        print ("Your guess was slightly too low")
        spejimai += 1
    if int(guessed_number)-1 == number:
        print ("Your guess was slightly too high")
        spejimai += 1
    guessed_number = input("Choose a number from 0 to 9 ")
    if int(guessed_number) == number:
        print ("You guessed exactly right!")
        spejimai += 1
        print (f"It took {spejimai} attempts for you to guess right 😁")
        break


