from pathlib import Path
import sys
import requests

from bs4 import BeautifulSoup

# Make src/ importable when running pytest from project root
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from crawler import crawl_website, extract_page_text, find_next_page_url


class MockResponse:
    """Simple mock response object for requests.get()."""

    def __init__(self, html_text, status_code=200):
        self.text = html_text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.RequestException(f"HTTP error: {self.status_code}")


def test_extract_page_text_returns_all_quotes():
    html = """
    <html>
        <body>
            <div class="quote">
                <span class="text">Quote one.</span>
            </div>
            <div class="quote">
                <span class="text">Quote two.</span>
            </div>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")

    result = extract_page_text(soup)

    assert result == "Quote one. Quote two."


def test_find_next_page_url_returns_absolute_url():
    html = """
    <html>
        <body>
            <li class="next">
                <a href="/page/2/">Next</a>
            </li>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")

    result = find_next_page_url(soup, "https://quotes.toscrape.com/")

    assert result == "https://quotes.toscrape.com/page/2/"


def test_find_next_page_url_returns_none_when_no_next_link():
    html = """
    <html>
        <body>
            <p>No next page here.</p>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, "html.parser")

    result = find_next_page_url(soup, "https://quotes.toscrape.com/")

    assert result is None


def test_crawl_website_returns_multiple_mocked_pages(monkeypatch):
    page_1_html = """
    <html>
        <body>
            <div class="quote">
                <span class="text">First page quote.</span>
            </div>
            <li class="next">
                <a href="/page/2/">Next</a>
            </li>
        </body>
    </html>
    """

    page_2_html = """
    <html>
        <body>
            <div class="quote">
                <span class="text">Second page quote.</span>
            </div>
        </body>
    </html>
    """

    pages_by_url = {
        "https://quotes.toscrape.com/": MockResponse(page_1_html),
        "https://quotes.toscrape.com/page/2/": MockResponse(page_2_html),
    }

    def mock_get(url, timeout):
        return pages_by_url[url]

    sleep_calls = []

    def mock_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr("crawler.requests.get", mock_get)
    monkeypatch.setattr("crawler.time.sleep", mock_sleep)

    result = crawl_website()

    assert len(result) == 2

    assert result[0]["url"] == "https://quotes.toscrape.com/"
    assert result[0]["text"] == "First page quote."

    assert result[1]["url"] == "https://quotes.toscrape.com/page/2/"
    assert result[1]["text"] == "Second page quote."

    assert sleep_calls == [6]


def test_crawl_website_stops_gracefully_on_request_error(monkeypatch):
    def mock_get(url, timeout):
        raise requests.RequestException("Network failure")

    monkeypatch.setattr("crawler.requests.get", mock_get)

    result = crawl_website()

    assert result == []


def test_crawl_website_stops_gracefully_on_http_error(monkeypatch):
    def mock_get(url, timeout):
        return MockResponse("<html></html>", status_code=500)

    monkeypatch.setattr("crawler.requests.get", mock_get)

    result = crawl_website()

    assert result == []