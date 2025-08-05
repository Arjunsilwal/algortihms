import requests
from bs4 import BeautifulSoup
import csv

# Open CSV file for writing
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # Header row

    page = 1
    while True:
        url = f"https://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        if "No quotes found!" in response.text:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        for q, a in zip(quotes, authors):
            writer.writerow([q.text, a.text])

        page += 1

print("Quotes saved to quotes.csv")
