# Wikipedia Query Utility

A lightweight Python utility for **retrieving and extracting information from Wikipedia articles** using the `wikipediaapi` library, with robust retry logic for reliability. This tool is ideal for programmatically fetching article content and extracting specific data patterns (such as population figures) from Wikipedia pages.

---

## Features

- **Fetch Wikipedia Article Content:**  
  Retrieve the full text of any Wikipedia article by title.

- **Pattern-Based Extraction:**  
  Optionally extract specific information from the article text using regular expressions (e.g., population numbers, dates, etc.).

- **Robust Retry Logic:**  
  Automatically retries failed requests with exponential backoff for improved reliability.

---

## Installation Instructions

1. **Install required packages:**
   ```bash
   pip install wikipedia-api tenacity
   ```

2. *(Optional)* If you plan to use advanced pattern matching, ensure you have the `regex` module:
   ```bash
   pip install regex
   ```

---

## Basic Usage

```python
import re
from wiki import wikiRespond  # Replace 'your_module' with the actual filename (without .py)

# Example 1: Get the full text of a Wikipedia article
text = wikiRespond("New York City")
print(text)

# Example 2: Extract the first population number from the article
pattern = r'population\s+[^\d]*(\d{1,3}(?:,\d{3})*)'
population = wikiRespond("New York City", pattern=pattern)
print("Population:", population)
```

---

## License Information

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## Contact Information

For questions or support, please contact:
- **GitHub Issues:** [https://github.com/yourusername/wikipedia-query-utility/issues](https://github.com/yourusername/wikipedia-query-utility/issues)

---
