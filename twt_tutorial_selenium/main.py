from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:/Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)

time.sleep(5)

driver.quit()