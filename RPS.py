import random
choise = input("Choose rock, paper or scissors ")
choises = 'rock', 'paper', 'scissors'
computer_choise = random.choice(choises)
game_is_over = 0
player = 0
computer = 0
print(f"You choose {choise}")
print (f"Computer choose {computer_choise}")
while (game_is_over == False):
    if choise.upper == computer_choise.upper:
        print ("It's a tie! ")
    elif choise.upper == "ROCK" and computer_choise.upper == "SCISSORS":
        print ("You won!")
        player += 1
    elif choise.upper == "PAPER" and computer_choise.upper == "ROCK":
        print ("You won!")
        player += 1
    elif choise.upper == "SCISSORS" and computer_choise.upper == "PAPER":
        print ("You won!")
        player += 1
    elif choise.upper == "ROCK" and computer_choise.upper == "PAPER":
        print ("Computer won!")
        computer+=1
    elif choise.upper == "PAPER" and computer_choise.upper == "SCISSORS":
        print("Computer won!")
        computer += 1
    else:
        print("Computer won!")
        computer += 1
    print (f"Your score: {player}")
    print (f"Computers score {computer}")

    game = input("Do you want to play again? (Yes,no) ")
    if game.upper == "YES":
        choise = input("Choose rock, paper or scissors ")
    else:
        game_is_over = False