from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")
driver.get("https://gmail.com")
driver.maximize_window()


usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("sammy181090@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

contrasenia = driver.find_element_by_name("password")
contrasenia.send_keys("00000000")
contrasenia.send_keys(Keys.ENTER)
time.sleep(3)

driver.close()