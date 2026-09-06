import pytest
import csv
from pages import TextBoxPage, RadioButtonPage, AlertsPage, DropdownPage

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
@pytest.mark.parametrize("name, email", get_csv_data())
def test_text_box_clean(driver, name, email):
    text_box_page = TextBoxPage(driver)
    text_box_page.load()
    
    text_box_page.fill_form(name, email)
    text_box_page.click_submit()
    
    assert name in text_box_page.get_output_name()

def test_radio_button_clean(driver):
    radio_page = RadioButtonPage(driver)
    radio_page.load()
    radio_page.click_yes()
    assert "Yes" in radio_page.get_success_message()

# --- 3. COMPLEX WEB ELEMENTS ---
def test_alert_popup(driver):
    alert_page = AlertsPage(driver)
    alert_page.load()
    
    # Click the button to trigger the alert
    alert_page.click_alert_button()
    
    # Accept it and check what it said
    alert_text = alert_page.accept_alert()
    assert alert_text == "You clicked a button"

def test_dropdown_menu(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.load()
    
    # Select "Yellow" from the dropdown list
    dropdown_page.select_color("Yellow")
    
    # Verify that Yellow is actually the active selection now
    selected = dropdown_page.get_selected_color()
    assert selected == "Yellow"