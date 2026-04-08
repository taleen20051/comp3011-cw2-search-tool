"""
Main command-line interface for the search tool.
"""

from crawler import crawl_website


def main():
    """
    Run a temporary crawler demo.
    """
    pages = crawl_website()

    print("\nCrawl complete.")
    print(f"Total pages crawled: {len(pages)}\n")

    for page in pages[:3]:
        print(f"URL: {page['url']}")
        print(f"Text preview: {page['text'][:200]}")
        print("-" * 60)


if __name__ == "__main__":
    main()