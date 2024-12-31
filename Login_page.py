import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.bigbasket.com/")
driver.maximize_window()
# driver.implicitly_wait(5)

# driver.find_element(By.CLASS_NAME, "Button-sc-1dr2sn8-0").click()
# driver.find_element(By.ID, "multiform").send_keys("samridhipradhan@gmail.com")
# driver.find_element(By.XPATH, "//button[@type = 'submit']").click()


# web_element = driver.find_element(By.XPATH,"(//input[@placeholder='Search for Products...'])[2]")
# web_element.click()
# web_element.send_keys("Potato")

wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.XPATH,"(//input[@placeholder='Search for Products...'])[2]"))).send_keys("potato")

wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "View all search results"))).click()
# driver.find_element(By.LINK_TEXT, "View all search results").click()
time.sleep(3)
