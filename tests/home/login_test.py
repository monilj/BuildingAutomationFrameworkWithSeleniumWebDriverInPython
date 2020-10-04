from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from pages.home.LoginPage import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()
