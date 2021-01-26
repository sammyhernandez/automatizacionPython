import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

class usan_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")

    def test_pagina_siguiente_o_anterior(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://gmail.com")
        time.sleep(3)
        driver.get("https://Google.com")
        time.sleep(3)
        driver.get("https://Youtube.com")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()

    def tearDown(self):
        driver = self.driver
        driver.close()
        

if __name__ == '__main__':
    unittest.main()
