import wordList, random
arr = [[],[],[],[]]
for c in range(0, len(wordList.aAdjectives)):
    if c >= len(wordList.aNouns):
        arr[0].append("*")
    else:
        arr[0].append(wordList.aNouns[c])

    if c >= len(wordList.aVerbs):
        arr[1].append("*")
    else:
        arr[1].append(wordList.aVerbs[c])

    if c >= len(wordList.aAdjectives):
        arr[2].append("*")
    else:
        arr[2].append(wordList.aAdjectives[c])

    if c >= len(wordList.aAdverbs):
        arr[3].append("*")
    else:
        arr[3].append(wordList.aAdverbs[c])

i = True
while i == True:
    randomAdverb = random.randint(0, len(wordList.aAdjectives))
    randomAdj = random.randint(0, len(wordList.aAdjectives))
    randomVerb = random.randint(0, len(wordList.aAdjectives))
    randomNoun = random.randint(0, len(wordList.aAdjectives))
    print ("Your phrase is:", arr[0][randomNoun], arr[1][randomVerb],arr[2][randomAdj],arr[3][randomAdverb])
    i = input("Again? Say Yes or No:")
    if i == "Yes":
        i = True
    elif i == "No":
        i = False
        print ("Program will now exit.")
