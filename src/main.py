from todoist_api_python.api import TodoistAPI # Import the TodoistAPI class
from read_env_vars import get_todoist_api_key # to get env vars
import api_interactions as controller
api = TodoistAPI(get_todoist_api_key()) # Create a TodoistAPI object

print(controller.get_filtered_task_list(api))