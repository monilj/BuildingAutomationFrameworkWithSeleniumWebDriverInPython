from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests:
    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        time.sleep(3)

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@email.com")

        time.sleep(3)

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("abcabc")

        loginButton = driver.find_element(By.NAME, "commit")
        time.sleep(10)
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")


loginTests = LoginTests()
loginTests.test_validLogin()
