import random
random_number = random.randint(1000,9999)
guessed_number = input("Guess a 4-digit password ")
cow = 0
bull = 0
spejimai =0
print (random_number)
while (str(random_number) != guessed_number):

    if guessed_number[0] == str(random_number)[0]:
        cow += 1
    elif guessed_number[0] == str(random_number)[1] or guessed_number[0] == str(random_number)[2] or guessed_number[0] == str(random_number)[3]:
         bull += 1
    if guessed_number[1] == str(random_number)[1]:
        cow += 1
    elif guessed_number[1] == str(random_number)[0] or guessed_number[1] == str(random_number)[2] or guessed_number[1] == str(random_number)[3]:
        bull += 1
    if guessed_number[2] == str(random_number)[2]:
        cow += 1
    elif guessed_number[2] == str(random_number)[0] or guessed_number[2] == str(random_number)[1] or guessed_number[2] == str(random_number)[3]:
        bull += 1
    if (guessed_number)[3] == str(random_number)[3]:
        cow += 1
    elif guessed_number[3] == str(random_number)[0] or guessed_number[3] == str(random_number)[1] or guessed_number[3] == str(random_number)[2]:
        bull += 1
    print (f"{cow} cows, {bull} bulls")
    spejimai+=1
    bull = 0
    cow = 0
    guessed_number = input("Guess a password again ")
print (f"You won in {spejimai+1} attempts")

