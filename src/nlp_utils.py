import spacy

# Load the English language model for spaCy
nlp = spacy.load("en_core_web_sm")


# Function to tokenize user input
def tokenize(text):
    """
    Tokenize the input text.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokens.
    """
    doc = nlp(text)
    return [token.text for token in doc]


# Function for intent recognition
def recognize_intent(tokens):
    """
    Recognize the intent behind the user's query.

    Args:
        tokens (list): A list of tokens representing the user's input.

    Returns:
        str: The recognized intent.
    """
    # For simplicity, let's assume the first token represents the intent
    if tokens:
        return tokens[0].lower()  # Return the first token as the intent
    else:
        return None  # Return None if no tokens are provided
