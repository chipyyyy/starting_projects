
with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data6.txt') as f: 
    data = f.readlines()

lastFourChars = []
new_data = []

for element in data:
    for char in element:
        new_data.append(char)

def nodoublecheck(lastFourChars, n):
    lastFourChars = set(lastFourChars)
    if len(lastFourChars) == 4:
        print(f'first marker after charakter {n+1}')
        return True
    else:
        return False

part1_count = 0
for i in range(len(new_data) - 4):
    part1_count += 1
    if len(set(new_data[i: i + 4])) == 4:
        print(part1_count + 3)
        break
part2_count = 0
for i in range(len(new_data)):
    part2_count += 1
    if len(set(new_data[i: i + 14])) == 14:
        print(part2_count + 14)
        break

def search(size):
    for i in range(len(data)-size):
        if len(set(data[i:i+size])) == size:
            return i+size

data = open("/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data6.txt").read().strip()
print(f"Part 1: {search(4)}")
print(f"Part 2: {search(14)}")