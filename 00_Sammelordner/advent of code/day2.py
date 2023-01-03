points = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
}


with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data2.txt') as f: 
    text = f.readlines()
#part 1
score = 0 

for lines in text:
    line = lines.strip()
    value = points[line]
    score += value

print(score)

#part 2
#x = loose 
#y = draw 
#z = win 
#a = schere
#b = stein 
#c = papier




