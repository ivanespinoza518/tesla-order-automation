from page_objects.home_page import HomePage
from page_objects.model3_order_page import Model3OrderPage
from tests.base_test import BaseTest
import time


class Model3OrderTest(BaseTest):
    """ Initialize WebDriver, HomePage, and OrderPage """
    def __init__(self, driver_path):
        super().__init__(driver_path)
        self.home_page = HomePage(self.driver)
        self.order_page = Model3OrderPage(self.driver)

    def run_test(self):
        try:
            self.setup("https://www.tesla.com")

            time.sleep(5)

            self.home_page.hover_over_vehicles()
            print("Hovered over 'Vehicles'")
            time.sleep(3)

            self.home_page.click_order_model3()
            print("Clicked 'Order' for Model 3")
            time.sleep(5)

            self.order_page.select_cash_tab()
            print("Selected 'Cash' tab")
            time.sleep(5)

            expected_prices = ["$29,990", "$34,990", "$42,490"]
            actual_prices = self.order_page.get_trim_prices()

            for idx, (actual, expected) in enumerate(zip(actual_prices, expected_prices), start=1):
                if actual == expected:
                    print(f"Trim {idx}: Price correct: {actual}")
                else:
                    print(f"Trim {idx}: Price incorrect. Found: {actual}, Expected: {expected}")
        finally:
            self.teardown()
