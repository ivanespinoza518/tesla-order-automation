from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    VEHICLES_TAB = (By.XPATH, "//span[text()='Vehicles']")
    ORDER_MODEL3_BUTTON = (
        By.XPATH,
        "//a[@href='/model3/design' and @aria-label='Order']",
    )

    def hover_over_vehicles(self):
        vehicles_element = self.driver.find_element(*self.VEHICLES_TAB)
        self.hover(vehicles_element)

    def click_order_model3(self):
        order_button = self.driver.find_element(*self.ORDER_MODEL3_BUTTON)
        self.click(order_button)
