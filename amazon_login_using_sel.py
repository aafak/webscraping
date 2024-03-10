#import undetected_chromedriver as uc
# https://letsusetech.com/how-to-scrape-amazon-product-reviews-behind-a-login
# Need tp change the email and password fields
from selenium import webdriver

import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = False

#river = uc.Chrome(use_subprocess=True, options=chromeOptions)
driver = webdriver.Chrome(options=chromeOptions, service=Service(ChromeDriverManager().install()))


# Replace the Amazon link below with your login URL
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=xxxxxxxxxxxx")

time.sleep(5) # Wait for a few seconds to ensure the page loads completely

email = driver.find_element(By.ID, "ap_email")

# Replace the xxx with your Amazon email
email.send_keys("xxxxxxxxx")

driver.find_element(By.ID, "continue").click()

time.sleep(5)

password = driver.find_element(By.ID, "ap_password")


# Replace the xxx with your Amazon password
password.send_keys("xxxxxxxx")

driver.find_element(By.ID, "signInSubmit").click()

time.sleep(10)

# Navigate to the Amazon product page
product_url = "https://www.amazon.com/ENHANCE-Headphone-Customizable-Lighting-Flexible/dp/B07DR59JLP/"

driver.get(product_url)

time.sleep(10) # Wait for a few seconds to ensure the page loads completely

# Locate and extract review elements
review_elements = driver.find_elements(By.CSS_SELECTOR, '.a-section.review')

csv_filename = 'product_reviews.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Author', 'Review', 'Review Date'])

    for review_element in review_elements:

        # Extract the author's name
        author_name = review_element.find_element(By.CLASS_NAME, 'a-profile-name').text

        # Extract review text
        review_text = review_element.find_element(By.CLASS_NAME, 'review-text').text

        # Extract review date
        review_date = review_element.find_element(By.CLASS_NAME, 'review-date').text

        # Print the extracted information
        print("Author: ", author_name)
        print("Review: ", review_text)
        print("Review Date: ", review_date)
        print("\n")

        csv_writer.writerow([author_name, review_text, review_date])

driver.close()
