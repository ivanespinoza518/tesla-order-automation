from selenium.webdriver.common.by import By
from .base_page import BasePage


class Model3OrderPage(BasePage):
    CASH_TAB = (By.XPATH, "//button[@id='cash']")
    TRIM_PRICE_IDS = ["$MT356-price", "$MT357-price", "$MT360-price"]

    def select_cash_tab(self):
        cash_tab = self.driver.find_element(*self.CASH_TAB)
        self.click(cash_tab)

    def get_trim_prices(self):
        prices = []
        for trim_id in self.TRIM_PRICE_IDS:
            price_element = self.driver.find_element(By.CSS_SELECTOR, f'p[data-id="{trim_id}"] span')
            prices.append(self.get_text(price_element))
        return prices
