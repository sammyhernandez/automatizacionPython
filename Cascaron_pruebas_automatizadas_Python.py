import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Cascaron (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_lo_que_sea(self):
        print("Caso -000")
        driver = self.driver
        driver.get("https://wwww.Google.com")

    
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
        unittest.main()