import csv
import os
from pprint import pp


def read_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


def find_shop(current_data, new_coffee_data: dict) -> bool:
    for each in current_data:
        pp(each)
        if new_coffee_data.get('Location') in each.values():
            # print("Duplicate")
            return True
    # print("No Duplicate Found.")
    return False


def add_shop(csv_file_path, coffee_shop_data: dict):
    with open(csv_file_path, 'a', newline='') as f:
        # Create a CSV writer object
        writer = csv.writer(f)
        # Write a row to the CSV file with the values of coffee_shop_data
        writer.writerow(coffee_shop_data.values())

def format_time(time):
    return time.strftime("%-I:%M %p")


def main():
    data = read_csv('cafe-data.csv')
    test_dict = {
        'Cafe Name': 'Starbucks',
        'Location': 'https://maps.app.goo.gl/ZEn2zW99dN3fZFxj7'
    }
    # find_shop(data, test_dict)
    if not find_shop(data, test_dict):
        print("New Entry")
    else:
        print("Duplicate Entry")


if __name__ == '__main__':
    main()
