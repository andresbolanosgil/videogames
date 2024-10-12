'''escript description number race
dev andres bolaños '''
from random import randint
import os


Status_menu=True


def main_menu():
    global status_opts
    status_opts= True
    print("::: main menu :::")
    print("[1]. Start game")
    print("[2]. Help")
    print("[3]. Exit")
    
    while status_opts:
        opt = int (input("press any option: "))
        if opt<1 or opt > 3:
            print("error.Press any option valid")
        else:
            status_opts=False
        return opt
while Status_menu:    
    os.system('clear')
    op = main_menu()
    if op== 1:
        os.system('clear ')
        print("Welcome to number race:::")
        players = int(input("press number of player[1:4]: "))
        
        print("::: level menu:::")
        print("[1]. Bassic")
        print("[2]. Intermediate")
        print("[3]. Advance")
        print("[4]. Expert")
        opt= int(input("Press any option: "))
        
        if opt== 1:
            pos= 20
        elif opt== 2:
            pos= 30
        elif opt == 3:
            pos=50
        else:
            pos=100
            
        #   Start game
        status_game= True
        roll_count= 0
        roll_acum= 0
        while status_game:
            key= input("Press any key to roll dice ...")
            dice1=randint(1,6)
            dice2=randint(1,6)
            
            print(f"dice 1: {dice1}")
            print(f"dice 2: {dice2}")
            total= dice1 + dice2
            print(f"Total:  {total}")
            
            roll_count += 1
            roll_acum += total

            print(f"Total acum:  {roll_acum}")
            if roll_acum >= pos:
                print("::: You win,congratulations :::")
                status_game= False
            
        print("::: STATICS :::")
        print(f"Total rolls: {roll_count}")
        print(f"Total dices: {roll_acum}")
        key =input("press any key to go to the main menu ...")
    elif op == 2:
        print("Gamen under construction")
        key =input("press any key to go to the main menu ...")
    else:
        print("see you later")    
        key =input("press any key to exit...")
        break
