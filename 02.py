gamesRaw = open('inputs_02.txt', "r").read()
games = gamesRaw.split('\n')[0:-1]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

possibleIdSum = 0

for game in games:
    [label, roundsRaw] = game.split(':')
    rounds = roundsRaw.split(';')
    allRounds = []
    for round in rounds:
        roundsDict = {}
        cubes = round.split(',')
        for cube in cubes:
            [number, color] = cube.strip().split(' ')
            roundsDict[color] = int(number)
        allRounds.append(roundsDict)
    id = label.split(' ')[1]
    impossible = False
    for round in allRounds:
        print(round)
        if (round.get('red') and ( round.get('red') > MAX_RED )) or (round.get('green') and (round.get('green') > MAX_GREEN)) or (round.get('blue') and (round.get('blue') > MAX_BLUE)):
           impossible = True 
    if(not impossible):
        possibleIdSum += int(id)

print(possibleIdSum)
