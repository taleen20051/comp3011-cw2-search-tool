# COMP3011 Coursework 2 – Search Engine Tool

## Project Overview

This project was developed for **COMP3011: Web Services and Web Data**.

The aim of this coursework is to implement a small search engine in Python that demonstrates the core principles of web crawling, inverted indexing, query processing, ranking, file-based storage, and automated testing.

The tool crawls the target website:

https://quotes.toscrape.com/

It extracts quote text from each page, builds an inverted index of all word occurrences, stores useful statistics, and allows the user to search through an interactive command-line interface.

---

## Coursework Requirements Addressed

This implementation satisfies the required coursework brief:

- Crawl pages of the target website
- Observe a politeness delay of at least 6 seconds between requests
- Build an inverted index while crawling
- Store word frequency and word positions
- Support case-insensitive search
- Provide the required commands:
  - `build`
  - `load`
  - `print <word>`
  - `find <query>`
- Save the compiled index to the file system
- Load the compiled index from the file system
- Include automated tests
- Include a compiled index file

---

## Repository Structure

```text
comp3011-cw2-search-tool/
├── src/
│   ├── crawler.py
│   ├── indexer.py
│   ├── search.py
│   └── main.py
├── tests/
│   ├── test_crawler.py
│   ├── test_indexer.py
│   └── test_search.py
├── data/
│   └── index.json
├── requirements.txt
└── README.md
```

## **Installation and Setup**

### **1. Clone Repository**

git clone `<your-github-repository-url>`
cd comp3011-cw2-search-tool

### **2. Create Virtual Environment**

python3 -m venv venv
source venv/bin/activate

### **3. Install Dependencies**

pip install -r requirements.txt

## **Dependencies**

requests
beautifulsoup4
pytest
pytest-cov
coverage

## **Running the Search Tool**

python src/main.py

You will see:

Simple Search Engine CLI
Commands: build, load, print `<word>`, find `<query>`, quit, exit

## **Command Usage**

### **build**

Crawls the website, builds the index, and saves it.

### **load**

Loads a previously saved index file.

### **print**

Displays the inverted index entry for a specific word.

```
print life
```

### **find**

Searches for pages containing one or more query words.

```
find good friends
```


## **Example CLI Demonstration**

```
build
print life
find good friends
find missingword
find
load
exit
```


This demonstrates:

* Crawling and indexing
* Saving index file
* Loading index file
* Printing a word entry
* Multi-word search
* Missing word handling
* Empty query handling
* Clean exit

---

## **Inverted Index Design**

The inverted index uses a nested dictionary structure:

```
{
    "word": {
        "page_url": {
            "frequency": 3,
            "positions": [2, 7, 9]
        }
    }
}
```


### **Why This Design?**

This structure allows:

* Fast word lookup
* Frequency-based ranking
* Position storage
* Easy JSON storage
* Easy explanation in coursework video

---

## **Search Ranking Method**

For multi-word queries:

1. Query is converted to lowercase
2. Query is tokenised
3. Only pages containing all query words are returned
4. Score = sum of query word frequencies on the page
5. Results sorted by descending score

Example:

```
find good friends
```

Possible output:

https://quotes.toscrape.com/page/2/ (score: 8)
https://quotes.toscrape.com/page/6/ (score: 2)


## **Crawling Design**

The crawler begins at:

```
https://quotes.toscrape.com/
```

It follows the Next page link until no further page exists.

It extracts quote text only.

A visited URL set prevents duplicate crawling.

---

## **Politeness Window**

The coursework requires a minimum 6-second delay between requests.

Implemented using:

```
time.sleep(6)
```

This is only applied when another page is about to be requested.

---

## **Error Handling**

The tool handles:

* Network failures
* HTTP errors
* Missing index file
* Empty queries
* Unknown commands
* Missing words
* Keyboard interruption (`Ctrl+C`)

Example outputs:

```
No results found.
Word 'missingword' not found.
Index file not found. Run 'build' first.
Please provide a query. Example: find good friends
```

## **Testing**

Run all tests:

```
pytest -v
```

Current result shows: 24 passed

## **Coverage**

Run coverage:

```
coverage run -m pytest
coverage report -m --omit="src/main.py"
```

Current Result shows 99% coverage on core modules


The report focuses on:

* `crawler.py`
* `indexer.py`
* `search.py`

The interactive CLI in `main.py` is demonstrated manually in the video.

---

## **Testing Strategy**

Tests cover:

### **crawler.py**

* HTML extraction
* Next-page detection
* Multi-page crawling
* Politeness delay
* Request errors
* HTTP errors

### **indexer.py**

* Tokenisation
* Case-insensitive indexing
* Frequency counting
* Position storage
* Save/load functionality

### **search.py**

* Single-word search
* Multi-word search
* Empty query handling
* Missing word handling
* Ranking correctness
* Case-insensitive queries

---

## **Code Quality**

The project is modular:

* `crawler.py` handles crawling
* `indexer.py` handles indexing and storage
* `search.py` handles searching
* `main.py` provides CLI interaction

This improves readability, testing, and maintainability.

---

## **Version Control**

Git was used throughout development with regular commits.

Typical workflow:

1. Build crawler
2. Build indexer
3. Add storage
4. Add search logic
5. Add tests
6. Improve documentation
7. Final polish

---

## **GenAI Declaration**

Generative AI tools were used for:

* Debugging assistance
* Improving test coverage
* Reviewing structure
* Documentation drafting
* Identifying edge cases

All outputs were reviewed, tested, and understood before inclusion.

---

## **GenAI Critical Reflection**

GenAI helped speed up development, especially for testing ideas and spotting edge cases. However, not all suggestions were accepted directly. Some generated solutions were unnecessarily complex or required modification.

I still needed to debug code manually, run tests, verify outputs, and ensure the final implementation matched the coursework brief.

This process improved both productivity and understanding, but required critical judgement rather than blind acceptance.

---

## **Future Improvements**

Possible extensions:

* TF-IDF ranking
* Phrase search
* Stemming
* Stop-word removal
* Query suggestions
* Search snippets
* Web interface

These were outside the coursework scope.

---

## **Submission Checklist**

Before submitting:

* Public GitHub repository
* README included
* Source code included
* `tests/` included
* `data/index.json` included or attached
* 5-minute video uploaded
* Video link works in incognito mode
* Final TXT/PDF contains:
  * Video link
  * GitHub URL
  * Index file attachment/link

---

## **Author**

Taleen Abubaker

University of Leeds

COMP3011 – Web Services and Web Data
