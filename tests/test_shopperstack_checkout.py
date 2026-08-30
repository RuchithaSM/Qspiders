import pytest
from pages.checkout_page import CheckoutPage


@pytest.mark.shopperstack
@pytest.mark.regression
def test_checkout_page_object_is_available(driver):
    page = CheckoutPage(driver)
    assert page.driver is driver
