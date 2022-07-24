from os import getenv
from dotenv import load_dotenv
import json

def get_todoist_api_key(envname = 'TODOIST_API_KEY'):
    """
    Read the Todoist API key from the environment variables.

    Args:
        envname: The name of the environment variable.
    
    Returns:
        str: The Todoist API key.
    
    Raises:
        Exception: If the Todoist API key is not found.
    """
    load_dotenv() # Loads the .env file into the environment
    key = getenv(envname)
    if key is None:
        raise Exception(f'{envname} not set.')
    return key

def read_time_labels(filename = 'time_label_naming.json'):
    """
    Read the time labels from a json file.

    Args:
        filename: The name of the json file.
    
    Returns:
        dict: A dictionary of labels, with their IDs as keys, and time as values.
    """
    with open(filename) as f:
        return json.load(f)