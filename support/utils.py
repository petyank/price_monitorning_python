def get_percent_diff(old_value, new_value):
    """ Calculate the percentage difference between two values """
    if old_value == 0:
        raise ValueError("Old value cannot be 0")
    return ((new_value - old_value) / old_value) * 100