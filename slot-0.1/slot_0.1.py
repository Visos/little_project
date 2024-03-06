import random

def deposit():
    amount =  input("how much you want to deposit?")
    while amount.isdigit() == False:
        amount =  input("how much you want to deposit?")
    return amount

def refresh(machine):
    for i  in range (0,3):
        for j in range (0,3):
            machine[i][j] = random.randint(1,4)


def main():
    a = deposit()
    print(a)
    machine[[0,0,0],
            [0,0,0]]
    
    refresh(machine)

    print(machine)

def bet1(money):
    bet = input("how much money do you want to bet?")
    while (bet.isdigit() == False)  or int(bet)> money:
        print("you dont hase so much :(")
        bet =  input("how much money do you want to bet?")
    return bet


def checkwin(machine, number):
    multiplier = 0
    for i in range(0,3):
        for j in range(0,3):
            if machine[i][j] == number:
                multiplier+=1
    return multiplier

def printslot(machine):
    print("==THE SLOT==")
    for i in range(0,3):
        for j in range(0,3):
            if j == 2:
                print(machine[i][j])
            else :
                print(machine[i][j], end="   ")

def main():
    print("WELCOME TO THE SLOT GAME")
    money = int(deposit())
    machine = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
    while(money>0):
        control = input("press 1 to play or any ther key to exit")
        if control != "1":
            break

        printslot(machine)

        number = int(input("what is your lucky number  from 1 to 3?"))


        ##bet
        bet = bet1(money)
        money -= int(bet)

        ##random macine value
        refresh(machine)
        print("REFRESH")
        printslot(machine)

        ## add win to money
        mult = int(checkwin(machine, number))
        print("you won ", int(bet)*mult)
        money += int(bet)*mult
        print("you now have ", money)







    



main()