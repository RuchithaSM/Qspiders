import pytest
from pages.shopperstack_login_page import ShopperStackLoginPage


@pytest.mark.shopperstack
@pytest.mark.smoke
def test_shopperstack_login_page_loads(driver):
    driver.get("https://www.shoppersstack.com/")
    assert driver.title


@pytest.mark.shopperstack
@pytest.mark.regression
def test_login_page_object_is_available(driver):
    page = ShopperStackLoginPage(driver)
    assert page.driver is driver
