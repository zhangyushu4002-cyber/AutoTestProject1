from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 元素定位器
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    submit_btn = (By.ID, "submit")
    success_text = (By.ID, "welcome")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def input_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)

    def input_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

    def get_success_text(self):
        return self.wait.until(EC.presence_of_element_located(self.success_text)).text

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_submit()