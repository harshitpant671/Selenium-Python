import os
import time

from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# Set up ChromeOptions without proxy settings
chrome_options = webdriver.ChromeOptions()

# Initialize WebDriver without proxy settings
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.essenzi.com/customer/login")
#driver.maximize_window()


driver.find_element(By.NAME, 'email').send_keys('harshit@example.com')

time.sleep(5)
#print(driver.current_url)
#print(driver.title)




