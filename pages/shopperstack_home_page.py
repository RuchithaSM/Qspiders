from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShopperStackHomePage(BasePage):
    """Representative Page Object for product discovery."""

    SEARCH_BOX = (
        By.CSS_SELECTOR,
        "input[type='search']"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Search')]"
    )

    def search_product(self, product):
        self.type_text(self.SEARCH_BOX, product)
        self.click(self.SEARCH_BUTTON)
