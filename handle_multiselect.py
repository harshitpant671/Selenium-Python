import time
import os
from time import sleep

import self

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from demo import chrome_options

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''


# Single select dropdown
class HandleDropDown():
    def handle_dropdown(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.get(
            "https://login.alibaba.com/reg/union_reg.htm?_regfrom=ICBU_UNION_REG&_regbizsource=main_page&return_url=https%3A%2F%2Fwww.alibaba.com%2F")

        dropdown = driver.find_element(By.NAME, "range")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(5)
        dd.select_by_visible_text("This Year")
        time.sleep(5)
        dd.select_by_value("year")
        time.sleep(5)
#Unselect the value using this
        dd.deselect_by_value("year")

handledropdown = HandleDropDown()
handledropdown.handle_dropdown()
