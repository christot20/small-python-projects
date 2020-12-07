cars = ["Buick","Ford","Honda"]
colors = ["Red","Blue","Black","White","Green"]
aType = ["Sedan","SUV","Sports","Coupe","Truck"]
arr = []
arr.append(cars)
arr.append(colors)
arr.append(aType)
print (arr)
for a in arr[0]:
    for c in range(len(arr[1])):
        print(a, arr[1][c], arr[2][c])





