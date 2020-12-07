#used to loop code or end program
def end():
    j = input("Would you like to use the program again? Answer with Yes or No (case sensitive).")
    if j == "Yes":
        main()
    elif j == "No":
        print("Program will now exit...")
        exit()
    else:
        print("Please input a valid answer")
        end()
#main function
def main():
    #user inputs for numbers
    a = int(input("Enter a whole, non-negative, number:"))
    b = int(input("Enter a whole, non-negative, number:"))

    #arrays to hold factors of a and b
    aarray = []
    barray = []

    #common factor array to find gcf
    cfarray = []

    #finding factors of each number and appending to respective array
    def factors():
        for i in range(1, a+1):
            if a % i == 0:
                aarray.append(i)
        for i in range(1, b + 1):
            if b % i == 0:
                barray.append(i)
        print("The factors for a are:", aarray)
        print("The factors for b are:", barray)
    factors()

    #finding gcf by iterating through array of common factors between a and b and choosing the final cf
    def gcf():
        for y in aarray:
            for z in barray:
                while y == z:
                    cfarray.append(y)
                    break
        print("The GCF of", a, "and", b, "is", cfarray[-1])
    gcf()

    #function of how lcm is found
    def lcm():
        r = a / cfarray[-1]
        h = r * b
        print ("The lcm of", a, "and", b, "is", h)
    lcm()
    end()
main()












