
def explore_data(dataset, start, end, rows_and_cols=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice: 
        print(row)
        print('\n')
    if rows_and_cols: 
        print('Anzahl der Rrehen:', len(dataset))
        print('Anzahl der Spalten', len(dataset[0]))

def read_datasets(dataset_path):
    from csv import reader
    opened_file = open(dataset_path)
    read_file = reader(opened_file)
    apps_data = list(read_file)
    return apps_data

def find_empty(dataset, header_row): 
    empty_index = []
    for row in dataset[1:]:
        if len(row) < len(header_row): 
            print(row)
            print(dataset.index(row))
            empty_index.append((dataset.index(row)))
    return empty_index


def double_input(dataset, index_name_in_data):
    list_single = []
    list_double = []
    for row in dataset[1:]: 
        name = row[index_name_in_data]
        if name in list_single:
            list_double.append(name)
        else:
            list_single.append(name)
    return list_single, list_double

def find_max_rating(dataset, index_name_in_data, index_n_rating_in_data):
    reviews_max = {}
    for row in dataset[1:]:
        name = row[index_name_in_data]
        n_rating = row[index_n_rating_in_data]
        if name in reviews_max and reviews_max[name] < n_rating: 
            reviews_max[name] = n_rating 
        elif name not in reviews_max:
            reviews_max[name] = n_rating
    return reviews_max