import random, time
print ("Welcome to the Jersey Cash 5!")
print ("Your numbers will be chosen automatically")
print ("Good Luck!")
def z():
    lottery = []
    flag = "n"
    while len(lottery) < 5:
        y = random.randint(1, 38)
        for aNumbers in (lottery):
            if aNumbers == y:
                flag = "y"
                break
        if flag == "n":
            time.sleep(1.00)
            lottery.append(y)
            print(lottery)
        if flag == "y":
            del lottery[-1]
            flag = "n"

    print("These are the Cash 5 numbers: \n", "    ", *lottery)

    print("Would you like to play again?")

z()



def u():
        h = input("Yes or No:")
        if h == ("Yes"):
            print ("Restarting Program...")
            z()
        if h == ("No"):
            print ("The program will now exit...")
        else:
            u()
u()






