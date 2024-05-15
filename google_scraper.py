from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
from selenium.common.exceptions import NoSuchElementException

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com/")

# Find the search box and enter the keyword
search_box = driver.find_element(By.NAME, "q")
keyword = "buy linjer"
search_box.send_keys(keyword)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(8)  # Adjust the time as needed

# Capture screenshot of the Sponsored list
driver.find_element(By.CLASS_NAME, "pla-exp-container").screenshot("google-search-result-sponsored.png")

# Get the information of all products under "Sponsored" list
sponsored_products = driver.find_elements(By.CLASS_NAME, "pla-unit")
for product in sponsored_products:
    try:
        product_title = product.find_element(By.CLASS_NAME, "pla-unit-title-link").text
    except NoSuchElementException:
        product_title = "product_title is empty"
    print("Title:", product_title)

    try:
        product_url = product.find_element(By.CLASS_NAME, "pla-unit-title-link").get_attribute("href")
    except NoSuchElementException:
        product_url = "product_url is empty"
    print("URL:", product_url)

    try:
        product_price = product.find_element(By.CLASS_NAME, "e10twf").text
    except NoSuchElementException:
        product_price = "product_price is empty"
    print("Price:", product_price)

    try:
        product_rating_star = product.find_element(By.XPATH, "//span[@role = 'img']").get_attribute("aria-label").replace(',', '')
    except NoSuchElementException:
        product_rating_star = "product_rating_star is empty"
    print("Rating Star:", product_rating_star)

    try:
        product_rating_num_count = product.find_element(By.XPATH, "//span[@class = 'fl pbAs0b']").text
    except NoSuchElementException:
        product_rating_num_count = "product_rating_num_count is empty" 
    print("Rating Num Count:", re.sub('[()]', '', product_rating_num_count))

    print("")

# Close the browser
driver.quit()
