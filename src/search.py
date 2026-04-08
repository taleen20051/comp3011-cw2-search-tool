"""
Search module for inspecting and querying the inverted index.
"""

from indexer import tokenize


def print_word(index, word):
    """
    Return the inverted index entry for a single word.

    Args:
        index: The inverted index dictionary.
        word: The word to look up.

    Returns:
        The index entry for the word, or None if not found.
    """
    normalized_word = word.strip().lower()

    if not normalized_word:
        return None

    return index.get(normalized_word)


def find_query(index, query):
    """
    Find pages that contain all words in the query.

    Args:
        index: The inverted index dictionary.
        query: A search query string.

    Returns:
        A list of matching page URLs sorted alphabetically.
    """
    query_words = tokenize(query)

    if not query_words:
        return []

    page_sets = []

    for word in query_words:
        if word not in index:
            return []

        pages_for_word = set(index[word].keys())
        page_sets.append(pages_for_word)

    matching_pages = set.intersection(*page_sets)

    return sorted(matching_pages)