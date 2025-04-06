from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.maximize_window()

'''
Right click
'''
achain = ActionChains(driver)
elm1 = driver.find_element(By.xpath,'xpath')
achain.context_click(elm1).perform()
time.sleep(2)

'''
Double click
'''
achain = ActionChains(driver)
elm2 = driver.find_element(By.xpath,'xpath')
achain.double_click(elm1).perform()
time.sleep(2)
