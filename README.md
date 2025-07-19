<<<<<<< HEAD
# Web Automation Testing with Selenium and Pytest

This project demonstrates end-to-end web automation testing using Selenium and Pytest in Python.  
It automates login functionality testing on (https://www.saucedemo.com), applying best practices such as the Page Object Model (POM) for clean and maintainable test code.

---

## Features

- Automated browser testing with Selenium
- Valid and invalid login scenario tests
- Page Object Model (POM) implementation
- Reusable, modular test components using Pytest
- Automatic WebDriver setup using webdriver-manager
- Easily extendable for larger test suites

---

## Tech Stack

- **Language**: Python 3
- **Test Framework**: Pytest
- **Browser Automation**: Selenium WebDriver
- **Driver Manager**: webdriver-manager

---

## Project Structure

web-automation-testing/
¦
+-- tests/
¦ +-- test_login.py # Contains login test cases
¦
+-- pages/
¦ +-- login_page.py # Page Object class for login page
¦
+-- utils/
¦ +-- browser_setup.py # Sets up Selenium WebDriver
¦
+-- requirements.txt # Project dependencies
+-- README.md # Project documentation


---

## Setup Instructions

1. Clone the repository
`ash
git clone https://github.com/your-username/web-automation-testing.git
cd web-automation-testing

2. Install the dependencies
bash
Copy code
pip install -r requirements.txt

3. Run the tests
bash
Copy code
pytest -v tests/test_login.py


| Test Case            | Description                                            |
| -------------------- | ------------------------------------------------------ |
| 	est_valid_login   | Tests successful login with standard\_user credentials |
| 	est_invalid_login | Verifies error message for incorrect login credentials |


What I Learned:

Built a basic automation testing framework from scratch

Applied the Page Object Model for scalable automation design

Used Pytest fixtures and assertions effectively

Managed browser drivers automatically with webdriver-manager

Practiced structured coding and separation of concerns


License
This project is licensed under the MIT License.
=======
# web-automation-testing
Automated end-to-end web testing using Selenium and Python.
>>>>>>> 5d3fefad48cd9cc190ac5cf67408d29c175b04b7
