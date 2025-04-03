from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseTest:
    """ Initializes the WebDriver using Service object. """
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)

    """ Opens the specified website and maximizes the window. """
    def setup(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Opened {url}")

    """ Test cleanup. """
    def teardown(self):
        self.driver.quit()
        print("Browser closed.")
