import requests
from bs4 import BeautifulSoup

# Fetch page
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract all quotes
quotes = soup.find_all("span", class_="text")
for q in quotes:
    print(q.text)


# Get author names
authors = soup.find_all("small", class_="author")
for a in authors:
    print(a.text)

# Extract all links from the page
for link in soup.find_all("a"):
    print(link.get("href"))

# Scrape Multiple Pages (Looping)
page = 1
while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if "No quotes found!" in response.text:
        break
    soup = BeautifulSoup(response.text, "html.parser")
    for q in soup.find_all("span", class_="text"):
        print(q.text)
    page += 1
