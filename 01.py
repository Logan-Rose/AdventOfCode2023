import requests

cookies = {
    'session': '53616c7465645f5f79c25e836fb4443981317de7f73f5c7890c0f9db4b489fcb81b68aa3ba57a194cfc566c1a5be766997db891094f033a7b0bf4b3776951bc4',
}
response = requests.get('https://adventofcode.com/2023/day/1/input', cookies=cookies)
wordList = response.text.split('\n')

NUMBERS = "0123456789"

def getLastNumber(word):
    pointer = 0
    numFound = False;
    for i in range(len(word)-1, -1, -1):
        j = i
        while j >= 0 and word[j] in NUMBERS:
            j -= 1
            numFound = True
        if numFound:
            return word[j+1:i+1]
    return '0' 
        

def getFirstNumber(word):
    pointer = 0
    numFound = False;
    for i in range(len(word)):
        j = i
        while j < len(word) and word[j] in NUMBERS:
            j+=1
            numFound = True
        if numFound:
            return word[i:j]
    return '0'

sum = 0
for i in range(len(wordList)):
    # Initially misread the question and thought I needed first and last numbers, but it is actually first and last digits. I updated the code here to take the first digit from the first number and the last digit from the last number becuase I'm lazy
    first = getFirstNumber(wordList[i])[0]
    last = getLastNumber(wordList[i])[-1]
    sum += int(first+last)
print(sum)
