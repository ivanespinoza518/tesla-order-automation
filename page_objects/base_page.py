from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def hover(self, element):
        """ Hover over a web element. """
        self.actions.move_to_element(element).perform()

    def click(self, element):
        """ Click on a web element. """
        element.click()

    def get_text(self, element):
        """ Retrieve text from a web element. """
        return element.text.strip()
