from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Path to your chromedriver
driver_path = r"C:\WebDriver\chromedriver.exe"

# Initialize the Service object
service = Service(driver_path)

# Initialize the WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Open Tesla website
driver.get("https://www.tesla.com")
driver.maximize_window()  # Navbar will not populate otherwise
print("Opened tesla.com")

# Locate the "Vehicles" element
vehicles_element = driver.find_element(By.XPATH, "//span[text()='Vehicles']")

# Initialize ActionChains
actions = ActionChains(driver)

# Hover over the "Vehicles" element
actions.move_to_element(vehicles_element).perform()
print("Hovered over 'Vehicles'")

# Wait for a few seconds to observe the hover effect
time.sleep(3)

# Locate the 'Order' button for the Model 3 (using href attribute) and click
order_button = driver.find_element(By.XPATH, "//a[@href='/model3/design' and @aria-label='Order']")
order_button.click()
print("Clicked 'Order' for Model 3")

# Wait for a few seconds to see the result and to wait for page to load
time.sleep(5)

# Locate and click the "Cash" tab using the ID or other attributes
cash_tab = driver.find_element(By.XPATH, "//button[@id='cash']")
cash_tab.click()
print("Clicked 'Cash' tab")

# Wait for a few seconds to observe the action and wait for trims to load
time.sleep(5)

# Expected prices for each trim
expected_prices = [
    "$29,990",  # Expected price for rear-wheel drive
    "$34,990",  # Expected price for all-wheel drive
    "$42,490"   # Expected price for performance all-wheel drive
]

# Locate the price elements
trim_prices = [
    driver.find_element(By.CSS_SELECTOR, 'p[data-id="$MT356-price"] span'),  # Listed price for rear-wheel
    driver.find_element(By.CSS_SELECTOR, 'p[data-id="$MT357-price"] span'),  # Listed price for all-wheel
    driver.find_element(By.CSS_SELECTOR, 'p[data-id="$MT360-price"] span')   # Listed price for performance all-wheel
]

# Iterate through the list of trim prices and verify each one
for idx, price_element in enumerate(trim_prices):
    price_text = price_element.text.strip()  # Get the price text and remove any extra spaces

    # Check if the price matches the expected price
    expected_price = list(expected_prices)[idx]  # Get the corresponding expected price for the trim

    if price_text == expected_price:
        print(f"Trim {idx + 1}: Price is correct: {price_text}")
    else:
        print(f"Trim {idx + 1}: Price is incorrect, found: {price_text}, expected: {expected_price}")

# Close the browser
driver.quit()