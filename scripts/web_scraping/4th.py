import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Login URL and payload (form data)
login_url = "https://example.com/login"
payload = {
    "username": "your_username",
    "password": "your_password"
}

# Send POST request to log in
session.post(login_url, data=payload)

# Now, scrape a protected page
protected_url = "https://example.com/dashboard"
response = session.get(protected_url)

# Parse content
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)  # Example: print page title
