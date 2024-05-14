from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

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
time.sleep(5)  # Adjust the time as needed

# Capture screenshot of the newsfeed
driver.find_element(By.CLASS_NAME, "pla-exp-container").screenshot("google-search-result-sponsored.png")

# Get the information of all products under "Sponsored" list
sponsored_products = driver.find_elements(By.CLASS_NAME, "pla-unit")
for product in sponsored_products:
    product_title = product.find_element(By.CLASS_NAME, "pla-unit-title-link").text
    product_url = product.find_element(By.CLASS_NAME, "pla-unit-title-link").get_attribute("href")
    product_price = product.find_element(By.CLASS_NAME, "e10twf").text
    product_rating_star = product.find_element(By.CLASS_NAME, "z3HNkc").get_attribute("aria-label")
    product_rating_num_count = product.find_element(By.CLASS_NAME, "pbAs0b").text
    if(product_title):
        print("Title:", product_title)
    if(product_url):
        print("URL:", product_url)
    if(product_price):
        print("Price:", product_price)
    if(product_rating_star):
        print("Rating Start:", product_rating_star)
    if(product_rating_num_count):
        print("Rating Num Count:", product_rating_num_count)
    print("")

# Close the browser
driver.quit()
