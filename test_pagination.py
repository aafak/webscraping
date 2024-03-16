from bs4 import BeautifulSoup
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
cookie = "session-id=261-8411119-7687861; session-id-time=2082787201l; i18n-prefs=INR; ubid-acbin=262-8727450-4461710; lc-acbin=en_IN; session-token=MFBKNDEi08pX5ftbnb9foFr8nyuArM6ICgVxmLTDKhMKtUiQ5BuRxUPq1+zm4gseBApVWH/77AL/O3oLqwPJJu7cjG0SZnOYMW2cs4F8jPYPn1PPFvtTy0zssHWiDqQoxpiow4GbCWXkvXMJGEYmcZaQ5eU8z6NaMuJ3DaV6KGxcEnmOFRWIYs/ws8c1+YRm+hqbx5ymgJtwa3DjTvcifgjQ07ynKBXZ3ZDPx0lfPyFRiLQv6X17ZTaDgrm7Rsi8uPT2eLf1DZBglMQLfddUkxPl1PkPasH2d4zIFS7YCx17QMGi2h2hYta3OqhA7xVntDXenp13dQv3Sg6j+qwKnIUWkdz7Snvs; csm-hit=tb:N6S3R8EK5WP8CDMV2G12+sa-8K7ZDNGRQV062QC6JSJK-TMQQP83EXKCY3VZABFXQ|1710571377161&t:1710571377161&adb:adblk_no"
HEADERS = ({'User-Agent': USER_AGENT,
            'Accept-Language': 'en-US, en;q=0.5',
            'Cookie': cookie,
            'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"'
            })

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

  reviews = []
  user_review_link = "https://www.amazon.in/Samsung-Storage-MediaTek-Octa-core-Processor/product-reviews/B0BMGC6LHP/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="

  for i in range(1, 10):
      link = user_review_link + str(i)
      print(f"Fetching reviews from link: {link}")
      user_reviews = get_user_reviews(link)
      print(f"Total reviews: {len(reviews)}")
      reviews.extend(user_reviews)

  print(f"Total reviews: {len(reviews)}")
  print(f"reviews: {reviews}")
  print(f"Total reviews: {len(reviews)}")