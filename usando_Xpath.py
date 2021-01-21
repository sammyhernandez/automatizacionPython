import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")
        self.driver.maximize_window()

    def test_buscar_por_xpath(self):
        print("Caso - 001: Buscando palabras en Google")
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("Selenium", Keys.ARROW_DOWN)
        time.sleep(6)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
