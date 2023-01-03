import re

stack = [
    ['F','L','M','W'],
    ['F','M','V','Z','B'],
    ['Q','L','S','R','V','H'],
    ['J','T','M','P','Q','V','S','F'],
    ['W','S','L'],
    ['W','J','R','M','P','V','F'],
    ['F','R','N','P','C','Q','J'],
    ['B','R','W','Z','S','P','H','V'],
    ['W','Z','H','G','C','J','M','B'],
 ]

new_stack = [row[::-1] for row in stack]

for row in new_stack: 
    print(row)

with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data5.txt') as f: 
    file = f.readlines()

def getmove(row):
    move = [int(zahl) for zahl in re.findall(r'\d+', row)]
    return move

def moveBoxes(numberBoxes,fromStack,targetStack):
    temp = []
    for boxes in range(numberBoxes):
        temp.append(new_stack[fromStack][-1])
        new_stack[fromStack].pop()
    temp = temp [::-1]
    for box in temp:
        new_stack[targetStack].append(box)
    return new_stack

for row in file:
    move = getmove(row)
    numberBoxes = move[0]
    fromStack = move[1]-1
    targetStack = move[2]-1
    moveBoxes(numberBoxes,fromStack,targetStack)


for row in new_stack:
    try: 
        print(row[-1],end='')
    except:
        pass


    

