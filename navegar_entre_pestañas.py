import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.Google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.Amazon.com")
        time.sleep(6)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()
