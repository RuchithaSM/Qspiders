<div align="center">

<img src="assets/freshbus-logo.png" alt="Fresh Bus Logo" width="180"/>

# Fresh Bus – Selenium Pytest Automation Framework

**Web Application QA & Test Automation Project**

`Python` · `Selenium` · `Pytest` · `Page Object Model` · `Jenkins`

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-0A9EDC?style=for-the-badge)](https://pytest.org/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?style=for-the-badge&logo=jenkins&logoColor=white)](https://www.jenkins.io/)

</div>

> **Portfolio Note**
> This repository is a sanitized representation of a real-world QA automation project. Proprietary source code, credentials, internal environments, production data, and restricted project assets are intentionally excluded.

---

## 🧭 Quick Navigation

| Section | Section |
|---|---|
| [📌 Project Overview](#-project-overview) | [👨‍💻 My Role](#-my-role) |
| [🛠️ Technology Stack](#️-technology-stack) | [🏗️ Framework Architecture](#️-framework-architecture) |
| [📂 Project Structure](#-project-structure) | [⚙️ Setup & Installation](#️-prerequisites) |
| [🧪 Automation Examples](#-webdriver-setup) | [📋 Test Scenarios](#-representative-test-scenarios) |
| [📊 Reporting](#-html-reporting) | [🔄 CI/CD](#-cicd-integration) |
| [🐞 Defect Management](#-defect-management) | [🔐 Security & Confidentiality](#-security--confidentiality) |
| [📈 Outcomes](#-project-outcomes) | [👤 Author](#-author) |

---

### 📌 Project Overview

This repository contains a **sanitized version of the Selenium + Pytest automation framework** developed for testing the Fresh Bus web application.

Fresh Bus is an online bus-booking platform supporting route search, travel-date selection, bus availability, seat selection, passenger information, and booking-related workflows.

The project was undertaken through **Robowaves, a client of QSpiders**, as part of the industry-project exposure provided to trainees.

I worked as a **QA Trainee** in a 15-member project team, including one team lead. My responsibilities covered functional testing, regression testing, exploratory testing, UI testing, cross-browser validation, automation, defect management, and UI-to-backend data validation.

> **Note:** The production project contained proprietary test cases, internal environments, credentials, APIs, database information, test data, and other client-specific assets. These have intentionally not been published. This repository demonstrates the framework architecture, representative automation code, and testing approach.

---

## 👨‍💻 My Role

### QA Trainee

**Project:** Fresh Bus  
**Organization:** Robowaves  
**Engagement:** Robowaves was a client of QSpiders  
**Duration:** July 2025 – August 2025  
**Team Size:** 15 members including 1 Team Lead

### Responsibilities

- Analyzed requirements and acceptance criteria.
- Designed and executed functional test cases.
- Performed regression and exploratory testing.
- Automated selected regression and functional scenarios using Selenium and Pytest.
- Developed reusable Page Object Model components.
- Validated UI workflows across browsers.
- Created reusable test utilities and fixtures.
- Performed positive, negative, and boundary testing.
- Validated booking information against backend data where required.
- Reported and tracked defects using FireFlink.
- Performed defect retesting and regression validation.
- Collaborated with developers and product stakeholders.
- Supported release-readiness validation.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Automation programming |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework and execution |
| Page Object Model | Maintainable framework architecture |
| pytest-html | HTML test reporting |
| pytest-xdist | Parallel test execution |
| WebDriver Manager | Browser-driver management |
| Git | Version control |
| GitHub | Source-code management |
| Jenkins | CI/CD test execution |
| FireFlink | Defect management |
| Oracle SQL | Backend data validation |
| MongoDB | Backend data validation |

---

## 🏗️ Framework Architecture

The framework follows a **Page Object Model (POM)** architecture.

```text
                    ┌─────────────────────┐
                    │    Test Scenarios   │
                    │       Pytest        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Page Objects    │
                    │      Selenium       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Base Page       │
                    │ Reusable Operations  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Fresh Bus Web App   │
                    └─────────────────────┘
```

Supporting components:

```text
Test Cases
    │
    ├── Page Objects
    │
    ├── Test Data
    │
    ├── Configuration
    │
    ├── Utilities
    │
    ├── Logging
    │
    └── Reporting
```

---

## 📂 Project Structure

```text
freshbus-automation/
│
├── assets/
│   └── freshbus-logo.png
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   ├── seat_selection_page.py
│   └── booking_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_home_page.py
│   ├── test_bus_search.py
│   ├── test_seat_selection.py
│   └── test_booking_validation.py
│
├── utilities/
│   ├── __init__.py
│   ├── config_reader.py
│   ├── logger.py
│   └── screenshot_util.py
│
├── test_data/
│   └── sample_routes.json
│
├── reports/
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── config.ini
└── README.md
```

---

## 🔄 Test Automation Flow

```text
Requirement Analysis
        ↓
Test Scenario Identification
        ↓
Test Case Design
        ↓
Automation Feasibility
        ↓
Page Object Development
        ↓
Test Script Development
        ↓
Test Data Preparation
        ↓
Pytest Execution
        ↓
Failure Analysis
        ↓
Defect Reporting
        ↓
Fix Verification
        ↓
Regression Testing
        ↓
HTML Reporting
        ↓
Release Validation
```

---

## ⚙️ Prerequisites

The following software is required:

- Python 3.9+
- Google Chrome
- Git
- pip
- Virtual Environment

Verify Python:

```bash
python --version
```

Verify pip:

```bash
pip --version
```

Verify Git:

```bash
git --version
```

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd freshbus-automation
```

---

### 2. Create a Virtual Environment

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

---

### 3. Install Dependencies

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

## 🌐 Application Configuration

Example `config.ini`:

```ini
[application]
base_url = https://www.freshbus.com/

[browser]
browser = chrome
implicit_wait = 5
explicit_wait = 10
```

Sensitive information such as:

- usernames
- passwords
- API keys
- authentication tokens
- internal URLs
- database credentials

must not be stored in the repository.

---

## 🧪 Pytest Configuration

Example `pytest.ini`:

```ini
[pytest]

markers =
    smoke: Critical smoke scenarios
    regression: Regression scenarios
    booking: Booking workflow scenarios

addopts =
    -v
    --html=reports/report.html
    --self-contained-html
```

---

## 🌐 WebDriver Setup

The framework uses Selenium WebDriver with WebDriver Manager.

`conftest.py`

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

The fixture:

1. Creates the browser.
2. Configures browser options.
3. Initializes Selenium WebDriver.
4. Makes the driver available to the test.
5. Automatically closes the browser after execution.

---

## 🧱 Base Page

Common Selenium operations are centralized inside the Base Page.

`pages/base_page.py`

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    def open(self, url):

        self.driver.get(url)

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

    def type_text(self, locator, text):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        element.send_keys(text)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_visible(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.is_displayed()
```

The purpose of the Base Page is to avoid repeating common Selenium operations across individual page classes.

---

## 🏠 Home Page Object

`pages/home_page.py`

```python
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    FROM_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'From')]"
    )

    TO_INPUT = (
        By.XPATH,
        "//input[contains(@placeholder,'To')]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Search')]"
    )

    def enter_source(self, source):

        self.type_text(
            self.FROM_INPUT,
            source
        )

    def enter_destination(self, destination):

        self.type_text(
            self.TO_INPUT,
            destination
        )

    def search_buses(self):

        self.click(
            self.SEARCH_BUTTON
        )
```

> The locators above are representative examples. Production locators and proprietary implementation details are intentionally excluded.

---

## 🧪 Sample Test Case – Home Page

`tests/test_home_page.py`

```python
import pytest


BASE_URL = "https://www.freshbus.com/"


@pytest.mark.smoke
def test_home_page_loads(driver):

    driver.get(BASE_URL)

    assert "Fresh" in driver.title
```

### Validation

The test verifies that:

- The application is accessible.
- The home page loads.
- The expected page title is displayed.

---

## 🧪 Sample Test Case – Search Fields

```python
import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
def test_search_fields_are_available(driver):

    driver.get(
        "https://www.freshbus.com/"
    )

    home = HomePage(driver)

    assert home.is_visible(
        home.FROM_INPUT
    )

    assert home.is_visible(
        home.TO_INPUT
    )

    assert home.is_visible(
        home.SEARCH_BUTTON
    )
```

---

## 🧪 Sample Test Case – Bus Search

```python
import pytest

from pages.home_page import HomePage


@pytest.mark.booking
def test_bus_search(driver):

    driver.get(
        "https://www.freshbus.com/"
    )

    home = HomePage(driver)

    home.enter_source(
        "Bangalore"
    )

    home.enter_destination(
        "Tirupati"
    )

    home.search_buses()

    assert (
        driver.current_url
        != "https://www.freshbus.com/"
    )
```

---

## 🧪 Negative Testing

Negative scenarios were also included as part of the testing strategy.

Examples:

```text
1. Search without source
2. Search without destination
3. Same source and destination
4. Invalid travel date
5. Invalid passenger information
6. Invalid mobile number
7. Mandatory field validation
8. Invalid booking information
```

Example:

```python
import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_search_without_destination(driver):

    driver.get(
        "https://www.freshbus.com/"
    )

    home = HomePage(driver)

    home.enter_source(
        "Bangalore"
    )

    home.search_buses()

    # Production implementation validates
    # the application's actual validation message.

    assert driver.current_url is not None
```

---

## 🔁 Data-Driven Testing

Pytest parameterization can be used to execute the same workflow against multiple routes.

```python
import pytest

from pages.home_page import HomePage


@pytest.mark.parametrize(
    "source,destination",
    [
        ("Bangalore", "Tirupati"),
        ("Hyderabad", "Vijayawada"),
        ("Chennai", "Pondicherry")
    ]
)
def test_multiple_routes(
    driver,
    source,
    destination
):

    driver.get(
        "https://www.freshbus.com/"
    )

    home = HomePage(driver)

    home.enter_source(source)

    home.enter_destination(destination)

    home.search_buses()

    assert driver.current_url is not None
```

This approach reduces duplicated test code and makes it easier to extend route coverage.

---

## 📋 Representative Test Scenarios

| Test ID | Test Scenario | Type |
|---|---|---|
| FB-001 | Verify application home page loads | Smoke |
| FB-002 | Verify From field | Functional |
| FB-003 | Verify To field | Functional |
| FB-004 | Search buses using valid route | Functional |
| FB-005 | Search without source | Negative |
| FB-006 | Search without destination | Negative |
| FB-007 | Validate same source/destination | Negative |
| FB-008 | Validate travel-date selection | Functional |
| FB-009 | Validate available bus results | Functional |
| FB-010 | Validate seat-selection workflow | Functional |
| FB-011 | Validate passenger information | Functional |
| FB-012 | Validate mandatory fields | Negative |
| FB-013 | Validate invalid passenger information | Negative |
| FB-014 | Validate booking summary | Regression |
| FB-015 | Validate fare information | Regression |
| FB-016 | Validate booking status | Regression |
| FB-017 | Cross-browser booking validation | Compatibility |
| FB-018 | UI/backend booking-data validation | Integration |

---

## 📸 Screenshot Capture

Screenshots can be captured automatically when a test fails.

Example:

```python
import os

import pytest


@pytest.hookimpl(
    hookwrapper=True
)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and report.failed
    ):

        driver = item.funcargs.get(
            "driver"
        )

        if driver:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            driver.save_screenshot(
                f"screenshots/"
                f"{item.name}.png"
            )
```

This provides visual evidence when an automation scenario fails.

---

## 📊 HTML Reporting

The framework can generate HTML execution reports using `pytest-html`.

Run:

```bash
pytest \
    --html=reports/report.html \
    --self-contained-html
```

The report provides information such as:

- Test name
- Test status
- Execution duration
- Failure information
- Test summary

Generated report:

```text
reports/
└── report.html
```

---

## ⚡ Parallel Test Execution

For larger regression suites, tests can be distributed across multiple workers using `pytest-xdist`.

```bash
pytest -n 4
```

This allows multiple independent tests to execute concurrently and can reduce overall regression execution time when the test suite is suitable for parallel execution.

---

## 🏷️ Test Markers

Tests can be grouped using Pytest markers.

### Smoke

```bash
pytest -m smoke
```

### Regression

```bash
pytest -m regression
```

### Booking

```bash
pytest -m booking
```

### All Tests

```bash
pytest
```

---

## ▶️ Running the Framework

### Run the complete suite

```bash
pytest
```

### Verbose execution

```bash
pytest -v
```

### Run a specific test file

```bash
pytest tests/test_bus_search.py -v
```

### Run a specific test

```bash
pytest tests/test_bus_search.py::test_bus_search -v
```

### Run smoke tests

```bash
pytest -m smoke
```

### Run regression tests

```bash
pytest -m regression
```

### Run with HTML report

```bash
pytest \
    --html=reports/report.html \
    --self-contained-html
```

---

## 🔄 CI/CD Integration

The automation framework was designed to support Jenkins-based execution.

A simplified CI workflow:

```text
                 Git Push
                    │
                    ▼
              Git Repository
                    │
                    ▼
                 Jenkins
                    │
                    ▼
          Install Dependencies
                    │
                    ▼
             Execute Pytest
                    │
                    ▼
            Generate Report
                    │
                    ▼
           Review Test Results
```

Example Jenkins command:

```bash
pip install -r requirements.txt

pytest \
    -m regression \
    --html=reports/regression-report.html \
    --self-contained-html
```

The production Jenkins configuration and internal CI environment are not included in this repository.

---

## 🗄️ UI & Backend Validation

For selected workflows, application data was validated beyond the UI layer.

The validation approach was:

```text
              Fresh Bus UI
                   │
                   ▼
             Application/API
                   │
                   ▼
          ┌──────────────────┐
          │ Backend Database  │
          ├──────────────────┤
          │ Oracle SQL        │
          │ MongoDB            │
          └──────────────────┘
```

Examples of data validated included:

- Booking reference
- Passenger information
- Seat information
- Journey information
- Booking status
- Fare information

The production project involved database validation as part of the QA process.

Actual:

- Database credentials
- Connection strings
- Production schemas
- Internal queries
- Production records
- Customer data

are intentionally excluded.

---

## 🐞 Defect Management

Defects identified during testing were documented and tracked through the complete defect lifecycle.

```text
Defect Identified
       ↓
Reproduce
       ↓
Document
       ↓
Assign Severity
       ↓
Log in FireFlink
       ↓
Developer Investigation
       ↓
Fix
       ↓
Retest
       ↓
Regression
       ↓
Closed / Reopened
```

Defect reports included information such as:

- Defect title
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Screenshots
- Environment information
- Retest status

---

## 🧩 Example Defect

```text
Defect ID: FB-XXX

Title:
Booking information displayed incorrectly after seat selection

Severity:
High

Module:
Booking

Steps:
1. Open Fresh Bus
2. Select source and destination
3. Select travel date
4. Select an available bus
5. Select a seat
6. Continue to booking

Expected:
Selected seat and booking information should
remain consistent throughout the booking workflow.

Actual:
Booking information displayed inconsistent data.

Status:
Retested after fix
```

> The example above is representative. Actual production defect IDs, screenshots, data, and internal details are not published.

---

## 🔐 Security & Confidentiality

This repository intentionally contains only a **sanitized representation** of the original framework.

The following are excluded due to company/client confidentiality requirements:

```text
Production Credentials
Internal URLs
Authentication Tokens
API Keys
Complete Production Test Suite
Internal API Endpoints
Database Credentials
Production Database Queries
Customer Information
Production Test Data
Internal Defect Reports
FireFlink Screenshots
Internal Project Documents
Jenkins Server Configuration
Company-Specific Utilities
Proprietary Business Logic
```

No credentials or secrets should be committed to GitHub.

Recommended `.gitignore` entries:

```gitignore
venv/
__pycache__/
*.pyc

.env
.env.*
config.local.ini

screenshots/
reports/

*.log

credentials/
secrets/
```

---

## 📈 Project Outcomes

The Fresh Bus project provided hands-on experience with:

- Real-world web application testing
- Functional testing
- Regression testing
- Exploratory testing
- Cross-browser testing
- Selenium automation
- Pytest framework development
- Page Object Model
- Reusable automation components
- Data-driven testing
- Test reporting
- Failure analysis
- Defect lifecycle management
- UI/backend data validation
- Agile sprint testing
- CI-oriented test execution

During the project, I also identified and tracked **50+ defects** and identified **18+ UI-to-backend data mismatches** through systematic validation.

---

## 🎯 Key Learning

The project provided practical experience in designing an automation framework rather than only writing individual Selenium scripts.

Key areas of learning included:

```text
Writing Maintainable Automation
             ↓
Applying Page Object Model
             ↓
Creating Reusable Components
             ↓
Managing Test Data
             ↓
Handling Dynamic Web Elements
             ↓
Debugging Failed Tests
             ↓
Generating Execution Reports
             ↓
Integrating Tests with CI
```

The focus was on making the automation suite **reusable, maintainable, scalable, and suitable for repeated regression execution**.

---

## 🌐 Application

Fresh Bus:

https://www.freshbus.com/

---

## 📌 Disclaimer

This repository is intended for **portfolio and educational demonstration purposes**.

The original project was performed in a real-world QA environment. Production source code, internal application information, proprietary test cases, credentials, customer information, and other restricted assets are intentionally excluded to comply with confidentiality and company policies.

The sample code and test scenarios in this repository demonstrate the **framework architecture and automation approach** without exposing confidential project information.

---

### 👤 Author

**Ruchitha Shivappashetty Mallikarjuna**

QA Engineer | Manual & Automation Testing

Skills:

```text
Python
Selenium
Pytest
API Testing
Functional Testing
Regression Testing
SQL
MongoDB
Jenkins
Git
FireFlink
Agile/Scrum
```
