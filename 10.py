input = open("inputs_10.txt", "r").read().split()



def getNextMoves(inputs, row, col):
    tile = inputs[row][col]
    match tile:
        case "|":
            return [(row + 1, col), (row - 1, col)]
        case "-":
            return [(row, col + 1), (row, col - 1)]
        case "L":
            return [(row - 1, col), (row, col + 1)]
        case "J":
            return [(row - 1, col), (row, col - 1)]
        case "7":
            return [(row + 1, col), (row, col - 1)]
        case "F":
            return [(row + 1, col), (row, col + 1)]
        case "S":
            return []
def getFirstMoves(inputs, row, col):
    startingPipes = []
    
    north = inputs[row-1][col]
    east = inputs[row][col+1]
    west = inputs[row][col-1]
    south = inputs[row+1][col]

    if north in ["|", "F", "7"]:
        startingPipes.append((row-1, col))
    if east in ["-", "J", "7"]:
        startingPipes.append((row, col+1))
    if west in ["-", "L", "F"]:
        startingPipes.append((row, col-1))
    if south in ["|", "L", "J"]:
        startingPipes.append((row+1, col))
    return startingPipes

def getStart(input):
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == "S":
                return (row, col)

start = getStart(input)
moves = getFirstMoves(input, start[0], start[1])
seen = set(getFirstMoves(input, start[0], start[1]))

while len(moves) != 0:
    node = moves.pop()
    nextMoves = getNextMoves(input, node[0], node[1])
    for move in nextMoves:
        if not (move in seen):
            moves.append(move)
        seen.add(move)

print(int(len(seen)/2))





