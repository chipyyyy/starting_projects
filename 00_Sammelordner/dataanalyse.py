
#Importiert alle Funktionen aus der Datei
from functions_dataanalyse import *

ios = read_datasets('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/AppleStore.csv')
android = read_datasets('/Users/tomhartmann/Documents/04_ENGINEERING/00_CODING/VS/BEGINNING/googleplaystore.csv')

#Daten ansehen 
#explore_data(ios, 0, 10)
#explore_data(android, 0, 10)

#Header ausgeben für Übersicht der folgenden Analyse
header_ios = ios [0] #['', 'id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']
header_android = android [0] #['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']

#Nach Fehlern in Daten suchen
#1. nach leeren Einträgen suchen + entfernen 
#2. nach doppelten Daten suchen + entfernen
#3. nach nicht-englsichen Apps suchen + entfernen

#1. nach leeren Einträgen suchen und entfernen
empty_android = find_empty(android, header_android)
empty_ios = find_empty(ios, header_ios)

if len(find_empty(ios, header_ios)) > 0:
    for n in empty_ios:
        del ios[find_empty(ios, header_ios)]
        print('Leerer Eintrag an Stelle ' + str(n) + ' wurde gelöscht')

if len(find_empty(android, header_android)) > 0:
    for n in empty_android:
        del android[n]
        print('Leerer Eintrag an Stelle ' + str(n) + ' wurde gelöscht')

#2. nach doppelten Einträgen suchen 
single_ios, double_ios = double_input(ios, 2)
single_android, double_android = double_input(android, 0)

#doppelte Einträge nach höchstem Rating sortieren und anschließend die mit niedrigerem Rating entfernen
reviews_max_ios = find_max_rating(ios, 2, 6)
reviews_max_android = find_max_rating(android, 0, 8)


#Hier weiter machen!
def clean_data_from_double(dataset, reviews_max, index_name_in_data, index_n_rating_in_data):
    clean_data = []
    for row in dataset[1:]:
        name = row[index_name_in_data]
        n_rating = row[index_n_rating_in_data]
        if (reviews_max[name] == n_rating): 
            clean_data.append(row)
    return clean_data

clean_data_android = clean_data_from_double(android, reviews_max_android, 0, 8)
clean_data_ios = clean_data_from_double(ios, reviews_max_ios, 2, 6)

def find_free(dataset, index_price):
    free_apps = []
    for row in dataset:
        if dataset[index_price] == '0':
            free_apps.append(row)
        
    return free_apps



free_ios = find_free(clean_data_ios, 5)
free_android = find_free(clean_data_android, 7)

print(free_ios[:4])
print(free_android[:4])








