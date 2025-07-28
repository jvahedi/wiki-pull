import wikipediaapi
from tenacity import (
    retry,
    stop_after_attempt,  # Added for limiting retry attempts
    wait_exponential  # Changed from wait_fixed to wait_exponential
)

@retry(wait=wait_exponential(multiplier=1, min=2, max=7))#, stop=stop_after_attempt(5))  # Modified retry logic
def wikiRespond(title, pattern = ''):
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MyProjectName (merlin@example.com)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    p_wiki = wiki_wiki.page(title)
    
    html_text = p_wiki.text
    
    # Regex pattern to find the first number (possibly with commas) after the word "population"
    if pattern == '': 
        return html_text
    else: 
        #pattern = r'population\s+[^\d]*(\d{1,3}(?:,\d{3})*)(?=[^\d]*(?:\.|\s))'
        
        # Search for the pattern in the HTML text
        match = re.search(pattern, html_text, re.IGNORECASE)
        
        # Print the first number found after "population" if it exists
        if match:
            repond = match.group(1)
        else:
            respond = "NULL"
        return respond