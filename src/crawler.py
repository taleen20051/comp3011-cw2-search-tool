"""
Crawler module for crawling pages from quotes.toscrape.com.
"""

import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://quotes.toscrape.com/"
POLITENESS_DELAY = 6
REQUEST_TIMEOUT = 10


def extract_page_text(soup):
    """
    Extract all quote text from a BeautifulSoup page object.
    """
    quote_elements = soup.find_all("div", class_="quote")
    quotes = []

    for quote in quote_elements:
        text_span = quote.find("span", class_="text")
        if text_span:
            quotes.append(text_span.get_text(strip=True))

    return " ".join(quotes)


def find_next_page_url(soup, current_url):
    """
    Find the absolute URL of the next page.
    """
    next_list_item = soup.find("li", class_="next")
    if not next_list_item:
        return None

    next_link = next_list_item.find("a")
    if not next_link or not next_link.get("href"):
        return None

    return urljoin(current_url, next_link["href"])


def crawl_website():
    """
    Crawl quotes.toscrape.com and return a list of page dictionaries.
    """
    crawled_pages = []
    visited_urls = set()
    current_url = BASE_URL

    while current_url and current_url not in visited_urls:
        print(f"Crawling: {current_url}")

        try:
            response = requests.get(current_url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Error fetching {current_url}: {error}")
            break

        visited_urls.add(current_url)

        soup = BeautifulSoup(response.text, "html.parser")
        page_text = extract_page_text(soup)

        crawled_pages.append(
            {
                "url": current_url,
                "text": page_text,
            }
        )

        next_url = find_next_page_url(soup, current_url)

        if next_url:
            print(f"Waiting {POLITENESS_DELAY} seconds before next request...")
            time.sleep(POLITENESS_DELAY)

        current_url = next_url

    return crawled_pages