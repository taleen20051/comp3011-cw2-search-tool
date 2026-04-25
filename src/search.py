# Search module for inspecting and querying the inverted index.

from indexer import tokenize


def print_word(index, word):
    # Return the inverted index entry for a single word.
    normalized_word = word.strip().lower()

    if not normalized_word:
        return None

    return index.get(normalized_word)


def find_query(index, query):
    # Find pages containing all words in a query and rank results.
    query_words = tokenize(query)

    if not query_words:
        return []

    page_sets = []

    for word in query_words:
        # If any query word is missing, no page can match.
        if word not in index:
            return []

        page_sets.append(set(index[word].keys()))

    # Keep only pages containing every query word.
    matching_pages = set.intersection(*page_sets)

    ranked_results = []

    for page_url in matching_pages:
        # Score pages using total query-word frequency.
        score = sum(index[word][page_url]["frequency"] for word in query_words)
        ranked_results.append((page_url, score))

    # Sort by highest score first, then alphabetically by URL.
    ranked_results.sort(key=lambda item: (-item[1], item[0]))
    return ranked_results