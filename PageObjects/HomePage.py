from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    new_message = (By.XPATH, "//span[contains(text(), 'New message')]")
    sender = (By.XPATH, "//input[contains(@aria-label, 'To')]")
    subject = (By.XPATH, "//input[contains(@aria-label, 'Add a subject')]")
    messageBody = (By.XPATH, "//div[contains(@aria-label, 'Message body')]")
    send = (By.XPATH, "//button[contains(@title, 'Send (Ctrl+Enter)')]")
    bold = (By.XPATH, "//button[contains(@aria-label,'Bold (Ctrl+B)')]")
    italic = (By.XPATH, "//button[contains(@aria-label,'Italic (Ctrl+I)')]")
    wsend = (By.XPATH, "(//span[contains(text(), 'Send')])[last()]")
    errorMessage = (By.XPATH, "//span[contains(text(), 'This message must have at least one recipient.')]")

    def getnewMessage(self):
        return self.driver.find_element(*HomePage.new_message)

    def getsender(self):
        return self.driver.find_element(*HomePage.sender)

    def getsubject(self):
        return self.driver.find_element(*HomePage.subject)

    def getmessageBody(self):
        return self.driver.find_element(*HomePage.messageBody)

    def getsend(self):
        return self.driver.find_element(*HomePage.send)

    def make_bold(self):
        return self.driver.find_element(*HomePage.bold)

    def make_italic(self):
        return self.driver.find_element(*HomePage.italic)

    def final_send(self):
        return self.driver.find_element(*HomePage.wsend)

    def getErrorMessage(self):
        return self.driver.find_element(*HomePage.errorMessage)



