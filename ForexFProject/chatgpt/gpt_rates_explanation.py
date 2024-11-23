import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://www.marketwatch.com/latest-news/currencies"

# Send an HTTP request to the URL
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section containing the "Recent Currency News"
currency_news_section = soup.find('div', class_='element element--article')
if currency_news_section:
    articles = currency_news_section.find_all('a')
    for article in articles:
        title = article.text.strip()
        link = article['href']
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()
else:
    print("Currency News section not found.")
