import time

from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestFile(BaseClass):

    def test_login(self):
        log = self.getLogger()
        log.info("start")
        ss = LoginPage(self.driver)
        time.sleep(5)
        log.info("Entering wrong email")
        email = LoginPage(self.driver)
        email.getEmail().send_keys("a15")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s1.png")
        nextButton = LoginPage(self.driver)
        nextButton.clickNext().click()
        time.sleep(3)
        emailErrorMessage = LoginPage(self.driver)
        text1 = emailErrorMessage.emailErrorMessage().text
        log.info(text1)
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s2.png")
        # assert text1 == "We couldn't find an account with that username. Try another, or get a new Microsoft account"
        email.getEmail().clear()
        time.sleep(3)
        log.info("Entering correct email")
        email.getEmail().send_keys("demo.automation@outlook.com")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s3.png")
        nextButton.clickNext().click()
        time.sleep(3)
        log.info("Entering wrong password")
        password = LoginPage(self.driver)
        password.getPassword().send_keys("abcd")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s4.png")
        time.sleep(3)
        signin = LoginPage(self.driver)
        signin.clickSignIn().click()
        time.sleep(3)
        passwordErrorMessage = LoginPage(self.driver)
        text2 = passwordErrorMessage.passwordErrorMessage().text
        log.info(text2)
        # assert text2 == "Your account or password is incorrect. If you don't remember your password, reset it now."
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s5.png")
        password.getPassword().clear()
        time.sleep(3)
        log.info("Entering correct password")
        password.getPassword().send_keys("Password@1999")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s6.png")
        signin.clickSignIn().click()
        time.sleep(3)
        signin.clickSignIn().click()
        time.sleep(5)
        log.info("Successful login")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s7.png")
