import pytest
from pages.shopperstack_home_page import ShopperStackHomePage


@pytest.mark.shopperstack
@pytest.mark.regression
def test_product_search_page_object(driver):
    page = ShopperStackHomePage(driver)
    assert page.driver is driver
