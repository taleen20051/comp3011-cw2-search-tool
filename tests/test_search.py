from pathlib import Path
import sys

# Make src/ importable
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from search import find_query, print_word


def sample_index():
    return {
        "life": {
            "page1": {"frequency": 2, "positions": [0, 3]},
            "page2": {"frequency": 1, "positions": [0]},
        },
        "good": {
            "page1": {"frequency": 1, "positions": [4]},
            "page3": {"frequency": 1, "positions": [1]},
            "page5": {"frequency": 3, "positions": [2, 7, 9]},
        },
        "friends": {
            "page1": {"frequency": 1, "positions": [5]},
            "page4": {"frequency": 1, "positions": [2]},
            "page5": {"frequency": 2, "positions": [3, 8]},
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


def test_print_word_returns_none_for_empty_word():
    index = sample_index()

    result = print_word(index, "   ")

    assert result is None


def test_find_query_returns_pages_containing_all_words_ranked_by_score():
    index = sample_index()

    result = find_query(index, "good friends")

    assert result == [("page5", 5), ("page1", 2)]


def test_find_query_returns_empty_list_when_word_missing():
    index = sample_index()

    result = find_query(index, "good missing")

    assert result == []


def test_find_query_returns_empty_list_for_empty_query():
    index = sample_index()

    result = find_query(index, "")

    assert result == []


def test_find_query_is_case_insensitive():
    index = sample_index()

    result = find_query(index, "GOOD FRIENDS")

    assert result == [("page5", 5), ("page1", 2)]


def test_find_query_ignores_punctuation():
    index = sample_index()

    result = find_query(index, "good, friends!")

    assert result == [("page5", 5), ("page1", 2)]


def test_find_query_returns_single_word_results_ranked_by_frequency():
    index = sample_index()

    result = find_query(index, "good")

    assert result == [("page5", 3), ("page1", 1), ("page3", 1)]