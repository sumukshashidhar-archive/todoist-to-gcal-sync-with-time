def link_labels(todoist_labels, time_labels):
    """
    Link the time labels to the Todoist labels.
    """
    linked_dict = {}
    for label in todoist_labels:
        if label['name'] in time_labels:
            linked_dict[label['id']] = time_labels[label['name']]
    return linked_dict