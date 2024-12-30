import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "Button-sc-1dr2sn8-0").click()
time.sleep(2)
