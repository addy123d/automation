# https://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://app.revechat.com/")

driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/input').send_keys('adityachaudhary@ineuron.ai')
time.sleep(3)
  
# find the element where we have to 
# enter the xpath
# fill the password
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('test@123')
time.sleep(3)
  
# find the element log in 
# request using xpath 
# clicking on that element 
driver.find_element(By.XPATH, '//*[@id="intro-singup"]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="top_header_profile_image"]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="top_bar_profile_option"]/li[6]/a').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="engaged_tab"]/a').click()
time.sleep(8)


driver.find_element(By.XPATH, '//*[@id="top_header_profile_image"]').click()
time.sleep(5)


driver.find_element(By.XPATH, '//*[@id="top_bar_profile_option"]/li[12]/a').click()
time.sleep(2)

# //*[@id="delete"]
driver.find_element(By.XPATH, '//*[@id="delete"]').click()
