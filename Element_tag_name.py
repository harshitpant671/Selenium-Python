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

class DemoElementTagName():
    def element_tag_name(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options= chrome_options)

        driver.get("https://secure.yatra.com/social/common/yatra/signin.html")

        #driver.find_element(By.TAG_NAME, "button").click()
        driver.find_element(By.CLASS_NAME, "yt-sme-mobile-input").send_keys("harshit@example.com")

        time.sleep(10)

findtagname = DemoElementTagName()
findtagname.element_tag_name()

