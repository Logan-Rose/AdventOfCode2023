inputs = open("inputs_11.txt", "r").read().split("\n")[0:-1]
def expandRows(inputs):
    emptyLayers = []
    for i in range(len(inputs)):
        empty = True
        for j in range(len(inputs[i])):
            if inputs[i][j] == "#":
                empty = False
                break
        if empty:
            emptyLayers.append(i)
    for i in emptyLayers[::-1]:
        inputs.insert(i, inputs[i])

    return (inputs, emptyLayers)

def expandCols(inputs):
    emptyCols = []
    for i in range(len(inputs[0])):
        empty = True
        for j in range(len(inputs)):
            if inputs[j][i] == "#":
                empty = False
                break
        if(empty):
            emptyCols.append(i)
    for i in emptyCols[::-1]:
        for j in range(len(inputs)):
            inputs[j] = inputs[j][:i] +"."+ inputs[j][i:]
    return (inputs, emptyCols)

def getGalaxies(inputs):
    galaxies = set()
    emptyLayers = []
    for i in range(len(inputs)):
        empty = True
        for j in range(len(inputs[i])):
            if inputs[i][j] == "#":
                galaxies.add((i,j))
    return galaxies 

expanded = expandCols(expandRows(inputs)[0])[0]
galaxies = getGalaxies(expanded)

allPaths = []
for galaxy in galaxies:
    for otherGalaxy in galaxies:
        xDist = abs(galaxy[0] - otherGalaxy[0])
        yDist = abs(galaxy[1] - otherGalaxy[1])
        allPaths.append(xDist + yDist)

print("Part One")
print(int(sum(allPaths)/2))

inputs = open("inputs_11.txt", "r").read().split("\n")[0:-1]

galaxies = getGalaxies(inputs)
emptyRows = expandRows(inputs)[1]
emptyCols = expandCols(inputs)[1]
allPathsPartTwo = []
for galaxy in galaxies:
    for otherGalaxy in galaxies:
        xStart = galaxy[1]
        xEnd = otherGalaxy[1]
        xDist = abs(xStart - xEnd)
        for col in emptyCols:
            if( (col < xStart and col > xEnd) or (col > xStart and col < xEnd)):
                xDist += 999_999
        

        yStart = galaxy[0]
        yEnd = otherGalaxy[0]
        yDist = abs(yStart - yEnd)
        for row in emptyRows:
            if( (row < yStart and row > yEnd) or (row > yStart and row < yEnd)):
                yDist += 999_999 
        allPathsPartTwo.append(xDist + yDist)

print("Part Two")
print(int(sum(allPathsPartTwo)/2))
