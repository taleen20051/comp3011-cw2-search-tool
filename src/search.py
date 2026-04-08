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
    Find pages that contain all words in the query, ranked by total term frequency.

    Ranking method:
    - Only pages containing all query words are returned.
    - Each matching page gets a score equal to the sum of the frequencies
      of all query words on that page.
    - Results are sorted by descending score, then alphabetically by URL.

    Args:
        index: The inverted index dictionary.
        query: A search query string.

    Returns:
        A list of tuples in the form:
        [(page_url, score), ...]
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

    ranked_results = []
    for page_url in matching_pages:
        score = sum(index[word][page_url]["frequency"] for word in query_words)
        ranked_results.append((page_url, score))

    ranked_results.sort(key=lambda item: (-item[1], item[0]))
    return ranked_results