from bs4 import BeautifulSoup
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
HEADERS = ({'User-Agent': USER_AGENT, 'Accept-Language': 'en-US, en;q=0.5'})

def get_user_reviews(review_link):
    response = requests.get(url=review_link, headers=HEADERS)

    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    # with open("page2.html", "w", encoding='utf-8') as f:
    #     f.write(str(soup))

    reviews = soup.find_all("span", {'data-hook': "review-body"})
    user_reviews = []
    for r in reviews:
        user_reviews.append(r.text.strip())

    print(f"Total reviews : {len(user_reviews)}")
    print(user_reviews)
    return user_reviews


if __name__ == '__main__':

  user_review_link = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=1"
  get_user_reviews(user_review_link)

  # following link not working
  # user_review_link = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=2"
  # get_user_reviews(user_review_link)
  #




#URL = "https://www.amazon.in/Redmi-Arctic-Storage-Dimensity-Slimmest/product-reviews/B0CQPGG8KG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&pageNumber=2"
#response = requests.get("http://localhost:8050/render.html", params={'url':URL, 'wait': 2})
