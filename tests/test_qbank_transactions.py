import pytest
from pages.qbank_accounts_page import QBANKAccountsPage


@pytest.mark.qbank
@pytest.mark.regression
def test_qbank_accounts_page_object_is_available(driver):
    page = QBANKAccountsPage(driver)
    assert page.driver is driver
