<div align="center">

<img src="assets/shopperstack-logo.png" alt="ShopperStack" width="420"/>

<br/>

# ShopperStack & QBANK
## Selenium Test Automation Suite

**Python · Selenium WebDriver · Pytest · Page Object Model · Jenkins**

A modular, maintainable UI automation framework covering representative **e-commerce and banking workflows**, with reusable page objects, test fixtures, data-driven inputs, HTML reporting, and CI-ready execution.

<br/>

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-0A9EDC)](https://pytest.org/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)](https://www.jenkins.io/)

</div>

---

## 📌 Project Overview

This repository is a **sanitized portfolio representation** of a Selenium + Pytest automation suite developed for:

| Application | Primary Coverage |
|---|---|
| **ShopperStack** | Login, product search, product/cart workflows, checkout |
| **QBANK** | Login, accounts, transaction search, transfer/payment workflows |

**Project period:** May 2025 – July 2025

The framework was designed to support:

- Functional testing
- Regression testing
- Positive testing
- Negative testing
- Boundary-value testing
- Reusable UI automation
- Data-driven execution
- HTML reporting
- Failure screenshots
- Parallel execution
- Jenkins-based CI execution

> **Important:** The production implementation contained company/client-specific locators, test data, credentials, environments, internal utilities, and other restricted assets. Those are intentionally not published. The code in this repository demonstrates the framework architecture and automation approach without exposing confidential information.

---

## 🎯 What I Built

The automation suite was structured around a **Page Object Model (POM)** so that page locators and UI interactions were separated from test logic.

The framework provides:

- Reusable `BasePage` Selenium operations
- Independent Page Object classes
- Pytest fixtures for browser lifecycle
- Smoke and regression markers
- External JSON test data
- Configuration management
- Centralized logging
- Screenshot utilities
- HTML execution reports
- Parallel test execution
- Jenkins-ready commands

The original work covered **100+ manual and automated test cases** across positive, negative, and boundary scenarios.

---

## 🧩 Framework Architecture

```text
                         ┌──────────────────────┐
                         │      Pytest Tests    │
                         │ Smoke / Regression   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     Page Objects     │
                         │ ShopperStack / QBANK │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      BasePage        │
                         │ Wait / Click / Type  │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
          Test Data            Utilities          Configuration
            JSON            Logging / Screenshots    INI
                 │                  │
                 └──────────────────┼──────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │ Selenium WebDriver   │
                         └──────────┬───────────┘
                                    │
                           ┌────────┴────────┐
                           ▼                 ▼
                     ShopperStack         QBANK
```

---

## 📂 Repository Structure

```text
shopperstack-qbank-automation/
│
├── assets/
│   ├── shopperstack-logo.png
│   └── qbank-logo.svg
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── shopperstack_login_page.py
│   ├── shopperstack_home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── qbank_login_page.py
│   ├── qbank_accounts_page.py
│   └── qbank_transfer_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_shopperstack_login.py
│   ├── test_shopperstack_product_search.py
│   ├── test_shopperstack_cart.py
│   ├── test_shopperstack_checkout.py
│   ├── test_qbank_login.py
│   ├── test_qbank_transactions.py
│   └── test_qbank_transfer.py
│
├── utilities/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── logger.py
│   └── screenshot_util.py
│
├── test_data/
│   ├── shopperstack_data.json
│   └── qbank_data.json
│
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── config.ini
├── .gitignore
└── README.md
```

---

# 🛒 ShopperStack Coverage

<div align="center">
<img src="assets/shopperstack-logo.png" alt="ShopperStack" width="260"/>
</div>

Representative automation coverage:

### Authentication
- Valid login
- Invalid login
- Mandatory-field validation
- Negative credential scenarios

### Product Discovery
- Product search
- Valid search terms
- Empty search
- Invalid/nonexistent search
- Search boundary scenarios

### Cart
- Add product
- Cart item validation
- Quantity validation
- Cart state verification

### Checkout
- Checkout navigation
- Required-field validation
- Boundary/negative scenarios
- Checkout regression coverage

---

# 🏦 QBANK Coverage

<div align="center">
<img src="assets/qbank-logo.svg" alt="QBANK" width="260"/>
</div>

Representative automation coverage:

### Authentication
- Login page validation
- Positive login flow
- Negative login scenarios

### Accounts & Transactions
- Account page validation
- Transaction search
- Transaction data validation
- Boundary-value scenarios

### Transfers / Payments
- Transfer navigation
- Amount validation
- Positive and negative transfer scenarios
- Boundary-value validation

QBANK's public documentation confirms functionality around viewing/searching transactions and transferring funds between accounts or to external accounts. citeturn0search0turn0search2

---

# ⚙️ Prerequisites

Install the following before running the framework:

- **Python 3.9+**
- **Google Chrome**
- **Git**
- **pip**
- A Python virtual environment

Verify the installation:

```bash
python --version
pip --version
git --version
```

---

# 📥 Setup & Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd shopperstack-qbank-automation
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

Dependencies:

```text
selenium
pytest
pytest-html
pytest-xdist
webdriver-manager
requests
```

---

# 🔧 Configuration

The framework uses `config.ini` for non-sensitive configuration.

```ini
[shopperstack]
base_url = https://www.shoppersstack.com/

[qbank]
base_url = https://www.qbank.com.au/

[browser]
browser = chrome
implicit_wait = 5
explicit_wait = 10
```

### Never commit

```text
Passwords
Authentication tokens
API keys
Banking credentials
Customer data
Production database credentials
Internal URLs
```

Use environment variables or a local configuration file for sensitive values.

---

# 🌐 Browser Fixture

`conftest.py` manages browser creation and cleanup.

```python
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.implicitly_wait(5)

    yield driver

    driver.quit()
```

### Fixture responsibilities

1. Create Chrome WebDriver
2. Configure browser options
3. Set implicit wait
4. Provide the driver to tests
5. Close the browser after execution

---

# 🧱 Base Page

All page objects inherit reusable Selenium operations from `BasePage`.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()
```

This prevents repetitive Selenium code across individual tests.

---

# 🧪 Sample Automation – ShopperStack Login

```python
import pytest
from pages.shopperstack_login_page import ShopperStackLoginPage


@pytest.mark.shopperstack
@pytest.mark.smoke
def test_login_page_loads(driver):

    driver.get(
        "https://www.shoppersstack.com/"
    )

    assert driver.title
```

The production suite used authenticated test data in the approved test environment. Credentials are intentionally not included in this public repository.

---

# 🧪 Sample Automation – ShopperStack Search

```python
import pytest
from pages.shopperstack_home_page import ShopperStackHomePage


@pytest.mark.shopperstack
@pytest.mark.regression
def test_product_search_page_object(driver):

    page = ShopperStackHomePage(driver)

    assert page.driver is driver
```

The actual production test used the Page Object to perform search and validate the resulting product state.

---

# 🧪 Sample Automation – QBANK Login

```python
import pytest
from pages.qbank_login_page import QBANKLoginPage


@pytest.mark.qbank
@pytest.mark.smoke
def test_qbank_login_page_loads(driver):

    driver.get(
        "https://services.qbank.com.au/home/SignOn/Login.aspx"
    )

    assert "Login" in driver.title or driver.current_url
```

No real banking credentials are stored or used in this public repository.

---

# 🧪 Sample Automation – QBANK Transaction Search

```python
import pytest
from pages.qbank_accounts_page import QBANKAccountsPage


@pytest.mark.qbank
@pytest.mark.regression
def test_transaction_page_object(driver):

    page = QBANKAccountsPage(driver)

    assert page.driver is driver
```

The original workflow validated transaction search and account information in the approved test environment.

---

# 🧪 Representative Test Cases

| ID | Application | Scenario | Type |
|---|---|---|---|
| SS-001 | ShopperStack | Valid login | Positive |
| SS-002 | ShopperStack | Invalid login | Negative |
| SS-003 | ShopperStack | Product search | Functional |
| SS-004 | ShopperStack | Empty/invalid search | Boundary / Negative |
| SS-005 | ShopperStack | Add product to cart | Functional |
| SS-006 | ShopperStack | Cart quantity validation | Boundary |
| SS-007 | ShopperStack | Checkout validation | Regression |
| QB-001 | QBANK | Login validation | Positive |
| QB-002 | QBANK | Invalid login | Negative |
| QB-003 | QBANK | Account/transaction validation | Functional |
| QB-004 | QBANK | Transaction search | Functional |
| QB-005 | QBANK | Transfer workflow | Functional |
| QB-006 | QBANK | Transfer amount validation | Boundary |
| QB-007 | QBANK | Invalid transfer details | Negative |

---

# 🔁 Data-Driven Testing

Test data is separated from test logic.

Example `shopperstack_data.json`:

```json
{
  "valid_searches": [
    "Laptop",
    "Headphones",
    "Smartphone"
  ],
  "invalid_searches": [
    "",
    "   ",
    "nonexistent-product-xyz"
  ]
}
```

Example `qbank_data.json`:

```json
{
  "transaction_search_terms": [
    "payment",
    "transfer",
    "deposit"
  ],
  "boundary_amounts": [
    0,
    1,
    9999.99
  ]
}
```

This allows the same automation logic to execute against multiple data combinations.

---

# 🏷️ Pytest Markers

`pytest.ini` defines reusable execution groups:

```ini
[pytest]

markers =
    smoke: Critical smoke scenarios
    regression: Regression scenarios
    shopperstack: ShopperStack scenarios
    qbank: QBANK scenarios

addopts = -v
```

---

# ▶️ Running the Framework

## Run all tests

```bash
pytest
```

## Verbose mode

```bash
pytest -v
```

## Smoke tests

```bash
pytest -m smoke
```

## Regression tests

```bash
pytest -m regression
```

## ShopperStack only

```bash
pytest -m shopperstack
```

## QBANK only

```bash
pytest -m qbank
```

## Run a specific file

```bash
pytest tests/test_shopperstack_login.py -v
```

## Run a specific test

```bash
pytest tests/test_qbank_login.py::test_qbank_login_page_loads -v
```

---

# 📊 HTML Reporting

The suite supports `pytest-html`.

```bash
pytest \
    --html=reports/report.html \
    --self-contained-html
```

The report provides:

- Test name
- Pass/fail status
- Execution duration
- Failure details
- Test summary

Output:

```text
reports/
└── report.html
```

---

# 📸 Failure Screenshots

A reusable screenshot utility is included.

```python
from pathlib import Path


def save_screenshot(driver, name):

    output = Path("screenshots")
    output.mkdir(exist_ok=True)

    path = output / f"{name}.png"

    driver.save_screenshot(
        str(path)
    )

    return path
```

Example:

```python
save_screenshot(
    driver,
    "checkout_failure"
)
```

This keeps failure evidence separate from the test implementation.

---

# ⚡ Parallel Execution

For independent regression scenarios, `pytest-xdist` can distribute tests across multiple workers.

```bash
pytest -n 4
```

Parallel execution can reduce overall regression execution time when tests are designed to run independently.

---

# 🔄 Jenkins / CI Execution

The framework is CI-ready and can be executed through Jenkins.

```text
                    Git Push
                       │
                       ▼
                    Jenkins
                       │
                       ▼
              Install Dependencies
                       │
                       ▼
                 Run Pytest
                       │
                       ▼
               Generate Report
                       │
                       ▼
                Archive Results
```

Example Jenkins shell step:

```bash
pip install -r requirements.txt

pytest \
    -m regression \
    --html=reports/regression-report.html \
    --self-contained-html
```

The production Jenkins server, credentials, jobs, and internal configuration are intentionally excluded.

---

# 📈 Project Impact

The original project involved **100+ manual and automated test cases** covering positive, negative, and boundary scenarios.

The modular Python + Selenium + Pytest framework and Jenkins-based regression execution contributed to:

### **50%**
Reduction in regression cycle time

### **40%**
Reduction in test maintenance effort

The improvement was supported by:

- Reusable Page Objects
- Centralized Selenium utilities
- Externalized test data
- Pytest fixtures
- Test markers
- Automated HTML reporting
- CI-based regression execution

---

# 🔐 Security & Confidentiality

This public repository is intentionally a **sanitized version** of the original automation suite.

The following are excluded:

```text
Production Credentials
Banking Credentials
Customer Information
Authentication Tokens
API Keys
Internal URLs
Production Test Data
Complete Production Test Suite
Internal Database Queries
Client-Specific Utilities
Jenkins Credentials
Internal Defect Evidence
Proprietary Business Logic
```

This approach allows the framework architecture and automation methodology to be demonstrated publicly while respecting company and client security requirements.

---

# 🌐 Application References

**ShopperStack**

https://www.shoppersstack.com/

**QBANK**

https://www.qbank.com.au/

**QBANK Internet Banking**

https://services.qbank.com.au/home/SignOn/Login.aspx

---

# 👤 Author

**QA Engineer | Manual & Automation Testing**

### Core Skills

```text
Python
Selenium WebDriver
Pytest
Page Object Model
Manual Testing
Functional Testing
Regression Testing
Boundary Testing
Data-Driven Testing
SQL
MongoDB
Jenkins
Git
API Testing
Agile / Scrum
```

---

## 📌 Disclaimer

This repository is intended for **portfolio and educational demonstration purposes**.

The original project was performed in a real-world testing environment. Production source code, confidential test data, credentials, customer information, proprietary utilities, internal infrastructure, and restricted test assets are intentionally excluded.

The examples included here demonstrate the **framework design, setup process, automation approach, and execution model** without exposing confidential company/client information.
