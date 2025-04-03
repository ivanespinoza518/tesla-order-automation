from tests.model3_order_test import Model3OrderTest

if __name__ == "__main__":
    DRIVER_PATH = r"C:\\WebDriver\\chromedriver.exe"  # Path to chromedriver
    test = Model3OrderTest(DRIVER_PATH)
    test.run_test()
