import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element(By.CLASS_NAME, "Button-sc-1dr2sn8-0").click()
# driver.find_element(By.ID, "multiform").send_keys("samridhipradhan@gmail.com")
# driver.find_element(By.XPATH, "//button[@type = 'submit']").click()


web_element = driver.find_element(By.XPATH,"(//input[@placeholder='Search for Products...'])[2]")
web_element.click()
web_element.send_keys("Potato")
time.sleep(2)


