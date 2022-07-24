from os import getenv
from dotenv import load_dotenv

def get_todoist_api_key():
    """
    Read the Todoist API key from the environment variables.

    Args:
        None
    
    Returns:
        str: The Todoist API key.
    
    Raises:
        Exception: If the Todoist API key is not found.
    """
    load_dotenv() # Loads the .env file into the environment
    key = getenv('TODOIST_API_KEY')
    if key is None:
        raise Exception('TODOIST_API_KEY environment variable not set.')
    return key