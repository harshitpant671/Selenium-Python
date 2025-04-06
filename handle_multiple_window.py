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
driver.get("https://www.yatra.com/react-home/flights")
parent_handle = driver.current_window_handle
print(parent_handle)

driver.find_element(By.XPATH, '//div[contains(text(), "View all offers")]').click()
all_handles = driver.window_handles
print(all_handles)

for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        # another new window link
        driver.find_element(By.XPATH, '//img[@src="//www.yatra.com/ythomepagecms/media/todayspick_home/2025/Jan/06d4f2151f688c39c37c6f7a2ba2e99a.jpg"]').click()
        time.sleep(4)
        driver.close()
        time.sleep(2)
        break

driver.switch_to.window(parent_handle)
driver.find_element(By.XPATH, '//div[contains(text(), "View all offers")]')
driver.close()
time.sleep(2)



time.sleep(2)
