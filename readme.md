# ShopperStack & QBANK – Selenium Test Automation Suite

<p align="center">
  <b>Python • Selenium • Pytest • Page Object Model • Jenkins</b>
</p>

A sanitized portfolio version of a **Selenium + Pytest automation framework** covering representative e-commerce and banking workflows across **ShopperStack** and **QBANK**.

## 📌 Project Scope

The suite is designed around:

- Functional testing
- Regression testing
- Positive, negative, and boundary testing
- UI automation
- Data-driven testing
- Reusable Page Object Model components
- HTML test reporting
- Jenkins-based execution

Representative workflows include:

**ShopperStack**
- Login
- Product search
- Product validation
- Cart
- Checkout

**QBANK**
- Login
- Account/transaction validation
- Transaction search
- Transfer/payment workflows

QBANK's public documentation describes online banking capabilities including viewing/searching transactions and transferring funds. citeturn0search0turn0search7

> **Confidentiality:** The original project contained proprietary test cases, credentials, test data, internal environments, and client-specific implementation details. This repository intentionally contains only sanitized framework examples.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Automation development |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and fixtures |
| Page Object Model | Maintainable framework design |
| pytest-html | HTML reporting |
| pytest-xdist | Parallel execution |
| WebDriver Manager | Driver management |
| Jenkins | CI/CD execution |
| Git / GitHub | Version control |

---

## 🏗️ Framework Architecture

```text
                    Pytest Test Cases
                           │
                           ▼
                    Page Object Layer
                           │
                           ▼
                     Base Page
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        Utility Layer              Test Data
              │
              ▼
        Selenium WebDriver
              │
        ┌─────┴─────┐
        ▼           ▼
  ShopperStack    QBANK
```

The framework separates test logic, page interactions, reusable utilities, and test data to improve maintainability and reduce duplicated Selenium code.

---

## 📂 Project Structure

```text
shopperstack-qbank-automation/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
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
│   ├── test_product_search.py
│   ├── test_cart.py
│   ├── test_checkout.py
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
└── README.md
```

---

## ⚙️ Prerequisites

Install:

- Python 3.9+
- Google Chrome
- Git
- pip
- Virtual environment

Verify:

```bash
python --version
pip --version
git --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd shopperstack-qbank-automation
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
selenium
pytest
pytest-html
pytest-xdist
webdriver-manager
requests
```

---

## 🔧 Configuration

Example `config.ini`:

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

Never store:

- Passwords
- API keys
- Authentication tokens
- Banking credentials
- Production test data
- Internal URLs

in GitHub.

---

## 🧪 Pytest Configuration

Example `pytest.ini`:

```ini
[pytest]

markers =
    smoke: Critical smoke scenarios
    regression: Regression scenarios
    shopperstack: ShopperStack test scenarios
    qbank: QBANK test scenarios

addopts = -v
```

---

## 🌐 WebDriver Fixture

Example `conftest.py`:

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

The fixture creates and tears down the browser automatically for each test.

---

## 🧱 Page Object Model

Common Selenium operations are centralized in `BasePage`.

Example:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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
```

Individual page classes then contain application-specific locators and workflows.

---

## 🛒 Representative ShopperStack Test

```python
import pytest


@pytest.mark.shopperstack
@pytest.mark.smoke
def test_product_search(driver):

    driver.get(
        "https://www.shoppersstack.com/"
    )

    # Page Object methods would handle:
    # 1. Login
    # 2. Product search
    # 3. Product selection
    # 4. Validation

    assert driver.title
```

---

## 🏦 Representative QBANK Test

QBANK provides online banking functionality including account and transaction access and transfer/payment capabilities. citeturn0search0turn0search7

```python
import pytest


@pytest.mark.qbank
@pytest.mark.regression
def test_qbank_login_page_loads(driver):

    driver.get(
        "https://www.qbank.com.au/"
    )

    assert driver.title
```

> Banking credentials and authenticated customer information are never included in the public repository.

---

## 📋 Representative Test Coverage

| ID | Scenario | Application | Type |
|---|---|---|---|
| SS-001 | Login with valid credentials | ShopperStack | Positive |
| SS-002 | Invalid login validation | ShopperStack | Negative |
| SS-003 | Product search | ShopperStack | Functional |
| SS-004 | Search boundary validation | ShopperStack | Boundary |
| SS-005 | Add product to cart | ShopperStack | Functional |
| SS-006 | Cart quantity validation | ShopperStack | Functional |
| SS-007 | Checkout validation | ShopperStack | Regression |
| QB-001 | Login validation | QBANK | Positive |
| QB-002 | Invalid login | QBANK | Negative |
| QB-003 | Account/transaction validation | QBANK | Functional |
| QB-004 | Transaction search | QBANK | Functional |
| QB-005 | Internal transfer validation | QBANK | Functional |
| QB-006 | Payment/transfer validation | QBANK | Regression |

---

## 📊 Test Execution & Reporting

Run the complete suite:

```bash
pytest
```

Verbose execution:

```bash
pytest -v
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run ShopperStack tests:

```bash
pytest -m shopperstack
```

Run QBANK tests:

```bash
pytest -m qbank
```

Generate an HTML report:

```bash
pytest \
    --html=reports/report.html \
    --self-contained-html
```

---

## ⚡ Parallel Execution

For independent regression scenarios:

```bash
pytest -n 4
```

Parallel execution can reduce overall suite execution time when scenarios are designed to run independently.

---

## 📸 Failure Screenshots

The framework can capture screenshots when an automation scenario fails.

Example utility:

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

---

## 🔄 Jenkins Integration

The framework can be executed as part of a Jenkins regression pipeline.

```text
Git Push
   ↓
Jenkins
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Generate HTML Report
   ↓
Archive Results
```

Example Jenkins command:

```bash
pip install -r requirements.txt

pytest \
    -m regression \
    --html=reports/regression-report.html \
    --self-contained-html
```

---

## 📈 Project Outcome

The suite covered **100+ manual and automated test cases** across positive, negative, and boundary scenarios.

The modular Python + Selenium + Pytest framework, combined with reusable components and Jenkins execution, contributed to:

- **50% reduction in regression cycle time**
- **40% reduction in test maintenance effort**

Structured HTML execution reports and standardized severity classifications were used to make test results and defect reporting more consistent.

---

## 🔐 Confidentiality

This public repository is a **sanitized portfolio representation**.

The following are intentionally excluded:

```text
Production Credentials
Banking Credentials
Customer Information
Internal URLs
API Keys
Authentication Tokens
Proprietary Test Data
Complete Production Test Suite
Internal Database Queries
Client-Specific Infrastructure
Jenkins Credentials
Internal Defect Evidence
```

The examples in this repository demonstrate the framework structure and automation approach without exposing confidential project information.

---

## 🌐 Applications

- [ShopperStack](https://www.shoppersstack.com/)
- [QBANK](https://www.qbank.com.au/)

---

## 👤 Author

**QA Engineer | Manual & Automation Testing**

**Core Skills**

```text
Python
Selenium
Pytest
Page Object Model
Manual Testing
Functional Testing
Regression Testing
SQL
MongoDB
Jenkins
Git
API Testing
Agile/Scrum
```

---

## 📌 Disclaimer

This repository is intended for portfolio and educational demonstration purposes. The production implementation, credentials, proprietary test assets, customer information, and internal infrastructure are not included.
