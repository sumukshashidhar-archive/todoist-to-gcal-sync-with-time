from todoist_api_python.api import TodoistAPI # Import the TodoistAPI class
from read_env_vars import get_todoist_api_key # to get env vars
from read_env_vars import read_time_labels # to get time labels
import api_interactions as controller
from utility import link_labels # to link labels
from gcal_controller import authorize # to authorize google calendar
from gcal_controller import gcal_whate

api = TodoistAPI(get_todoist_api_key()) # Create a TodoistAPI object
timelabels = read_time_labels() # Get the time labels

labels = controller.get_all_labels(api) # Get all labels from Todoist
linked_labels = link_labels(labels, timelabels) # Link the labels to the time labels

syncable = controller.get_tasks_to_sync(api, linked_labels) # Get the tasks that can be synced to GCal

gcal_creds = authorize() # Authorize Google Calendar and get credentials