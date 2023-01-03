import gender_guesser.detector as gender
import csv

d = gender.Detector()

file = open('')
data = list(csv.reader(file, delimiter = ';'))


def anrede(vorname, nachname, gender):
    if gender == 'male':
        anrede = f'Sehr geehrter Herr {nachname},'
        name.append(anrede)
    if gender == 'mostly_male':
        anrede = f'Sehr geehrter Herr {nachname},'
        name.append(anrede)
    if gender == 'female':
        anrede = f'Sehr geehrte Frau {nachname},'
        name.append(anrede)
    if gender == 'mostly_female':
        anrede = f'Sehr geehrte Frau {nachname},'
        name.append(anrede)


for name in data: 
    vorname = name[1]
    nachname = name[0]
    gender = d.get_gender(vorname)
    anrede(vorname, nachname, gender)

    if gender == 'unknown': 
        vorname = vorname.split('-')[0]
        gender = d.get_gender(vorname)
        if gender == 'unknown': 
            vorname = vorname.split()[0]
            gender = d.get_gender(vorname)
        anrede(vorname, nachname, gender)

new_file = open('new_file.csv','w')
with new_file:
    writer = csv.writer(new_file)
    for row in data: 
        writer.writerow(row)


        










