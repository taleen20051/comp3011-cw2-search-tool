from pathlib import Path
import sys

# Make src/ importable
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from search import print_word, find_query


def sample_index():
    return {
        "life": {
            "page1": {"frequency": 2, "positions": [0, 3]},
            "page2": {"frequency": 1, "positions": [0]},
        },
        "good": {
            "page1": {"frequency": 1, "positions": [4]},
            "page3": {"frequency": 1, "positions": [1]},
        },
        "friends": {
            "page1": {"frequency": 1, "positions": [5]},
            "page4": {"frequency": 1, "positions": [2]},
        },
    }


def test_print_word_returns_entry_for_existing_word():
    index = sample_index()

    result = print_word(index, "life")

    assert result == {
        "page1": {"frequency": 2, "positions": [0, 3]},
        "page2": {"frequency": 1, "positions": [0]},
    }


def test_print_word_is_case_insensitive():
    index = sample_index()

    result = print_word(index, "LiFe")

    assert result == index["life"]


def test_print_word_returns_none_for_missing_word():
    index = sample_index()

    result = print_word(index, "missing")

    assert result is None


def test_find_query_returns_pages_containing_all_words():
    index = sample_index()

    result = find_query(index, "good friends")

    assert result == ["page1"]


def test_find_query_returns_empty_list_when_word_missing():
    index = sample_index()

    result = find_query(index, "good missing")

    assert result == []


def test_find_query_returns_empty_list_for_empty_query():
    index = sample_index()

    result = find_query(index, "")

    assert result == []