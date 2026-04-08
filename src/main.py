from crawler import crawl_website
from indexer import build_inverted_index, save_index, load_index
from search import print_word, find_query


def main():
    print("Building index...")
    pages = crawl_website()
    index = build_inverted_index(pages)
    save_index(index)

    print("\nLoading index...")
    loaded_index = load_index()

    word = "life"
    word_entry = print_word(loaded_index, word)

    print(f"\nPRINT COMMAND TEST: '{word}'")
    if word_entry:
        for url, data in word_entry.items():
            print(f"- {url}")
            print(f"  frequency: {data['frequency']}")
            print(f"  positions: {data['positions'][:10]}")
    else:
        print("Word not found.")

    query = "good friends"
    results = find_query(loaded_index, query)

    print(f"\nFIND COMMAND TEST: '{query}'")
    if results:
        for url in results:
            print(f"- {url}")
    else:
        print("No matching pages found.")


if __name__ == "__main__":
    main()