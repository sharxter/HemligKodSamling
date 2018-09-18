print("Welcome to memeBank")
print("=====================")
print("Välj det du vill göra")
print("Option 1: withdrawal")
print("Option 2: deposit")
print("Option 3: currency")
print("Option 4: exit")


for x in range(1, 11):
    currency = 2000 - 100 #rent for having bank
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
    elif option ==4: 
        input("Thanks for chosing memebank")
