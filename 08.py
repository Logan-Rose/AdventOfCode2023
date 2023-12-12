import math
inputs = open("inputs_08.txt", "r").read().split('\n')[0:-1]
instructions = list(inputs[0].replace("L", "0").replace("R", "1"))
def partOne():
    print("---- PART 1 ----")
    for i in range(len(instructions)):
        instructions[i] = int(instructions[i])

    network = inputs[2:]
    nodeMap = {}
    for node in network:
        base, neighbours = node.split("=")
        [left, right] = neighbours.strip()[1:-1].split(", ")
        nodeMap[base.strip()] = (left, right)


    target = "AAA"
    steps = 0
    while target != "ZZZ":
        target = nodeMap[target][instructions[steps % len(instructions)]]
        steps +=1
    print(steps)

def partTwo():
    print('---- PART 2 ----')
    network = inputs[2:]
    nodeMap = {}
    for node in network:
        base, neighbours = node.split("=")
        [left, right] = neighbours.strip()[1:-1].split(", ")
        nodeMap[base.strip()] = (left, right)
    activeNodes = list(filter(lambda x: x[-1] == 'A', nodeMap.keys()))
    steps = 0
    allDone = False
    stepsToZ = []
    for i, target in enumerate(activeNodes):
        steps = 0
        while target[-1] != "Z":
            target = nodeMap[target][int(instructions[steps % len(instructions)])]
            steps += 1
        stepsToZ.append(steps)
    # Couldnt be bothered to write algorithm to calculate least common multiple sorry not sorry
    print(math.lcm(*stepsToZ))

partOne()
partTwo()
