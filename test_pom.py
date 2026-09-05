import pytest
from pages import TextBoxPage, RadioButtonPage

# --- THIS IS THE MAGIC TRICK ---
# We give Pytest a list of 3 different people.
@pytest.mark.parametrize("name, email", [
    ("Sathish R", "sathish@example.com"),
    ("John Batman", "batman@test.com"),
    ("Spider Man", "spidey@test.com")
])
def test_text_box_clean(driver, name, email):
    # Notice how we put the words 'name' and 'email' inside the parentheses above?
    # Pytest will automatically grab "Sathish R" and put it wherever it sees 'name'
    # Then it runs the test again and grabs "John Batman", and so on!
    
    text_box_page = TextBoxPage(driver)
    text_box_page.load()
    
    # We use the variable 'name' instead of typing "Sathish R" in quotes
    text_box_page.fill_form(name, email) 
    text_box_page.click_submit()
    
    assert name in text_box_page.get_output_name() 
# --------------------------------

def test_radio_button_clean(driver):
    radio_page = RadioButtonPage(driver)
    radio_page.load()
    radio_page.click_yes()
    assert "Yes" in radio_page.get_success_message()