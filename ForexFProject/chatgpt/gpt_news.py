import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage content
url = 'https://zpravy.kurzy.cz/l.asp?LT=0&RF=0&RC=30'
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract desired data
# Example: Extracting all article titles and their links
articles = soup.find_all('a', class_='article-title')  # Adjust the tag and class based on actual HTML structure

for article in articles:
    title = article.get_text(strip=True)
    link = article['href']
    print(f'Title: {title}')
    print(f'Link: {link}')
    print('---')
