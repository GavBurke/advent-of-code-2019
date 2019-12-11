puzzleMin     = 254032
puzzleMax     = 789860
puzzleCurrent = puzzleMin
puzzleCount   = 0

while puzzleCurrent <= puzzleMax:
    isRepeated   = False
    isDecreasing = False
    puzzleCurrentArray = list(map(int, str(puzzleCurrent)))
    i = 0
    while i < 5:
        if puzzleCurrentArray[i] == puzzleCurrentArray[i+1]:
            isRepeated = True
        i+=1
    i = 0
    while i < 5:
        if puzzleCurrentArray[i] > puzzleCurrentArray[i+1]:
            isDecreasing = True
        i+=1
    puzzleCurrent+=1
    if isRepeated == True and isDecreasing == False:
        puzzleCount+=1

print(puzzleCount)

