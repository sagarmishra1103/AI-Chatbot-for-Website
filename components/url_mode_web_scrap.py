import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_html(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text

def clean_soup(soup):
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()
    return soup

def extract_text(soup):
    content = []

    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            content.append(text)

    for tag in soup.find_all("p"):
        text = tag.get_text(strip=True)
        if text:
            content.append(text)

    for tag in soup.find_all("li"):
        text = tag.get_text(strip=True)
        if text:
            content.append(text)

    return "\n".join(content)

def scrape_website(url: str) -> str:
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    soup = clean_soup(soup)
    text = extract_text(soup)

    if not text.strip():
        raise Exception("No usable content found.")

    return text