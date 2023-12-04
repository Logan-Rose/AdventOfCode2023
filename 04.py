rounds = open('inputs_04.txt', 'r').read().split('\n')[0:-1]
totalPoints = 0
for round in rounds:
    [label, numbers] = round.split(':') 
    cardNo = label.split()[1]
    [winnersRaw, handRaw] = numbers.split('|')
    winners = set(winnersRaw.split())
    hand = handRaw.split()
    matches = 0 
    for num in hand:
        if num in winners:
            matches +=1
    points =0 
    if matches == 1:
        points = 1
    elif matches > 1:
        points = 1 
        for i in range(matches-1):
            points = points * 2

    totalPoints += points

print(totalPoints)

# Part 2 

# Perfect use case for dynamic programming, but quiote short on time today, so I just used a queue

totalPoints = 0
for round in rounds:
    [label, numbers] = round.split(':') 
    cardNo = label.split()[1]
    [winnersRaw, handRaw] = numbers.split('|')
    winners = set(winnersRaw.split())
    hand = handRaw.split()
    matches = 0 
    for num in hand:
        if num in winners:
            matches +=1
    for j in range(matches):
       rounds.append(rounds[int(cardNo)+j]) 

print(len(rounds))
