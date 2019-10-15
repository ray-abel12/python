print ("welcome choice between 1.rock 2.paper and 3.scissor ")

player1 = input("please enter player one choice ")
player2 = input("please enter player two choice ")
print ("shoot!")

if player1 == "rock" and player2 == "paper":
    print ("player one wins")
elif player1 == "paper" and player2=="rock":
    print ("player two wins")
elif player1 == "paper" and player2=="scissor":
    print ("player two wins")
elif player1 == "scissor" and player2=="rock":
    print ("player one wins")
elif player1 == "rock" and player2=="scissor":
    print ("player two wins")
elif player1 == player2:
    print ("no winner tie")
else :
    print("invalid entry")
    

