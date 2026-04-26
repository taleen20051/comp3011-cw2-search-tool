
# COMP3011 Coursework 2 – Search Engine Tool

Python | Web Crawling | Inverted Index | Pytest

## Project Overview

This project implements a command-line search engine for COMP3011 Web Services and Web Data.

The system crawls https://quotes.toscrape.com/, builds an inverted index of words found on each page, stores frequency and position statistics, and allows searching using shell commands.

## Features

- Website crawling with 6-second politeness delay
- Inverted index creation
- Frequency + position storage
- Case-insensitive searching
- build / load / print / find commands
- JSON index storage
- Automated tests with pytest

## Repository Structure

```text
src/
tests/
data/
README.md
requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/taleen20051/comp3011-cw2-search-tool.git
cd comp3011-cw2-search-tool
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Dependencies

- requests
- beautifulsoup4
- pytest
- pytest-cov
- coverage

## Running the Tool

```bash
python src/main.py
```

## Commands

### Build Index

```text
build
```

### Load Index

```text
load
```

### Print Word Entry

```text
print life
```

### Search Query

```text
find good friends
```

## Testing

Run tests:

```bash
pytest -v
```

Run coverage:

```bash
coverage run -m pytest
coverage report -m --omit="src/main.py"
```

## Design Summary

The inverted index uses nested dictionaries:

```python
{
  "word": {
    "url": {
      "frequency": int,
      "positions": [int]
    }
  }
}
```

This provides fast lookup, ranking support, and easy JSON storage.

## GenAI Declaration

GenAI tools such as ChatGPT and Gemini were used for support during debugging, testing ideas, and documentation refinement. All outputs were critically reviewed, tested, and modified before inclusion.

## Author

Taleen Abubaker
University of Leeds
