from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# import from webdriver_manager (using underscore)
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# create a driver object using driver_path as a parameter
driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))

# chrome_options = webdriver.ChromeOptions()                      # Create object ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
#driver= webdriver.Chrome('chromedriver',options=chrome_options) # Create driver


if __name__ == '__main__':
  #
  user_review_link = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=1"
  driver.get(user_review_link)

  # This review link not working
  # user_review_link2 = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=2"
  # driver.get(user_review_link2)

  #  review = driver.find_element(By.XPATH, ".//span[@data-hook = 'review-body']")  # working
  # print(review.text)

  #reviews = driver.find_elements(By.XPATH, ".//span[@data-hook = 'review-body']")  # sometimes does not load run twice works
  # print(reviews)  # working

  reviews = wait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, ".//span[@data-hook = 'review-body']")))

  print(reviews)
  # print(type(reviews))
  # print(dir(reviews))
  for r in reviews:
    print(r.text)
