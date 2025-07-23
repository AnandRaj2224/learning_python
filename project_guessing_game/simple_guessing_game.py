import random

print("WELCOME STRANGER GUESS THE RIGHT NUMBER AND GET LUCKY (1-10)\n")

player_guess = int(input())
game_over = False

while not game_over:
    random_number = random.randint(1,10)

    if player_guess != random_number:
        player_guess = int(input("WRONG!,FOCUS STRANGER TRY AGAIN\n"))
    else :
        print("congratulations STRANGER U WILL GET LUCKY AFTER MIDNIGHT\n")
        choice = input("DO U WANT TO PLAY AGAIN TO GET MORE LUCKY (Y | N)\n")
        if choice == "N":
            break
        else:
            player_guess = int(input("NEW GUESS\n"))

