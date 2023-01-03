import string
with open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data3.txt') as f: 
    text = f.readlines()

#1. Nummeriert mit einer for-Loop alle Buchstaben nach ANSII Code durch und erstellt ein dict. 
#2. Nummeriert alle Großbuchstaben nach ANCII Code durch mit zwei Iteratoren (zip) 
#3. Hängt zwei dicts aneinander mit update. So, wie .append()
#4. Teilt den String in zwei Hälften und vergleicht jeweilst die einzelnen Buchstaben

letter_count = {chr(i+96):i for i in range(1,27)} #lowecase letters
uppercaseletter_count = {chr(i+64):j for i,j in zip(range(1,27), range(27,53))} #uppercase letters zip() lässt einen zwei Iteratoren in einem for loop benutzen

letter_count.update(uppercaseletter_count) #.update() hängt ein dict an ein dict

score = 0

for line in text:
    string = line.strip()
    string_1 = string[:len(string)//2] #Teilt String in zwei Hälften 
    string_2 = string[len(string)//2:]
    for letter_1 in string_1:
        if letter_1 in string_2:
            score += letter_count[letter_1]
            break
            
print(score)
batch_size = 3
l = [1,2,3,4,5,6,7,8,9,10]
score_2 = 0
j=0
for i in range(0, len(text), batch_size):
    string_1 = text[i].strip()
    string_2 = text[i+1].strip()
    string_3 = text[i+2].strip()
    for letter in string_1: 
        if letter in string_2 and letter in string_3:
            score_2 += letter_count[letter]
            break


print(score_2)
