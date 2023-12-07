inputs = open("inputs_05.txt", "r").read().strip().split('\n\n')
seeds = [int(seed) for seed in inputs[0][7:].split()]
maps = inputs[1:]
for i in range(len(maps)):
    lines = maps[i].split('\n')
    for j in range(len(lines)):
        lines[j] = lines[j].split()
    maps[i] = lines[1:]
for i in range(len(maps)):
    for j in range(len(maps[i])):
        for k in range(len(maps[i][j])):
            maps[i][j][k] = int(maps[i][j][k])

# Part 1

locations = []
for seed in seeds:
    for m in maps:
        for option in m:
            [destinationRange, sourceRange, rangeLength] = option
            if(seed >= sourceRange and seed < sourceRange + rangeLength):
                seed = destinationRange + (seed - sourceRange)
                break
    locations.append(seed)

print(min(locations))

# Part 2

locations = []
inputRanges = []
for i in range(0, len(seeds), 2):
    start = seeds[i+1]
    numberOfSeeds =  seeds[i]
    inputRanges.append((start, start+numberOfSeeds))
for i in range(len(maps)):
    for j in range(len(maps[i])):
        [destinationRange, sourceRange, rangeLength] = maps[i][j]
        maps[i][j] = ((destinationRange+rangeLength), (sourceRange, sourceRange + rangeLength))
 
for inputRange in inputRanges:
     print(inputRange)
     for m in maps[:1]:
        for layer in m:
            (sourceRangeMin, sourceRangeMax) = layer[1]
            overlap = (max(inputRange[0], sourceRangeMin), min(inputRange[1], sourceRangeMax))
            print(layer)
            if(overlap[1] >= overlap[0]):
                print("Overlap", overlap)
                print("New inputs:", overlap[1] - overlap[0])


        print('----')
         
     print('====')
#for seed in seeds:
#    for m in maps:
#        for option in m[::]:
#            [destinationRange, sourceRange, rangeLength] = option
#            if(seed >= sourceRange and seed < sourceRange + rangeLength):
#                seed = destinationRange + (seed - sourceRange)
#                break
#    locations.append(seed)


