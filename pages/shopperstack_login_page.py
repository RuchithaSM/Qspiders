from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShopperStackLoginPage(BasePage):
    """Representative Page Object for ShopperStack authentication."""

    USERNAME = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Login')]")

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
