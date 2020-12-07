import sys
# inputs
user_input = input("Enter any key to start ('quit' to quit): ")
if user_input == 'quit':
    sys.exit("Program will exit...")
while user_input != 'quit':
    print("Please enter values for the truth gates and quit when you are finished.")
    try:
        a = int(input("Enter a number of 0 or 1 for a:"))
        if a != 1 and a != 0:
            raise ValueError("invalid a value, enter a value of 0 or 1")
        b = int(input("Enter a number of 0 or 1 for b:"))
        if b != 1 and b != 0:
            raise ValueError("invalid b value, enter a value of 0 or 1")
        c = int(input("Enter a number of 0 or 1 for c:"))
        if c != 1 and c != 0:
            raise ValueError("invalid c value, enter a value of 0 or 1")
    except ValueError as errormessage:
        print(errormessage)
    user_input = input("Enter any key to add different values or quit to continue:")
#if user tries to go through loop without correct numbers
if a != 0 and a != 1:
    sys.exit("Invalid Values. Program will exit...")
elif b != 0 and b != 1:
    sys.exit("Invalid Values. Program will exit...")
elif c != 0 and c != 1:
    sys.exit("Invalid Values. Program will exit...")
else:
    print(":)")
#values of circuit
print("Circuit A is", a)
print("Circuit B is", b)
print("Circuit C is", c)


# functions for the gates
def ANDGate(b, c):
    if b == 1 and b == c:
        x = 1
    else:
        x = 0
    return x


def NORGate(a, b):
    if a == 0 and b == 0:
        y = 1
    else:
        y = 0
    return y


def ORGate():
    if ANDGate(c, b) == 0 and NORGate(a, b) == 0:
        z = 0
    else:
        z = 1
    return z


# True or False
if ANDGate(b, c) == 1:
    h = True
else:
    h = False

if NORGate(a, b) == 1:
    i = True
else:
    i = False

if ORGate() == 1:
    Q = True

else:
    Q = False

print("The output of the AND Gate is", ANDGate(b, c), "and is", h)
print("The output of the NOR Gate is", NORGate(a, b), "and is", i)
print("The output of the OR Gate is", ORGate(), "and is", Q)
print("Q is", Q)
