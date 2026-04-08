"""
Main command-line interface for the search engine.
"""

from crawler import crawl_website
from indexer import build_inverted_index, save_index, load_index
from search import print_word, find_query


def main():
    """Run the interactive command-line shell."""
    index = None

    print("Simple Search Engine CLI")
    print("Commands: build, load, print <word>, find <query>, quit")

    while True:
        command = input("\nEnter command: ").strip()

        if command == "build":
            print("Building index...")
            pages = crawl_website()
            index = build_inverted_index(pages)
            save_index(index)
            print("Index built and saved successfully.")

        elif command == "load":
            try:
                index = load_index()
                print("Index loaded successfully.")
            except FileNotFoundError as error:
                print(error)

        elif command.startswith("print "):
            if index is None:
                print("No index loaded. Use 'build' or 'load' first.")
                continue

            word = command.split(" ", 1)[1].strip()
            result = print_word(index, word)

            if result is None:
                print(f"Word '{word}' not found.")
            else:
                print(f"\nInverted index entry for '{word}':")
                for url, data in result.items():
                    print(f"- {url}")
                    print(f"  frequency: {data['frequency']}")
                    print(f"  positions: {data['positions']}")

        elif command.startswith("find "):
            if index is None:
                print("No index loaded. Use 'build' or 'load' first.")
                continue

            query = command.split(" ", 1)[1].strip()
            results = find_query(index, query)

            if not results:
                print("No results found.")
            else:
                print(f"\nPages containing '{query}':")
                for url in results:
                    print(f"- {url}")

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Use: build, load, print <word>, find <query>, quit")


if __name__ == "__main__":
    main()