from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QBANKAccountsPage(BasePage):
    """Representative Page Object for account/transaction workflows."""

    ACCOUNTS_LINK = (
        By.XPATH,
        "//a[contains(., 'Accounts')]"
    )
    TRANSACTION_SEARCH = (
        By.CSS_SELECTOR,
        "input[type='search']"
    )

    def open_accounts(self):
        self.click(self.ACCOUNTS_LINK)

    def search_transactions(self, value):
        self.type_text(self.TRANSACTION_SEARCH, value)
