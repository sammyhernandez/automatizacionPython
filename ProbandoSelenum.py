from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\ChromeDriver\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.close();
