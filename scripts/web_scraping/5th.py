import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Step 1: Get the login page to fetch CSRF token
login_url = "https://quotes.toscrape.com/login"
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

# Extract CSRF token
csrf_token = soup.find("input", {"name": "csrf_token"})["value"]

# Step 2: Prepare login data
payload = {
    "username": "test",        # demo username
    "password": "test",        # demo password
    "csrf_token": csrf_token   # required security token
}

# Step 3: Log in
session.post(login_url, data=payload)

# Step 4: Access protected page (quotes after login)
protected_url = "https://quotes.toscrape.com/"
response = session.get(protected_url)
soup = BeautifulSoup(response.text, "html.parser")

# Print first 5 quotes
quotes = soup.find_all("span", class_="text")[:5]
for q in quotes:
    print(q.text)
