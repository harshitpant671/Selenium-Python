import time
import os
from time import sleep

import self

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from demo import chrome_options

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''


# Single select dropdown
class HandleAutoSuggest():
    def handle_autosuggest(self):
        chrome_options = webdriver.ChromeOptions()

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://demo.bagisto.com/search-suggestion-common/")

        time.sleep(3)
        test = driver.find_element(By.XPATH, "//input[@class='block w-full px-11 py-3 bg-[#F5F5F5] rounded-lg text-gray-900 text-xs font-medium transition-all border border-transparent hover:border-gray-400 focus:border-gray-400']")
        test.click()
        time.sleep(5)

        test.send_keys("arct")
        time.sleep(5)

        # test2 = (driver.find_element(By.XPATH, "// div // span // a[ @ href = 'arctic-cozy-knit-unisex-beanie']"))
        # test2.click()

       # some issue in xpath
        search_result = driver.find_element(By.XPATH, "//div[@class='absolute max-h-96 border rounded z-10 overflow-y-auto w-'")

        print(len(search_result))
        for result in search_result:
            print(result.text)
            if "arctic-cozy-knit-unisex-beanie" in result.text:
                result.click()
                time.sleep(5)
                break
        time.sleep(5)


        test.send_keys(Keys.ENTER)

        time.sleep(3)

handlesuggest = HandleAutoSuggest()
handlesuggest.handle_autosuggest()
