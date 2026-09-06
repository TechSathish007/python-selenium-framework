from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        # THIS IS THE BRAIN: Wait up to 10 seconds for things to happen
        self.wait = WebDriverWait(driver, 10) 

    def load(self):
        self.driver.get("https://demoqa.com/text-box")

    def fill_form(self, name, email):
        # SMART WAIT: Wait exactly until the box is visible before typing
        name_box = self.wait.until(EC.visibility_of_element_located((By.ID, "userName")))
        name_box.send_keys(name)
        
        self.driver.find_element(By.ID, "userEmail").send_keys(email)

    def click_submit(self):
        # SMART WAIT: Wait exactly until the button is clickable
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn) # Scroll down to it
        self.driver.execute_script("arguments[0].click();", submit_btn) # Click it safely

    def get_output_name(self):
        # SMART WAIT: Wait for the result to pop up on screen
        output = self.wait.until(EC.visibility_of_element_located((By.ID, "name")))
        return output.text

class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://demoqa.com/radio-button")

    def click_yes(self):
        # SMART WAIT: Wait for the Yes button to be clickable
        yes_label = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='yesRadio']")))
        yes_label.click()

    def get_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "text-success")))
        return message.text