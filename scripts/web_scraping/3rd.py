import requests
from bs4 import BeautifulSoup
import pandas as pd

all_quotes = []
all_authors = []

page = 1
while True:
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if "No quotes found!" in response.text:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [q.text for q in soup.find_all("span", class_="text")]
    authors = [a.text for a in soup.find_all("small", class_="author")]

    all_quotes.extend(quotes)
    all_authors.extend(authors)
    page += 1

# Create DataFrame and save to CSV
df = pd.DataFrame({"Quote": all_quotes, "Author": all_authors})
df.to_csv("quotes.csv", index=False, encoding="utf-8")
print("Quotes saved to quotes.csv")