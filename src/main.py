# Main command-line interface for the search engine.

from crawler import crawl_website
from indexer import build_inverted_index, load_index, save_index
from search import find_query, print_word


def main():
    # Run the interactive command-line shell.
    index = None

    print("Simple Search Engine CLI")
    print("Commands: build, load, print <word>, find <query>, quit, exit")

    while True:
        try:
            # Read a command from the user.
            command = input("\nEnter command: ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if command == "build":
            # Crawl the website, build the index, and save it.
            print("Building index...")
            pages = crawl_website()
            index = build_inverted_index(pages)
            save_index(index)
            print("Index built and saved successfully.")

        elif command == "load":
            # Load an existing index file.
            try:
                index = load_index()
                print("Index loaded successfully.")
            except FileNotFoundError as error:
                print(error)

        elif command.startswith("print "):
            # Display index data for a single word.
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

        elif command == "print":
            print("Please provide a word. Example: print nonsense")

        elif command.startswith("find "):
            # Search for pages containing the query words.
            if index is None:
                print("No index loaded. Use 'build' or 'load' first.")
                continue

            query = command.split(" ", 1)[1].strip()
            results = find_query(index, query)

            if not results:
                print("No results found.")
            else:
                print(f"\nRanked results for '{query}':")
                for url, score in results:
                    print(f"- {url} (score: {score})")

        elif command == "find":
            print("Please provide a query. Example: find good friends")

        elif command in {"quit", "exit"}:
            print("Goodbye!")
            break

        else:
            print("Invalid command. Use: build, load, print <word>, find <query>, quit, exit")


if __name__ == "__main__":
    main()