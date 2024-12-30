from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME, "img")
count = 0
for image in images:
    count += 1
print(count)
