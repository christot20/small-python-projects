#program gives a times table from 1  to 12 using a for and while loop
print ("While Loop")
ctr = 1   #first counter variable
while ctr <= 12:
    print("") #used to allow for vertical display of numbers
    ctr2 = 1  #second counter which resets before second loop
    while ctr2 <= 12:
        print(ctr2 * ctr, end="\t")  #multiplication with tab for good spacing
        ctr2 += 1  #counter increases until end is reached and loop ends
    ctr += 1 #counter for first loop increases
print ("\n") #new line


print ("For Loop \n")


for x in range (1,13):  #first loop
    for y in range (1,13): #second loop
        print(x*y, end="\t") #mulitplication of both variables in loops with x being increased after every instance of the y loop ends
    print()


