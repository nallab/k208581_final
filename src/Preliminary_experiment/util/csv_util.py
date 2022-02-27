import os
import csv

def get_data_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        data = [row[0] for row in reader]
    return data

def my_makedirs(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

def exist_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def write_value(file_path, list_value):
    dir_name = os.path.dirname(file_path)
    my_makedirs(dir_name)
    exist_file(file_path)
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["key","pred", "obj"])
        writer.writerows(list_value)