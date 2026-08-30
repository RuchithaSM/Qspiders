from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QBANKLoginPage(BasePage):
    """Representative Page Object for QBANK login."""

    MEMBER_NUMBER = (By.ID, "MemberNumber")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def login(self, member_number, password):
        self.type_text(self.MEMBER_NUMBER, member_number)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
