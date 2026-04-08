from crawler import crawl_website
from indexer import build_inverted_index, save_index, load_index


def main():
    print("Building index...")
    pages = crawl_website()
    index = build_inverted_index(pages)

    save_index(index)

    print("\nLoading index...")
    loaded_index = load_index()

    # test a word
    word = "life"
    if word in loaded_index:
        print(f"\nWord '{word}' found in loaded index:")
        for url, data in loaded_index[word].items():
            print(f"- {url}")
            print(f"  frequency: {data['frequency']}")
            print(f"  positions: {data['positions'][:10]}")
    else:
        print(f"Word '{word}' not found.")


if __name__ == "__main__":
    main()