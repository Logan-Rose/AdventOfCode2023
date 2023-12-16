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

    return inputs

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
    print(emptyCols)
    for i in emptyCols[::-1]:
        for j in range(len(inputs)):
            inputs[j] = inputs[j][:i] +"."+ inputs[j][i:]
    return inputs

def getGalaxies(inputs):
    galaxies = set()
    emptyLayers = []
    for i in range(len(inputs)):
        empty = True
        for j in range(len(inputs[i])):
            if inputs[i][j] == "#":
                galaxies.add((i,j))
    return galaxies 


for row in inputs:
    print(row)
print('==')
expanded = expandCols(expandRows(inputs))
galaxies = getGalaxies(expanded)

for row in expanded:
    print(row)
            
allPaths = []
for galaxy in galaxies:
    for otherGalaxy in galaxies:
        xDist = abs(galaxy[0] - otherGalaxy[0])
        yDist = abs(galaxy[1] - otherGalaxy[1])
        allPaths.append(xDist + yDist)
print(sum(allPaths)/2)
