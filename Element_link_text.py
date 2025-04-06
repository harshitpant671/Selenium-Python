import os
import time
from time import sleep

import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

class demoFindElementByLinkText():
    def find_link_text(self):

        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options = chrome_options)

        driver.get("https://www.yatra.com/")
        #driver.find_element(By.LINK_TEXT, "For Business").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "For").click()

        time.sleep(10)

findtextlink = demoFindElementByLinkText()
findtextlink.find_link_text()