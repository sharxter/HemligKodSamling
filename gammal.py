currency = 2000
menu2 = 0
player = 0
house = 0
from random import randint
from colorama import Fore, Back, Style
#Green for
print("Welcome to memeBank")
print("=====================")
print("Välj det du vill göra")
print("Option 1: withdrawal")
print("Option 2: deposit")
print("Option 3: currency")
print("Option 4: exit")
print("Option 5: Black jack?")
print("Option 6: Rock throwing")


for x in range(1, 11):
    currency = currency - 100 #rent for having bank
    option = int(input("Please choose an option"))

    if option == 1:
        withdrawl = int(input('How much do you want to Withdrawl?:'))
        currency = currency - withdrawl
        print (' Your current currency :', currency)
    elif option == 2:
        deposit = int(input("How much do you want to Deposit"))
        currency = currency + deposit
        print(" Your current currency is", currency)
    elif option ==3:
        print (' Your current currency :', currency)
    elif option == 4:
        input("Thanks for chosing memebank")
    elif option == 5:
        print("Welcome to blackjack")
        print("====================")
        print("Do you want to proceed Y/N?")
        if input("y" or "Y"):
            bet = int(input("How much do you want to bet?")) #Fixa bet amount och att det tar från pengarna
            currency = currency - bet
            print("You have this amount of points", player)
            print("Do you want to stay at this amount or continue")
            print("==============================================")
            print("Option 1: Continue")
            print("Option 2: Stay")
            for x in range(1,10):
                try:
                    option = int(input("Choose a option"))
                except:
                    print("You need to choose an option")
                if option == 1:
                    player = randint(1,11) + player
                    print("====================")
                    print("You have this amount", player)
                    print("====================")
                    if player > 21:
                        print("You've have over 21 points which means you have lost") 
                        player = 0       
                elif option == 2:
                    print("Time for the house to play")
                    house = randint(16,21)
                    print("This is the house score", house)
                    print("This is your score", player)
                    if player > house:
                        print("You've won you're bet will be doubled")
                        currency = bet * 2
                        player = 0
                    elif player < house:
                        print("You've lost")
                        player = 0
        