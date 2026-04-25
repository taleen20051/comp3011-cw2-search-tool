"""
Indexer module for building, saving, and loading an inverted index.
"""

import json
import os
import re


def tokenize(text):
    """
    Convert raw text into lowercase word tokens.

    Punctuation is removed and the search is case-insensitive.
    """
    return re.findall(r"\b\w+\b", text.lower())


def build_inverted_index(pages):
    """
    Build an inverted index from crawled pages.

    Structure:
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
                    "positions": [],
                }

            index[word][url]["frequency"] += 1
            index[word][url]["positions"].append(position)

    return index


def save_index(index, filepath="data/index.json"):
    """
    Save the inverted index to a JSON file.
    """
    directory = os.path.dirname(str(filepath))
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(index, file, indent=2)

    print(f"Index saved to {filepath}")


def load_index(filepath="data/index.json"):
    """
    Load the inverted index from a JSON file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError("Index file not found. Run 'build' first.")

    with open(filepath, "r", encoding="utf-8") as file:
        index = json.load(file)

    print(f"Index loaded from {filepath}")
    return index