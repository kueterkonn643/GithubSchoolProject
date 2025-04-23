import requests
from bs4 import BeautifulSoup
import time

def fetch_news(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            news_items = soup.find_all("div", class_="news-item")
            return [item.get_text(strip=True) for item in news_items]
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the web page: {e}")

url = "https://example.com/news"
news = fetch_news(url)
for news in news:
    print(news)
