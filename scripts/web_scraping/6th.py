from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Set up driver
service = Service("chromedriver")  # Replace with your path if needed
driver = webdriver.Chrome(service=service)

# Open website
driver.get("https://quotes.toscrape.com/js/")  # JS-based quotes page

time.sleep(2)  # wait for page to load

# Extract quotes dynamically loaded
quotes = driver.find_elements(By.CLASS_NAME, "text")
for q in quotes:
    print(q.text)

driver.quit()
