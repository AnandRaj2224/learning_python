print("hello to Rock Paper Scissor Game\n")

player1 = input("enter player 1's choice\n")
player2 = input("enter player 2's choice\n")

if player1 == player2:
    print("its a tie\n")  

elif player1 == 'rock':
    if player2 == 'paper':
        print("paper beats rock ------ player 2 wins !\n")
    elif player2 == 'scissor':
        print("rock beats scissor ------ player 1 wins !\n")

elif player1 == 'paper':
    if player2 == 'rock':
        print("paper beats rock ------ player 1 wins !\n")
    elif player2 == 'scissor':
        print("scissor beats paper ------ player 2 wins !\n")

elif player1 == 'scissor':
    if player2 == 'paper':
        print("scissor beats paper ------ player 1 wins !\n")
    elif player2 == 'rock':
        print("rock beats scissor ------ player 2 wins !\n")
