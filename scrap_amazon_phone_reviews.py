from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


AMAZON_BASE_URL = "https://www.amazon.in/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
#HEADERS = ({'User-Agent': "", 'Accept-Language': 'en-US, en;q=0.5'})

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "Sec-Ch-Ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Google Chrome\";v=\"122\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-65ed5e12-258e9ba70a89a6ac77f3b96b"
  }

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    #"Referer": "https://www.google.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
}

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

if __name__ == '__main__':

    # add your user agent
    # https://www.whatismybrowser.com/

    # The webpage URL
    search_query = "nike+shoes+men"

    URL = AMAZON_BASE_URL +"s?k="+ search_query

    # # HTTP Request
    # print(f"Fetching data from URL: {URL}")
    # response = requests.get(URL, headers=HEADERS)
    # print(f"response: {response}")
    #
    # product_names = []
    # response = getAmazonSearch(search_query)
    # soup = BeautifulSoup(response.content, "html.parser")
    # count = 0
    # for i in soup.findAll("span", {
    #     'class': 'a-size-base-plus a-color-base a-text-normal'}):  # the tag which is common for all the names of products
    #     product_names.append(i.text)  # adding the product names to the list
    #     if count > 2:
    #         break
    #     count +=1
    #
    # print(f"product_names: {product_names}")

    # data_asin = []
    # response = getAmazonSearch(search_query)
    # count = 0
    # # "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"
    # soup = BeautifulSoup(response.content, "html.parser")
    # for i in soup.findAll("div", {
    #     'class': "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"}):
    #     data_asin.append(i['data-asin'])
    #     if count > 2:
    #         break
    #     count += 1
    #
    # link = []
    # count = 0
    # for i in range(len(data_asin)):
    #     response = Searchasin(data_asin[i])
    #     soup = BeautifulSoup(response.content, "html.parser")
    #     for i in soup.findAll("a", {'data-hook': "see-all-reviews-link-foot"}):
    #         link.append(i['href'])
    #         if count > 2:
    #             break
    #         count += 1
    #
    # print(f"links: {link}")


    link =  ['/Nike-Revolution-Running-Shoes-Black/product-reviews/B0C8THZMZW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews', '/Nike-Revolution-Running-Shoes-Black/product-reviews/B0C8THZMZW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews', '/Nike-Full-Force-Shoes-White/product-reviews/B0CLYWL8QB/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews', '/Nike-Downshifter-White-DK-Grey-Pure-Platinum/product-reviews/B0B56YYS3T/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews', '/Nike-Downshifter-11-Platinum-White-Wolf-GREY-CW3411-004-7UK/product-reviews/B098PCBSDM/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    reviews = []
    #for j in range(len(link)):
    for j in range(2):
        for k in range(1):
            #review_link = "Nike-Revolution-Running-Shoes-Black/product-reviews/B0C8THZMZW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
            review_link = "Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
            #review_link = "Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=2"

            #review_link = "Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=2"

            # response = Searchreviews(link[j] + '&pageNumber=' + str(k))
            response = Searchreviews(review_link)
            print(response)

            #print(f"review response: {response.content}")
            soup = BeautifulSoup(response.content, "html.parser")
            #print(soup)
            #rating = get_rating(soup)
            # a-size-base review-text review-text-content
            #"average-star-rating"
            #for i in soup.find_all("span", {'class': "a-size-base review-text review-text-content"}):
            #for i in soup.find_all("i", {"data-hook":"average-star-rating"}):

            for i in soup.findAll("span", {'data-hook': "review-body"}):
                #print(f"i: {i}")
                reviews.append(i.text)
                #break
        break
        print(reviews)

    print(reviews)