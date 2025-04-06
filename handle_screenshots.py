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
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
time.sleep(2)

cur_button= driver.find_element(By.XPATH,'//button[@id="login-continue-btn"]')

# . means current directory
cur_button.screenshot(".//test1.png")
time.sleep(2)

cur_button.click()
time.sleep(1)
driver.get_screenshot_as_file("C:\\automation-selenium\\error.png")
time.sleep(2)