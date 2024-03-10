from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


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
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:
        try:
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

def get_user_reviews(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available

if __name__ == '__main__':

    # add your user agent
    # https://www.whatismybrowser.com/
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    #URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    #URL = "https://www.amazon.com/s?k=samsung+phone&crid=30WBEUTLVCP73&sprefix=samsu%2Caps%2C338&ref=nb_sb_ss_ts-doa-p_2_5"
    URL = "https://www.amazon.in/s?k=samsung+mobile&crid=142CNLJ4QPRV5&sprefix=Sam%2Caps%2C232&ref=nb_sb_ss_ts-doa-p_2_3"

    # HTTP Request
    print(f"Fetching data from URL: {URL}")
    response = requests.get(URL, headers=HEADERS)
    print(f"response: {response}")

    # Soup Object containing all data
    soup = BeautifulSoup(response.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}
    data = []

    # Loop for extracting product details from each link
    count = 0
    for link in links_list:
        if count == 1:
            break
        link_url = "https://www.amazon.in" + link
        print(f"Fetching data from URL: {link_url}")

        response = requests.get(link_url, headers=HEADERS)
        print(f"Response: {response}")
        #break

        new_soup = BeautifulSoup(response.content, "html.parser")

        #print(f"Response: {response.content}")
        user_reviews = get_user_reviews(new_soup)
        print(f"user_reviews: {user_reviews}")

        data.append({
            "title": get_title(new_soup),
            "price": get_price(new_soup),
            "rating": get_rating(new_soup),
            "reviews": get_review_count(new_soup),
            "availability": get_availability(new_soup),
        })
        count += 1

    print(data)