import random
num_win=random.randint(1,100)
guess=1
number=int(input("enter a number 1 or 100"))
game_over=False
while not(game_over) :
    if(number==num_win):
        print(f"hurrah you are winner,the guess time is {guess}")
        game_over=True
    else:
        if(number<num_win):

            print ("low")
            guess+=1
            number=int(input("number again"))
        else:
            print ("high")
            guess+=1
            number=int(input("number again"))
