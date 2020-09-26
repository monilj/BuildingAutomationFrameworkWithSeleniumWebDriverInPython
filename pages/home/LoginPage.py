from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def login(self, username, password):
        loginLink = self.driver.find_element(By.LINK_TEXT, self._login_link)
        loginLink.click()

        emailField = self.driver.find_element(By.ID, self._email_field)
        emailField.send_keys(username)

        passwordField = self.driver.find_element(By.ID, self._password_field)
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.NAME, self._login_button)
        loginButton.click()
