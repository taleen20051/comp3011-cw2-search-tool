"""
Indexer module for building an inverted index.
"""

import re


def tokenize(text):
    """
    Convert text into a list of lowercase words.

    Args:
        text: Raw page text.

    Returns:
        List of lowercase word tokens.
    """
    return re.findall(r"\b\w+\b", text.lower())


def build_inverted_index(pages):
    """
    Build an inverted index from crawled pages.

    Args:
        pages: A list of dictionaries with:
            - url
            - text

    Returns:
        A dictionary in the form:
        {
            "word": {
                "page_url": {
                    "frequency": int,
                    "positions": [int, int, ...]
                }
            }
        }
    """
    index = {}

    for page in pages:
        url = page["url"]
        words = tokenize(page["text"])

        for position, word in enumerate(words):
            if word not in index:
                index[word] = {}

            if url not in index[word]:
                index[word][url] = {
                    "frequency": 0,
                    "positions": []
                }

            index[word][url]["frequency"] += 1
            index[word][url]["positions"].append(position)

    return index