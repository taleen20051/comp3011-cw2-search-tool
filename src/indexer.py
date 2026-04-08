"""
Indexer module for building an inverted index.
"""

import re
import json
import os


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

    return index  # ✅ IMPORTANT FIX


def save_index(index, filepath="data/index.json"):
    """
    Save the inverted index to a JSON file.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"Index saved to {filepath}")


def load_index(filepath="data/index.json"):
    """
    Load the inverted index from a JSON file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError("Index file not found. Run 'build' first.")

    with open(filepath, "r", encoding="utf-8") as f:
        index = json.load(f)

    print(f"Index loaded from {filepath}")
    return index