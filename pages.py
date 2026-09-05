from selenium.webdriver.common.by import By

class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        # We store the locators here at the top
        self.url = "https://demoqa.com/text-box"
        self.name_input = (By.ID, "userName")
        self.email_input = (By.ID, "userEmail")
        self.submit_btn = (By.ID, "submit")
        self.output_name = (By.ID, "name")

    # We store the actions here at the bottom
    def load(self):
        self.driver.get(self.url)

    def fill_form(self, name, email):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        
    def click_submit(self):
        btn = self.driver.find_element(*self.submit_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", btn)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_output_name(self):
        return self.driver.find_element(*self.output_name).text




class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        # The locators for the kitchen
        self.url = "https://demoqa.com/radio-button"
        self.yes_radio_label = (By.XPATH, "//label[@for='yesRadio']")
        self.success_text = (By.CLASS_NAME, "text-success")

    # The Waiter's actions
    def load(self):
        self.driver.get(self.url)

    def click_yes(self):
        self.driver.find_element(*self.yes_radio_label).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_text).text