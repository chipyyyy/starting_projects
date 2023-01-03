
with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data4.txt') as f: 
    data = [tuple(int(x) for assignment in row.split(',')
                      for x in assignment.split('-')) for row in f.read().splitlines()] #read() liest, splitlines() entfernt \n


def within(a_lower, a_upper, b_lower, b_upper):
     return a_lower <= b_lower and b_upper <= a_upper or b_lower <= a_lower and a_upper <= b_upper
def overlap(a_lower, a_upper, b_lower, b_upper):
     return b_lower <= a_lower <= b_upper or a_lower <= b_lower <= a_upper
part1 = sum(within(a_lower, a_upper, b_lower, b_upper) for a_lower, a_upper, b_lower, b_upper in data)
part2 = sum(overlap(a_lower, a_upper, b_lower, b_upper) for a_lower, a_upper, b_lower, b_upper in data)
print(part1)
print(part2)
        
