from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QBANKTransferPage(BasePage):
    """Representative Page Object for transfer workflow."""

    TRANSFER_LINK = (
        By.XPATH,
        "//a[contains(., 'Transfer')]"
    )
    AMOUNT = (
        By.CSS_SELECTOR,
        "input[name='amount']"
    )

    def open_transfer(self):
        self.click(self.TRANSFER_LINK)

    def enter_amount(self, amount):
        self.type_text(self.AMOUNT, str(amount))
