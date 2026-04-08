from pathlib import Path
import sys

# Make src/ importable
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from indexer import build_inverted_index


def test_build_inverted_index_basic():
    pages = [
        {
            "url": "page1",
            "text": "Life is beautiful life"
        },
        {
            "url": "page2",
            "text": "Life is hard"
        }
    ]

    index = build_inverted_index(pages)

    assert "life" in index

    # Check page1
    assert "page1" in index["life"]
    assert index["life"]["page1"]["frequency"] == 2
    assert index["life"]["page1"]["positions"] == [0, 3]

    # Check page2
    assert "page2" in index["life"]
    assert index["life"]["page2"]["frequency"] == 1
    assert index["life"]["page2"]["positions"] == [0]


def test_index_is_case_insensitive():
    pages = [
        {
            "url": "page1",
            "text": "Life LIFE life"
        }
    ]

    index = build_inverted_index(pages)

    assert "life" in index
    assert index["life"]["page1"]["frequency"] == 3


def test_multiple_words_indexed():
    pages = [
        {
            "url": "page1",
            "text": "hello world"
        }
    ]

    index = build_inverted_index(pages)

    assert "hello" in index
    assert "world" in index

    assert index["hello"]["page1"]["frequency"] == 1
    assert index["world"]["page1"]["frequency"] == 1