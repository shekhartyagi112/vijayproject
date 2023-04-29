from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com/")
firstname = "Test"
lastname = "name"
mobile = "9839980052"
driver.implicitly_wait(10)
driver.find_element(By.PARTIAL_LINK_TEXT,"Create new accou").click()
firstName = driver.find_element(By.NAME,"firstname")
firstName.send_keys(firstname)
lastName = driver.find_element(By.NAME,"lastname")
lastName.send_keys(lastname)
x = driver.find_element(By.NAME,"reg_email__")
x.send_keys(mobile)
driver.find_element(By.ID,"password_step_input").send_keys('Bharti@12345')
driver.find_element(By.XPATH,"//option[@value='28']").click()
driver.find_element(By.XPATH,"//option[normalize-space()='Jan']").click()
driver.find_element(By.XPATH,"//option[@value='1998']").click()
driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
driver.find_element(By.NAME,"websubmit").click()
time.sleep(20)
driver.close()

