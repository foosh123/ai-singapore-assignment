import requests
from collections import Counter
import re

def fetch_text_from_url(url):
    """
    Fetch raw text content from a given URL.

    Parameters:
        url (str): The URL to fetch text from.

    Returns:
        str: The raw text content of the URL.
    """
    try:
        response = requests.get(url, timeout=10)  # Set timeout for the request
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching text from URL: {e}")

def extract_clean_text(html):
    """
    Extract and clean visible text from raw HTML.

    Parameters:
        html (str): Raw HTML content.

    Returns:
        str: Cleaned visible text.
    """
    # Remove script and style content
    html = re.sub(r"(?s)<(script|style).*?>.*?</\1>", "", html)
    # Remove all HTML tags
    text = re.sub(r"<.*?>", "", html)
    # Replace multiple spaces/newlines with a single space
    return re.sub(r"\s+", " ", text).strip()

def tokenize_text(text):
    """
    Tokenize text into a list of words, handling basic punctuation.

    Parameters:
        text (str): Input text.

    Returns:
        list: A list of lowercase words.
    """
    return re.findall(r"\b[\w'-]+\b", text.lower())

def get_frequent_words(words, start_rank, end_rank):
    """
    Get words ranked by frequency between specified ranks.

    Parameters:
        words (list): A list of words.
        start_rank (int): The starting rank (inclusive).
        end_rank (int): The ending rank (inclusive).

    Returns:
        list: A list of tuples with words and their frequencies.
    """
    if not words:
        return []
    word_counts = Counter(words)
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[start_rank - 1:end_rank]

if __name__ == "__main__":
    # Constants
    URL = "https://www.gutenberg.org/cache/epub/16317/pg16317.txt"
    START_RANK = 10
    END_RANK = 20

    try:
        # Fetch and process the text
        raw_text = fetch_text_from_url(URL)
        clean_text = extract_clean_text(raw_text)
        words = tokenize_text(clean_text)

        # Get words ranked by frequency
        top_words = get_frequent_words(words, START_RANK, END_RANK)

        # Display results
        print(f"Words ranked from {START_RANK}th to {END_RANK}th by frequency:")
        for rank, (word, count) in enumerate(top_words, start=START_RANK):
            print(f"{rank}. {word}: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")
