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
driver.get("https://demo.bagisto.com/bagisto-common/admin/login")

time.sleep(2)

# Scroll method


# Fetch the current URL of the page

# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@example.com')
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys('admin123')
driver.find_element(By.XPATH, "//button[@aria-label='Sign In']").click()
# time.sleep(5)

driver.get("https://demo.bagisto.com/bagisto-common/admin/catalog/products")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='primary-button']").click()
time.sleep(5)

driver.find_element(By.XPATH, "//select[@name='type']").click()
time.sleep(3)
drop_down= Select(driver.find_element(By.XPATH, "//select[@name='type']"))
drop_down.select_by_index(0)
time.sleep(2)

driver.find_element(By.XPATH, "//select[@name='attribute_family_id']").click()
drop_down1 = Select(driver.find_element(By.XPATH, "//select[@name='attribute_family_id']"))
drop_down1.select_by_index(0)
# time.sleep(2)

sku_data = driver.find_element(By.XPATH, "//input[@name='sku']")
sku_data.send_keys("108")
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(5)

message = driver.find_element(By.XPATH, "//p[@class='mt-1 text-xs italic text-red-600']")

if message.is_displayed() and "The sku has already been taken" in message.text:
    sku_data.clear()  # Clear the current value if you want to input a new SKU
    time.sleep(2)
    sku_data.send_keys("sku218")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='product_number']").send_keys("554545")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Simple Product 203")
time.sleep(2)

# driver.find_element(By.XPATH,"//input[@id='url_key']").send_keys("sku-310")
#
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
for i in range(0,2):
    driver.find_elements(By.XPATH, "//button[@aria-label='Source code']")[i].click()
    # short_description.send_keys("Simple Product 111")
    time.sleep(2)
    driver.find_element(By.XPATH,"//textarea[@type='text']").send_keys("Simple Product 209")
    time.sleep(2)

    driver.find_element(By.XPATH,"//button[@title='Save']").click()
time.sleep(2)

driver.find_element(By.XPATH,'//textarea[@name="meta_title"]').send_keys("ASX")
driver.find_element(By.XPATH,'//textarea[@name="meta_keywords"]').send_keys("ASX")
driver.find_element(By.XPATH,'//textarea[@name="meta_description"]').send_keys("ASX")

time.sleep(2)
driver.execute_script("window.scrollBy(0,-600);")

time.sleep(2)

driver.find_element(By.XPATH,'//input[@name="price"]').send_keys("100")
time.sleep(2)

driver.execute_script("window.scrollBy(0,600);")

driver.find_element(By.XPATH,'//input[@id="weight"]').send_keys("0.32")
time.sleep(2)


# # driver.find_element(By.XPATH,"//iframe[@id='description_ifr']").send_keys("Simple Product")

# driver.find_element(By.XPATH,"//input[@name='price']").send_keys("1")
driver.execute_script("window.scrollBy(0,500);")

# driver.find_element(By.XPATH,"//input[@name='weight']").send_keys("1")
#
driver.find_element(By.XPATH,"//label[@for='visible_individually']").click()

driver.find_element(By.XPATH,"//label[@for='status']").click()

driver.find_element(By.XPATH,"//label[@for='guest_checkout']").click()
time.sleep(2)

driver.find_element(By.XPATH,'//input[@name="inventories[1]"]').send_keys('5')
time.sleep(2)

driver.execute_script("window.scrollBy(0,-800);")

driver.find_element(By.XPATH,'//button[@class="primary-button"]').click()
time.sleep(5)
