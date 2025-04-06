import time
import os
from time import sleep

import self

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from demo import chrome_options

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

class HandleRadio():
    def handle_radio(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options= chrome_options)

        driver.get("https://demo.bagisto.com/bagisto-common/adventure-seeker-boys-half-sleeve-graphic-t-shirt")
        time.sleep(5)
        # driver.find_element(By.TAG_NAME, "button").click()
        print(driver.find_element(By.XPATH, "//label[@title='5-7 Y']").is_selected())

        driver.find_element(By.XPATH, "//label[@title='5-7 Y']").click()
        # time.sleep(5)
        print(driver.find_element(By.XPATH, "//label[@title='5-7 Y']").is_selected())

        time.sleep(5)

handleradio = HandleRadio()
handleradio.handle_radio()