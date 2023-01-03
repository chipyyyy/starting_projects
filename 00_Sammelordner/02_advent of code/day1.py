import csv

file = open('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/advent of code/data1.csv')
data = csv.reader(file, delimiter = ',')
data_list = list(data)

print(data_list[:4], len(data_list), len(data_list[0]))


max_value = 0
max_cal = []
for calories in data_list[1:]:
    try:
        num_calories = calories[0]
        max_cal.append(int(num_calories))
    except:
        new_sum = sum(max_cal)
        max_cal = []
        if new_sum > max_value: 
            max_value = new_sum

print(max_value)






        