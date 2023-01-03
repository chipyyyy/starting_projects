import numpy as np
with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data8_test.txt') as f: 
    trees = f.readlines()

treesList = [[int(numberTrees) for numberTrees in treeLine.strip()] for treeLine in trees]

visibleTrees = 0

def direction_check(direction, i, j, line, treesList):
    treesfound = 0
    if direction == 'left':
        for tree in line[:j]:
            if tree >= line[j]:
                return treesfound, (i,j)
        treesfound += 1
        return treesfound, (i,j)
    elif direction == 'right':
        for tree in line[j+1:]:
            if tree >= line[j]:
                return treesfound, (i,j)
        treesfound += 1
        return treesfound, (i,j)
    elif direction == 'up':
        for k, line in zip(range(len(treesList[:i])), treesList):
            if line[j] >= treesList[i][j]: 
                return treesfound, (i,j)
        treesfound += 1
        return treesfound, (i,j)
    elif direction == 'down':
        for k, line in zip(range(len(treesList[i+1:])), treesList):
            if line[j] >= treesList[i][j]: 
                return treesfound, (i,j)
            
        treesfound += 1
        return treesfound, (i,j)

        
#list, which saves the ccoordintes of found trees as a tupel
foundalready = []

for i, line in enumerate(treesList):
    #checks for outer row
    if i == 0 or i == len(treesList)-1:
        visibleTrees += len(line)
        continue
    #checks for outer elements in row 
    for j, tree in enumerate(line):
        if j == 0 and i != 0 or j == len(line)-1 and i != len(treesList)-1:
            visibleTrees += 1
            continue
        #checks in every direction
        for direction in ['left','right','up','down']:
            treesfound, index = direction_check(direction, i, j, line, treesList)
            if treesfound == 1 and index not in foundalready:
                visibleTrees += 1
                foundalready.append((index))



print(visibleTrees)
print(foundalready)
