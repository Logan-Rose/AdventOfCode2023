inputs = open('inputs_03.txt','r').read().split('\n')[0:-1]
numbers = "0123456789"

def safeGetIndex(row, col, grid):
    try:
        return grid[row][col]
    except:
        return '.' 

def getFullNumber(row, col, grid):
    left = col
    right = col
    while safeGetIndex(row, left, grid) in numbers:
        left -= 1
    while safeGetIndex(row, right, grid) in numbers:
        right += 1
    return (row, (left+1),  right)

parts = set() 
for row in range(len(inputs)):
    for col in range(len(inputs[row])):
        atCurrentIndex = inputs[row][col]
        if atCurrentIndex not in numbers and atCurrentIndex != '.':
            neighbours = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1, -1), (1,0), (1,1)]
            for (y,x) in neighbours:
                neighbour = safeGetIndex(row+y, col+x, inputs)
                if neighbour in numbers:
                    fullNumber = getFullNumber(row+y, col+x, inputs)
                    parts.add(fullNumber)

partOneSum = 0
for (row, start, end) in parts:
    partOneSum += int(inputs[row][start:end])

print(partOneSum)

# Part 2
partTwoSum = 0
parts = set() 
for row in range(len(inputs)):
    for col in range(len(inputs[row])):
        atCurrentIndex = inputs[row][col]
        if atCurrentIndex == '*':
            neighbours = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1, -1), (1,0), (1,1)]
            adjacentParts = set() 
            for (y,x) in neighbours:
                neighbour = safeGetIndex(row+y, col+x, inputs)
                if neighbour in numbers:
                    fullNumber = getFullNumber(row+y, col+x, inputs)
                    adjacentParts.add(fullNumber)
            if len(adjacentParts) == 2:
                [rowOne, leftOne, rightOne] = list(adjacentParts)[0]
                [rowTwo, leftTwo, rightTwo] = list(adjacentParts)[1]
                partTwoSum += (int(inputs[rowOne][leftOne:rightOne]) * int(inputs[rowTwo][leftTwo:rightTwo]))

# partNumberSum = 0
# for (row, start, end) in parts:
#     partNumberSum += int(inputs[row][start:end])

print(partTwoSum)


