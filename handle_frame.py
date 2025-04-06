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

# Switch to the Locator parent iframe
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@id="short_description_ifr"]'))
# Switch to the indexing.
driver.switch_to.frame(0)

# Here we can add another child iframe
driver.find_element(By.XPATH,'//body[@data-id="short_description"]').click()


time.sleep(2)