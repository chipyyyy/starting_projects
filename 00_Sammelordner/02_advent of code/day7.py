from collections import defaultdict

with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data7.txt', 'r') as f: 
    data = f.readlines()

path = []
directory = defaultdict(int)

for command in data:
    command = command.strip()
    if command == '$ cd ..':
        path.pop()
    elif command[:4] == '$ cd':
        command = command.split()
        path.append(command[2])
    elif command[0].isdigit(): 
        size, _ = command.split()
        for i in range(len(path)): 
            directory['/'.join(path[:i + 1])] += int(size)

print('Part 1:', sum(d for d in directory.values() if d < 100_000))
print('Part 2:', min([f for f in directory.values() if directory['/'] - f <= 40_000_000]))



AT_MOST = 100000


