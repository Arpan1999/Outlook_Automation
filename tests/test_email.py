import time

from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass


class TestFile(BaseClass):
    def test_newMessage(self):
        log = self.getLogger()
        log.info("start")
        ss = LoginPage(self.driver)
        time.sleep(5)
        log.info("Entering email")
        email = LoginPage(self.driver)
        email.getEmail().send_keys("demo.automation@outlook.com")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s8.png")
        nextButton = LoginPage(self.driver)
        nextButton.clickNext().click()
        time.sleep(3)
        log.info("Entering password")
        password = LoginPage(self.driver)
        password.getPassword().send_keys("Password@1999")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s9.png")
        signin = LoginPage(self.driver)
        signin.clickSignIn().click()
        time.sleep(3)
        signin.clickSignIn().click()
        time.sleep(5)
        log.info("Successfull login")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s10.png")
        newmessage = HomePage(self.driver)
        newmessage.getnewMessage().click()
        time.sleep(3)
        log.info("Entering Sender Email")
        senderName = HomePage(self.driver)
        senderName.getsender().send_keys("arpan.dey@celebaltech.com")
        log.info("Entering Subject")
        subject = HomePage(self.driver)
        subject.getsubject().send_keys("Test")
        log.info("Entering message body")
        messageBody = HomePage(self.driver)
        messageBody.getmessageBody().send_keys("Test Automation Demo")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s11.png")
        send = HomePage(self.driver)
        send.getsend().click()
        time.sleep(5)
        log.info("Message successfully send")
        newmessage.getnewMessage().click()
        time.sleep(3)
        log.info("Entering Sender Email")
        senderName.getsender().send_keys("arpan.dey@celebaltech.com")
        log.info("Entering Subject")
        subject.getsubject().send_keys("Test")
        log.info("Bold enabled")
        Bold = HomePage(self.driver)
        Bold.make_bold().click()
        log.info("Italic enabled")
        Italic = HomePage(self.driver)
        Italic.make_italic().click()
        log.info("Entering message body")
        messageBody.getmessageBody().send_keys("Test Automation Demo")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s12.png")
        send.getsend().click()
        time.sleep(5)
        log.info("Message successfully send")
        newmessage.getnewMessage().click()
        time.sleep(3)
        log.info("Entering Sender Email")
        senderName.getsender().send_keys("arpan.dey@celebaltech.com")
        log.info("Entering message body")
        messageBody.getmessageBody().send_keys("Test Automation Demo")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s13.png")
        send.getsend().click()
        time.sleep(3)
        fsend = HomePage(self.driver)
        fsend.final_send().click()
        log.info("Message send without subject")
        time.sleep(5)
        newmessage.getnewMessage().click()
        log.info("Entering Subject")
        subject.getsubject().send_keys("Test")
        log.info("Entering message body")
        messageBody.getmessageBody().send_keys("Test Automation Demo")
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s14.png")
        send.getsend().click()
        time.sleep(3)
        log.info("Message not sent")
        text = HomePage(self.driver)
        errorMsg = text.getErrorMessage().text
        log.info(errorMsg)
        ss.capture_screenshot("C:\\Users\Arpan Dey\PycharmProjects\Gmail_Automation\Screenshots\s15.png")
