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

class HandleHiddenElement():
    def hidden_element(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options= chrome_options)

        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

        # driver.find_element(By.TAG_NAME, "button").click()


        display_element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()

        print(display_element)

        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        display_element1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(display_element1)

        time.sleep(10)

    def hidden_element_yatra(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options= chrome_options)

        driver.get("https://demo.bagisto.com/bagisto-common/search?new=1")
        driver.find_element(By.XPATH,"//div[@class='relative z-//div[@class='absolute z-20 w-max overflow-hidden rounded-").click()
        time.sleep(5)

        # driver.find_element(By.XPATH,"//div[@class='relative z-//div[@class='absolute z-20 w-max overflow-hidden rounded-")
        ele = driver.find_element(By.XPATH, "//div[@class='relative z-//div[@class='absolute z-20 w-max overflow-hidden rounded-").is_displayed()

        print(ele)

        time.sleep(5)
hiddenelement = HandleHiddenElement()
hiddenelement.hidden_element_yatra()