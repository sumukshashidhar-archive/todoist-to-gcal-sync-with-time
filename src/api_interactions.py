def get_filtered_task_list(api_object):
    """
    """
    task_list = api_object.get_tasks()
    filtered_task_list = []
    for task in task_list:
        filtered = {
            'content': task.content,
            'priority': task.priority,
            'url': task.url,
            'due': task.due,
            'label_ids': task.label_ids,
        }
        filtered_task_list.append(filtered)
    return filtered_task_list