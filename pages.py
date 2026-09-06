from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select # NEW TOOL FOR DROPDOWNS

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    def load(self):
        self.driver.get("https://demoqa.com/text-box")
    def fill_form(self, name, email):
        name_box = self.wait.until(EC.visibility_of_element_located((By.ID, "userName")))
        name_box.send_keys(name)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
    def click_submit(self):
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
    def get_output_name(self):
        output = self.wait.until(EC.visibility_of_element_located((By.ID, "name")))
        return output.text

class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def load(self):
        self.driver.get("https://demoqa.com/radio-button")
    def click_yes(self):
        yes_label = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='yesRadio']")))
        yes_label.click()
    def get_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "text-success")))
        return message.text

# --- THE NEW ENTERPRISE FEATURES ---

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def load(self):
        self.driver.get("https://demoqa.com/alerts")
        
    def click_alert_button(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "alertButton")))
        self.driver.execute_script("arguments[0].click();", btn)
        
    def accept_alert(self):
        self.wait.until(EC.alert_is_present()) # 1. Wait for popup
        alert = self.driver.switch_to.alert    # 2. Switch robot's brain to the popup
        text = alert.text
        alert.accept()                         # 3. Click the "OK" button
        return text

class DropdownPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def load(self):
        self.driver.get("https://demoqa.com/select-menu")
        
    def select_color(self, color_name):
        # 1. Find the dropdown menu
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "oldSelectMenu")))
        # 2. Convert it into a special Selenium Select object
        dropdown = Select(element) 
        # 3. Tell it to pick an option by its text
        dropdown.select_by_visible_text(color_name)
        
    def get_selected_color(self):
        element = self.driver.find_element(By.ID, "oldSelectMenu")
        dropdown = Select(element)
        return dropdown.first_selected_option.text