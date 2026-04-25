from pathlib import Path
import sys

# Make src/ importable
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from indexer import build_inverted_index, load_index, save_index, tokenize


def test_build_inverted_index_basic():
    pages = [
        {
            "url": "page1",
            "text": "Life is beautiful life",
        },
        {
            "url": "page2",
            "text": "Life is hard",
        },
    ]

    index = build_inverted_index(pages)

    assert "life" in index

    assert "page1" in index["life"]
    assert index["life"]["page1"]["frequency"] == 2
    assert index["life"]["page1"]["positions"] == [0, 3]

    assert "page2" in index["life"]
    assert index["life"]["page2"]["frequency"] == 1
    assert index["life"]["page2"]["positions"] == [0]


def test_index_is_case_insensitive():
    pages = [
        {
            "url": "page1",
            "text": "Life LIFE life",
        }
    ]

    index = build_inverted_index(pages)

    assert "life" in index
    assert index["life"]["page1"]["frequency"] == 3


def test_multiple_words_indexed():
    pages = [
        {
            "url": "page1",
            "text": "hello world",
        }
    ]

    index = build_inverted_index(pages)

    assert "hello" in index
    assert "world" in index

    assert index["hello"]["page1"]["frequency"] == 1
    assert index["world"]["page1"]["frequency"] == 1


def test_tokenize_removes_punctuation_and_lowercases_words():
    result = tokenize("Good, GOOD! friends?")

    assert result == ["good", "good", "friends"]


def test_tokenize_handles_empty_text():
    result = tokenize("")

    assert result == []


def test_build_inverted_index_handles_empty_page_text():
    pages = [
        {
            "url": "page1",
            "text": "",
        }
    ]

    index = build_inverted_index(pages)

    assert index == {}


def test_save_and_load_index_round_trip(tmp_path):
    index = {
        "life": {
            "page1": {
                "frequency": 2,
                "positions": [0, 3],
            }
        }
    }

    filepath = tmp_path / "index.json"

    save_index(index, filepath)
    loaded_index = load_index(filepath)

    assert loaded_index == index


def test_load_index_raises_file_not_found_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing_index.json"

    try:
        load_index(missing_file)
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError as error:
        assert "Run 'build' first" in str(error)