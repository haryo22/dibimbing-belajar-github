import csv

def read_csv(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            print(f"Username: {row[0]}, Identifier: {row[1]}, First Name: {row[2]}, Last Name: {row[3]}")

if __name__ == "__main__":
    read_csv('username.csv')
