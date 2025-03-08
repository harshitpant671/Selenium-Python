from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
import os



os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''


# Setup Chrome options (Optional, for headless browser usage)
chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=0.7")
#chrome_options.add_argument("--headless") # Uncomment if you want to run headless

# Create the WebDriver object using the latest ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
# Open the URL in the browser
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
driver.switch_to.frame('iframeResult')

"""
Type1: Confirm
For the Alert
"""
#to Accept the Alert Message
driver.find_element(By.XPATH,'//button[contains(.,"Try it")]').click()
driver.switch_to.alert.accept()
# To Dismiss the Alert
driver.find_element(By.XPATH,'//button[contains(.,"Try it")]').click()
driver.switch_to.alert.dismiss()

"""
Type2: Prompt 
For Send the Text in Alert
"""
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.switch_to.frame('iframeResult')

driver.find_element(By.XPATH,'//button[contains(.,"Try it")]').click()
print(driver.switch_to.alert.text)
time.sleep(2)

driver.switch_to.alert.send_keys('Harshit Pant')
driver.switch_to.alert.accept()


# from create_product_page import message

time.sleep(3)