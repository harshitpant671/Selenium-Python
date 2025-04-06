import os
import time

from tkinter.font import names

import self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''


class demoFindCssSelector():
    def locate_by_CssSelector(self):
        # Set up ChromeOptions without proxy settings
        chrome_options = webdriver.ChromeOptions()

        # Initialize WebDriver without proxy settings
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.get("https://demo.bagisto.com/bagisto-103-184-236-227/admin/dashboard")
        #driver.maximize_window()

        driver.implicitly_wait(5)

        driver.find_element(By.CSS_SELECTOR, "button[aria-label='Sign In']").click()

        time.sleep(5)

findbycssselector = demoFindCssSelector()
findbycssselector.locate_by_CssSelector()

