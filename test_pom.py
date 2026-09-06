import pytest
import csv
from pages import TextBoxPage, RadioButtonPage

# --- 1. OUR SPREADSHEET READER ---
def get_csv_data():
    data_list = []
    with open("test_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skips the header row (name,email)
        
        for row in reader:
            data_list.append(tuple(row))
            
    return data_list

# --- 2. WE PLUG THE READER DIRECTLY INTO PYTEST ---
# Pytest will now open the CSV and loop this test for every row it finds!
@pytest.mark.parametrize("name, email", get_csv_data())
def test_text_box_clean(driver, name, email):
    text_box_page = TextBoxPage(driver)
    text_box_page.load()
    
    text_box_page.fill_form(name, email) 
    text_box_page.click_submit()
    
    assert name in text_box_page.get_output_name() 

# (The radio button test stays exactly the same)
def test_radio_button_clean(driver):
    radio_page = RadioButtonPage(driver)
    radio_page.load()
    radio_page.click_yes()
    assert "Yes" in radio_page.get_success_message()