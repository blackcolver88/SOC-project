import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
URL = 'https://www.bbc.com/news'

# Send a GET request to fetch the HTML content
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all headline elements (use the right HTML tags and classes)
    headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

    print("Top BBC News Headlines:")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline.text}")
else:
    print(f"Error: Unable to fetch content from {URL}. HTTP Status code: {response.status_code}")