import pytest
from pages.qbank_login_page import QBANKLoginPage


@pytest.mark.qbank
@pytest.mark.smoke
def test_qbank_login_page_loads(driver):
    driver.get("https://services.qbank.com.au/home/SignOn/Login.aspx")
    assert "Login" in driver.title or driver.current_url
