import pytest
from pages.cart_page import CartPage


@pytest.mark.shopperstack
@pytest.mark.regression
def test_cart_page_object_is_available(driver):
    page = CartPage(driver)
    assert page.driver is driver
