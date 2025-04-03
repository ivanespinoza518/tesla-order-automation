# Tesla Order Automation

This project automates the process of navigating the Tesla website to verify trim prices for the Model 3 using Selenium WebDriver with Python. The automation follows the Page Object Model design pattern for improved maintainability and scalability.

## Features

- Automates the process of navigating the Tesla website to select the Model 3.
- Hovers over the "Vehicles" tab.
- Clicks the "Order" button for the Model 3.
- Selects the "Cash" payment option.
- Verifies the listed trim prices for the Model 3.
- Implements Page Object Model (POM) design pattern for code maintainability.
- Uses Python, Selenium WebDriver, and ChromeDriver for browser automation.

## Requirements

To run this project, you'll need the following:

- Python 3.10 or higher
- Selenium WebDriver
- ChromeDriver (matching your Chrome version)
- Virtual Environment (optional but recommended)

## Setup

### 1. Clone the Repository
First, clone the repository to your local machine:

    git clone https://github.com/your-username/tesla-order-automation.git

### 2. Install Selenium
Navigate to the project directory and install selenium to your project:

    cd tesla-order-automation
    pip install selenium

### 3. Install ChromeDriver
Download and install the version of ChromeDriver that matches your installed Chrome version. Add the path to chromedriver to your system's PATH, or specify it directly in the script.

## Project Structure
The project follows the Page Object Model design pattern to organize the code into separate page objects for each page of the application.

    tesla-order-automation/
    ├── page_objects/
    │   ├── base_page.py           # Contains base methods like click, hover, etc.
    │   ├── home_page.py           # Page object for the home page
    │   └── model3_order_page.py   # Page object for the order page
    ├── tests/
    │   ├── base_test.py           # Base test class with setup/teardown methods
    │   └── model3_order_test.py   # Main test that runs the automation
    ├── main.py                    # Entry point to execute the automation
    └── README.md                  # This file

## Usage
1. Ensure that the necessary dependencies are installed.

2. Set up the ChromeDriver and ensure it's accessible via the system PATH.

3. Run the test:

    ```bash
    python main.py

- The script will:

  - Open the Tesla website.
  
  - Hover over the "Vehicles" tab.
  
  - Click on the "Order" button for the Model 3.
  
  - Select the "Cash" payment option.
  
  - Verify the trim prices for the Model 3 and print the results to the console.

