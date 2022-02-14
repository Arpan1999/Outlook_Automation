from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[contains(@type, 'email')]")
    next = (By.XPATH, "//input[contains(@value,'Next')]")
    wrong_email_error_message = (By.XPATH, "//div[@id = 'usernameError']")
    password = (By.XPATH, "//input[@name = 'passwd']")
    signin = (By.XPATH, "//input[contains(@type, 'submit')]")
    wrong_password_error_message = (By.XPATH, "//div[contains(@id, 'passwordError')]")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def clickNext(self):
        return self.driver.find_element(*LoginPage.next)

    def emailErrorMessage(self):
        return self.driver.find_element(*LoginPage.wrong_email_error_message)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickSignIn(self):
        return self.driver.find_element(*LoginPage.signin)

    def passwordErrorMessage(self):
        return self.driver.find_element(*LoginPage.wrong_password_error_message)

    def capture_screenshot(self,name):
        self.driver.get_screenshot_as_file(name)

