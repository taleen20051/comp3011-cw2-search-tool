from crawler import crawl_website
from indexer import build_inverted_index


def main():
    pages = crawl_website()
    index = build_inverted_index(pages)

    print(f"Total unique words: {len(index)}")

    word = "life"
    if word in index:
        print(f"\nWord '{word}' found in:")
        for url, data in index[word].items():
            print(f"- {url}")
            print(f"  frequency: {data['frequency']}")
            print(f"  positions: {data['positions'][:10]}")
    else:
        print(f"Word '{word}' not found.")


if __name__ == "__main__":
    main()