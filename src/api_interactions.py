from datetime import datetime

def get_all_labels(api_object):
    """
    Gets all the labels from Todoist.
    
    Args:
        api_object: A TodoistAPI object.
    
    Returns:
        A list of labels with id and name.
    """
    labels = api_object.get_labels()
    labels_filtered = []
    for label in labels:
        filtered_label = {
            'id': label.id,
            'name': label.name,
        }
        labels_filtered.append(filtered_label)
    return labels_filtered



def check_if_task_can_be_synced(task, lables_list):
    """
    Checks if a task can be synced to GCal.

    Args:
        task: A task object from Todoist.

    Returns:
        True if the task can be synced, False otherwise.
    """
    if task.due is not None and task.due.datetime is not None and len(task.label_ids) != 0:
        for label in task.label_ids:
            if label in lables_list:
                return True
    return False


def get_time_value(labels, labels_dict):
    """
    Gets the time value for a task.

    Args:
        labels: A list of labels for a task.
        labels_dict: A dictionary of labels, with their IDs as keys, and time as values.
    
    Returns:
        The time value for the task.
    """
    for label in labels:
        if label in labels_dict:
            return labels_dict[label]

def get_tasks_to_sync(api_object, labels_dict):
    """
    Fetches all the tasks from todoist, and decides which
    tasks can be synced to GCal, and returns them in a neat format
    that can be forwarded to our GCal event creation mechanism.

    Args:
        api_object: A TodoistAPI object.
        labels_dict: A dictionary of labels, with their IDs as keys, and time as values.

    Returns:
        A list of tasks that can be synced to GCal.
    """
    tasks = api_object.get_tasks() # Get all tasks from Todoist
    # iterate through all tasks
    syncable = [] # list of tasks that can be synced
    for task in tasks:
        if check_if_task_can_be_synced(task, labels_dict.keys()):
            # now we have a task that can be synced to GCal
            task_filtered = {
                'content': task.content,
                'url': task.url,
                'priority': task.priority,
                'time': get_time_value(task.label_ids, labels_dict),
                'due': datetime.fromisoformat(task.due.datetime),
            }
            syncable.append(task_filtered)
    return syncable
        
