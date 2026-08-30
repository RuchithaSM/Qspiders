from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Representative Page Object for checkout validation."""

    CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Checkout')]"
    )

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
