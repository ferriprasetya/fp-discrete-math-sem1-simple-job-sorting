def format_to_percent(number: float):
    """
    Convert a number to a percentage string.
    :param number: Number
    :return: Percentage string
    """
    return "{:.2f}".format(number * 100) + "%"
