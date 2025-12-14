import random
import textwrap

balance = 3000

def updt_bal(balance, gambleamt, gambleres):
    balance -= gambleamt

    if gambleres==1:
        balance += gambleamt*2
    return balance

#Gambling logic
def sgamble(balance, gambleamt, gambleno):
    jackno = random.randint(0,5)

    if(jackno==gambleno):
        print("Congratulations you won the jackpot!!")
        print(f"Your gambled ${gambleamt} is doubled!!")
        balance = updt_bal(balance, gambleamt, 1)
    else:
        print(f"Oops, No luck!\nYou lost ${gambleamt} :(")
        print(f"Jackpot number was: {jackno}")
        balance = updt_bal(balance, gambleamt, 0)
    return balance

#User inputs
name = str(input("Enter your name: "))
print(f"Welcome to gambling games, {name}.")
print("Note: It's always recommended to check account balance before starting a gamble.")
while True:
    print("""\n|====->Menu<-====|\n1. Choose a gambling game.\n2. Check account balance\n3. Exit""", end="\n")
    main_ch= int(input("Enter your choice: "))

#main options choice
    match main_ch:
        case 1:
        #Game selection
            while True:
                print("""\n|====->Games Menu<-====|\n1. Jackpot number gambling.\n2. Exit""", end="\n")
                game_choice = int(input("Enter your choice: "))
                match game_choice:
                    case 1:
                    #Base choice
                        print("\nRule: Maximum amount of $500/gamble can be invested in this game.")
                        while True:
                            print("\n1. How to play\n2. Start\n3. Exit")
                            action_choice = int(input("Enter your choice: "))
                            match action_choice:
                                case 1:
                                    print(textwrap.dedent("""
                                                        ++==++jackpot number game guide++==++
                                                        1. Enter a number in given range (1-5),
                                                        2. Enter amount to be gambled,
                                                        3. If the number you entered is the jackpot number your invested amount is doubled,
                                                        4. Continue playing or exit the game.\n"""))
                                case 2:
                                    while(1):
                                       gambleamt = int(input("\nEnter amount of money you want to gamble: "))
                                       if gambleamt > balance:
                                            print("Insufficient balance.")
                                            continue
                                       if(gambleamt>500):
                                            print("Invalid!, remember the rule: you cant gamble more than $500/gamble")
                                            continue
                                       else:
                                            break
                                           
                                    print("\nJackpot number is between 0-5 (0&5 included)")
                                    while(1):
                                        gambleno = int(input("Guess the jackpot number: "))
                                        if gambleno<0 or gambleno>5:
                                            print("Invalid guess")
                                            continue 
                                        else:
                                            break
                                    balance = sgamble(balance, gambleamt, gambleno)
                                case 3:
                                    print("Bye have a nice day! :D")
                                    break
                                case _:
                                    print("Invalid choice, Please select between 1-3")
                    case 2:
                        print("More games coming soon stay tuned!")
                        break
                    case _:
                        print("Invalid choice, Please select between 1-2")

        case 2:
            print(f"\nBalance = ${balance}")
        case 3:
            print("Hoping to see you again ^-^")
            break
        case _:
            print("Invalid choice, Please select between 1-3")
