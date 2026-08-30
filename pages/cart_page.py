from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Representative Page Object for cart validation."""

    CART_ITEMS = (
        By.CSS_SELECTOR,
        "[data-testid='cart-item']"
    )

    def has_items(self):
        return bool(self.driver.find_elements(*self.CART_ITEMS))
