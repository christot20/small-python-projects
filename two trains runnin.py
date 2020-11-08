#variable assignment of x and y values with randint and imports
import math
from random import randint
x1 = randint (1,100)
y1 = randint (1,50)
#statement showing the variables of x and y
print ("The trains each moved", x1, "units horizontally and", y1, "units vertically.")
#distance equation
distance1 = math.sqrt((x1**2) + (y1**2))*2
#round answer of pythagorean theorem distance equation and change to string, float, int
print ("The distance between both trains is", float(distance1), "units.")
print ("The distance between both trains is", int(distance1), "units.")
print ("The distance between both trains is", str(distance1), "units.")
print ("The distance between both trains is", round(distance1,1),"units when rounded to the nearest tenth.")



