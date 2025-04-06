from operator import index

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
driver.get("https://www.snapdeal.com/products/mens-footwear-sports-shoes?sort=plrty")


left_elem =  driver.find_element(By.CLASS_NAME, 'a.price-slider-scroll.left-handle' )
right_elem = driver.find_element(By.CLASS_NAME, 'a.price-slider-scroll.right-handle')

# ActionChains(driver).drag_and_drop_by_offset(left_elem,200,0).perform()
# ActionChains(driver).click_and_hold(left_elem).pause(1).move_by_offset(50,0).release().perform()
ActionChains(driver).move_to_element(left_elem).pause(1).click_and_hold().move_by_offset(80,0).release().perform()
time.sleep(5)


