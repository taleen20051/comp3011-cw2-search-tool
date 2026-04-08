"""
Search module for loading, printing, and querying the index.
"""

def print_word(index, word):
    """Print the inverted index entry for a word."""
    print(f"Word: {word}")
    print(index.get(word, "Not found"))


def find_query(index, query):
    """Return matching pages for a query."""
    print(f"Searching for: {query}")
    return []