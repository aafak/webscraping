from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


AMAZON_BASE_URL = "https://www.amazon.in/"


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

cookie = "session-id=261-8411119-7687861; session-id-time=2082787201l; i18n-prefs=INR; ubid-acbin=262-8727450-4461710; lc-acbin=en_IN; session-token=MFBKNDEi08pX5ftbnb9foFr8nyuArM6ICgVxmLTDKhMKtUiQ5BuRxUPq1+zm4gseBApVWH/77AL/O3oLqwPJJu7cjG0SZnOYMW2cs4F8jPYPn1PPFvtTy0zssHWiDqQoxpiow4GbCWXkvXMJGEYmcZaQ5eU8z6NaMuJ3DaV6KGxcEnmOFRWIYs/ws8c1+YRm+hqbx5ymgJtwa3DjTvcifgjQ07ynKBXZ3ZDPx0lfPyFRiLQv6X17ZTaDgrm7Rsi8uPT2eLf1DZBglMQLfddUkxPl1PkPasH2d4zIFS7YCx17QMGi2h2hYta3OqhA7xVntDXenp13dQv3Sg6j+qwKnIUWkdz7Snvs; csm-hit=tb:N6S3R8EK5WP8CDMV2G12+sa-8K7ZDNGRQV062QC6JSJK-TMQQP83EXKCY3VZABFXQ|1710571377161&t:1710571377161&adb:adblk_no"
HEADERS = ({'User-Agent': USER_AGENT,
            'Accept-Language': 'en-US, en;q=0.5',
            'Cookie': cookie,
            'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"'

            })
# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):
    try:
        #price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()
        price = soup.find("span", attrs={'class': 'a-price-whole'})
        #print(f"price: {price}")
        price = price.text.strip()
        #price = price.find("span").string.strip()
        print(price)


    except AttributeError as e:
        print(e)
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):
    try:
        #rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star-medium a-star-medium-4 averageStarRating'}).text.strip()

        print(f"rating: {rating}")
    except AttributeError as e:
        try:
            print(f"error: {e}")
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating


# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count


# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available


def getAmazonSearch(search_query):
    url=AMAZON_BASE_URL + "s?k=" + search_query
    print(url)
    page=requests.get(url,headers=HEADERS)
    if page.status_code==200:
        return page
    else:
        return "Error"

def getNextPageSearch(search_query):
    url=AMAZON_BASE_URL + search_query
    print(url)
    page=requests.get(url,headers=HEADERS)
    if page.status_code==200:
        return page
    else:
        return "Error"


def Searchasin(asin):
    url=AMAZON_BASE_URL + "dp/" + asin
    print(url)
    page=requests.get(url,headers=HEADERS)
    if page.status_code==200:
        return page
    else:
        return "Error"

def Searchreviews(review_link):
    url=AMAZON_BASE_URL + review_link
    print(url)
    page=requests.get(url,headers=HEADERS)
    if page.status_code==200:
        return page
    else:
        return "Error"

import  time
if __name__ == '__main__':
    #search_query = "samsung+mobile+phones"
    search_query = "iphone+mobile+phones"

    data_asin = set()
    total_page_count = None
    page_count = 1
    next_page_query = None
    disabled_next_button = None
    # while disabled_next_button is None:
    #     page_query = next_page_query if next_page_query else search_query
    #     response = getAmazonSearch(page_query)
    #     print(response)
    #     soup = BeautifulSoup(response.content, "html.parser")
    #
    #     for i in soup.findAll("div", {
    #         'data-component-type': "s-search-result"}):
    #         if i.get("data-asin"):
    #             data_asin.add(i['data-asin'])
    #     page_count += 1
    #     next_page_query = search_query + "&page=" + str(page_count)
    #     time.sleep(2)
    #     if total_page_count is None:
    #         total_items = soup.find("span", {"class": 's-pagination-item s-pagination-disabled'})
    #         print(total_items.string.strip())
    #         total_page_count = int(total_items.string.strip())
    #     disabled_next_button = soup.find("span", {"class": "s-pagination-item s-pagination-next s-pagination-disabled"})
    #     print(f"disabled_next_button: {disabled_next_button}")
    #     print(data_asin)
    #     if total_page_count and page_count > total_page_count:
    #         break
    #
    # print(data_asin)

    #data_asin.add("B0C9QS5G2R")   #  10,110
    #data_asin.add('B0CMCM52MB')  # 13 user review
    data_asin.add("B0CQYMMP94")  # 221
    link = []
    count = 0
    for pd in data_asin:
        pd_user_reviews = list()
        response = Searchasin(pd)
        soup = BeautifulSoup(response.content, "html.parser")
        review_link = soup.find("a", {'data-hook': "see-all-reviews-link-foot"})
        review_link_url = review_link.get("href")
        print(f"review_link_url: {review_link_url}")

        review_count_info = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
        review_count = int(review_count_info.split(" ")[0])
        print(f"review_count: {review_count}")

        review_disable_button = None
        review_page_count = 1
        while review_disable_button is None:
            response = Searchreviews(review_link_url + '&pageNumber=' + str(review_page_count))
            soup = BeautifulSoup(response.content, "html.parser")
            page_reviews = []
            user_reviews = soup.find_all("span", {'data-hook': "review-body"})
            for i in user_reviews:
                page_reviews.append(i.text)
            print(f"Reviews# {len(page_reviews)}")
            print(f"Reviews: {page_reviews}")
            pd_user_reviews.extend(page_reviews)

            review_disable_button = soup.find("li", {"class": "a-disabled a-last"})
            print(f"review_disable_button: {review_disable_button}")
            #  <li class="a-disabled a-last">Next page<span class="a-letter-space"></span><span class="a-letter-space"></span><span class="larr">→</span></li>
            if review_disable_button or len(page_reviews) == 0 or len(pd_user_reviews) > review_count :
                break
            review_page_count += 1
            time.sleep(2)
        print(f"pd_user_reviews# {len(pd_user_reviews)}")