import pytest
from pages.qbank_transfer_page import QBANKTransferPage


@pytest.mark.qbank
@pytest.mark.regression
def test_qbank_transfer_page_object_is_available(driver):
    page = QBANKTransferPage(driver)
    assert page.driver is driver
