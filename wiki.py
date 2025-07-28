import wikipediaapi
import regex as re
from tenacity import (
    retry,
    stop_after_attempt,  # Used to limit retry attempts
    wait_exponential     # Exponential backoff for retries
)

@retry(wait=wait_exponential(multiplier=1, min=2, max=7))
def wikiRespond(title, pattern=''):
    """
    Fetches the text of a Wikipedia article and optionally extracts information using a regex pattern.

    Args:
        title (str): The title of the Wikipedia article to fetch.
        pattern (str, optional): A regex pattern to extract specific information from the article text.
            If empty, returns the full article text. Defaults to ''.

    Returns:
        str: The full article text if no pattern is provided, or the first regex match if a pattern is given.
             Returns "NULL" if no match is found.

    Raises:
        Exception: If the Wikipedia API call fails or the page does not exist.
    """
    # Initialize the Wikipedia API client with a custom user agent and English language
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (merlin@example.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    # Fetch the Wikipedia page object
    p_wiki = wiki_wiki.page(title)
    
    # Get the plain text content of the page
    html_text = p_wiki.text
    
    # If no pattern is provided, return the full article text
    if pattern == '':
        return html_text
    else:
        # Search for the pattern in the article text (case-insensitive)
        match = re.search(pattern, html_text, re.IGNORECASE)
        
        # Return the first regex group if a match is found, otherwise "NULL"
        if match:
            respond = match.group(1)
        else:
            respond = "NULL"
        return respond
