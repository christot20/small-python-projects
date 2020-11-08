from random import randint
counter = 0
randNum = randint (1,12)
print ("The random number is", randNum,)
print ("The While loop method")
while counter <= 12:
    z = randNum * counter
    print (randNum, "*", counter, "=", z)
    counter += 1
print ("")
print ("The For loop method")
for h in range (0,13, 1):
    p = randNum * h
    print(randNum, "*", h, "=", p)
