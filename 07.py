inputs = open("inputs_07.txt", "r").read().split('\n')[0:-1]
rounds = []
ranks = "023456789TJQKA"
for round in inputs:
    rounds.append(round.split())

def getValue(hand):
    counts = {} 
    for card in set(hand):
        counts[card] = hand.count(card)
    pairs = 0
    for count in counts:
        if counts[count] == 2:
            pairs +=1
    if pairs == 2:
        return 2
    
    if 5 in counts.values():
        return 6 
    if 4 in counts.values():
        return 5 
    if 2 in counts.values() and 3 in counts.values():
        return 4
    if 3 in counts.values():
        return 3 
    if 2 in counts.values():
        return 1 
    return 0 

enhancedData = []
total = 0
for round in rounds:
    value = getValue(round[0])
    enhancedData.append({"Hand":round[0], "Score": value, "Wager": round[1]})

def compare(d1, d2):
    if(d1["Score"] == d2["Score"]):
        return 0 
    if(d1["Score"] < d2["Score"]):
        return -1
    if(d1["Score"] > d2["Score"]):
        return 1
enhancedData.sort(key=lambda x: (x["Score"], ranks.index(x['Hand'][0]), ranks.index(x['Hand'][1]), ranks.index(x['Hand'][2]), ranks.index(x['Hand'][3]), ranks.index(x['Hand'][4])))

for i, e in enumerate(enhancedData):
    total += (1+i) * int(e['Wager'])


print(total)
