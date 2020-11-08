print ("For Loop")
numSet = [1,2,3]
alphaSet = ['A', 'B', 'C']   #lists
for x in range(len(numSet)):    #first loop
    for y in range(len(alphaSet)): #second loop
        print (numSet[x], alphaSet[y])  #first loop runs first thing in list then second loop completes the whole list
        #loop resets until lists have been finished
print ("While Loop")
#While Loop
o = 0 #variables set
while o < len(numSet): #first loop
    i = 0
    while i < len(alphaSet): #second loop does a full run and goes back when increment finishes
        print (numSet[o], alphaSet[i])
        i += 1   #counter each time second loop runs
    o += 1 #counter for the first loop
     #set to restart the second loop so that it can negate the counter and run again
