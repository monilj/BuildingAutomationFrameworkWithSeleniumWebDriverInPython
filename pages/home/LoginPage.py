from selenium.webdriver.common.by import By
from base.CustomMethodForMethodsProvidedBySeleniumClass import CustomMethodForMethodsProvidedBySeleniumClass


class LoginPage(CustomMethodForMethodsProvidedBySeleniumClass):

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # def loginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickOnLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickOnLoginButton(self):
        self.elementClick(self._login_button, locatorType="Name")

    def login(self, email, password):
        self.clickOnLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickOnLoginButton()
