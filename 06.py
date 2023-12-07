inputs = open("inputs.txt", "r").read().split('\n')[0:-1]
print(':)')
cleanInput = []
for row in inputs:
    [label, nums] = row.split(":")
    vals = [int(x) for x in nums.split()]
    cleanInput.append(vals)

[times, distances] = cleanInput
waysToBeat = []
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    for j in range(time):
        left = j
        right = time - j
        if (left * right) > distance:
            waysToBeat.append((right-left + 1))
            break

answer = 1
for way in waysToBeat:
    answer *= way

