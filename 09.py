inputs = open("inputs_09.txt", "r").read().split('\n')[0:-1]

histories = []
total = 0
for history in inputs:
    topLayer = [int(x) for x in history.split()]
    layers = [topLayer]
    while len(layers) == 1 or len(layer) > 0:
        layer = []
        for i in range(1, len(layers[-1])):
            layer.append(layers[-1][i] - layers[-1][i-1])
        layers.append(layer)
    layers = layers[::-1]
    for i in range(2, len(layers)):
        layers[i].append(layers[i-1][-1] + layers[i][-1])
    total += layers[-1][-1]

print(total)
