inputs = open("inputs_12.txt", "r").read().split("\n")[0:-1]

def getPossibilities(input):
    possibleInputs = [input]
    for i in range(len(input)):
        for j in range(len(possibleInputs)-1, -1, -1):
            if possibleInputs[j][i] == "?":
                input = possibleInputs[j]
                possibleInputs.pop(j)
                p1 = input[:i] + "." + input[i+1:]
                p2 = input[:i] + "#" + input[i+1:]
                possibleInputs.append(p1)
                possibleInputs.append(p2)
    return possibleInputs

def getPattern(input):
    pattern = []
    path = 0
    for i in range(len(input)):
        if input[i] =="#":
            path +=1
        else:
            if path != 0:
                pattern.append(path)
            path = 0
    if input[-1] == "#":
        pattern.append(path)
    return pattern

count = 0
allArrangements = 0
for input in inputs:
    [parts, patternRaw] = input.split(" ")
    pattern = [int(x) for x in patternRaw.split(',')]
    print(parts, pattern)
    print(getPossibilities(parts))
    for possibility in getPossibilities(parts):
        possibilityPattern = getPattern(possibility)
        print(possibilityPattern)
        if possibilityPattern == pattern:
            allArrangements +=1
print(allArrangements)
