import csv
import pytest

# 1. The Helper Function: Opens the CSV and reads the rows
def get_csv_data():
    data_list = []
    # Open the file in 'read' mode
    with open("test_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # This skips the first row (the header: username,password)
        
        # Loop through the remaining rows and add them to our list
        for row in reader:
            data_list.append(tuple(row))
            
    return data_list

# 2. The Test: Pytest pulls the data directly from our helper function!
@pytest.mark.parametrize("user, pwd", get_csv_data())
def test_csv_login(user, pwd):
    # Instead of launching a browser for the demo, we will just print the data
    print(f"\n[Robot] Typing username: {user} | Typing password: {pwd}")