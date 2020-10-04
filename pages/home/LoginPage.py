from selenium.webdriver.common.by import By
from base.CustomMethodForMethodsProvidedBySeleniumClass import CustomMethodForMethodsProvidedBySeleniumClass
import utilities.custom_logger as cl
import logging


class LoginPage(CustomMethodForMethodsProvidedBySeleniumClass):
    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickOnLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickOnLoginButton(self):
        self.elementClick(self._login_button, locatorType="Name")

    def login(self, email="", password=""):
        self.clickOnLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickOnLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()