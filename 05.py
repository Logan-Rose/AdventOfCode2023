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

locations = []
for seed in seeds:
    for m in maps:
        for option in m[::]:
            [destinationRange, sourceRange, rangeLength] = option
            if(seed >= sourceRange and seed < sourceRange + rangeLength):
                seed = destinationRange + (seed - sourceRange)
                break
    locations.append(seed)

print(min(locations))

