import os
from tkinter.font import names

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Unset environment variables for proxy
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# Set up ChromeOptions without proxy settings
chrome_options = webdriver.ChromeOptions()

# Initialize WebDriver without proxy settings
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)



def verify_title():
    # Open a website
    driver.get("https://www.essenzi.com")

    # Print the title of the page
    print(driver.title)

    title = driver.title

    expected_title = "Buy Best Branded Perfumes Online in Dubai UAE - Essenzi"

    if title == expected_title:
        print("verified successfully")
    else:
        print("Not verified")

    driver.quit()

if __name__ == '__main__':
    verify_title()




