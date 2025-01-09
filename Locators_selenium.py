import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#locators: ID , name
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#locators: Xpath ,cssselector , classname
#css slector = tagname[attribute='value'] , #id ,.classname
#xpath = //tagname[@attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Sam")
#Radio button
driver.find_element(By.CSS_SELECTOR,"input[value='option2']").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Sam")
time.sleep(3)
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert 'Success' in message

time.sleep(4)

