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

class HandleCheckbox():
    def handle_checkbox(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options= chrome_options)

        driver.get("https://demo.bagisto.com/bagisto-common/customer/login")
        time.sleep(3)
        # driver.find_element(By.TAG_NAME, "button").click()
        driver.find_element(By.XPATH, "//label[@class='icon-uncheck peer-checked:icon-check-box cursor-pointer text-2xl text-navyBlue peer-checked:text-navyBlue max-sm:text-xl']").click()
        # TO CHECK THE CHECKBOX IS SELECTED OR NOT
        time.sleep(2)
        check_select= driver.find_element(By.XPATH,"//label[@class='icon-uncheck peer-checked:icon-check-box cursor-pointer text-2xl text-navyBlue peer-checked:text-navyBlue max-sm:text-xl']").is_selected()
        print(check_select)
        time.sleep(5)

        driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
        time.sleep(3)


handlecheckbox = HandleCheckbox()
handlecheckbox.handle_checkbox()