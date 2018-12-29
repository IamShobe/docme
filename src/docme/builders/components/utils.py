def indent(text, count=1, prefix="    "):
    """Indent the given text prefix times the count.

    Args:
        text (str): string to indent (line by line).
        count (number): number of indents.
        prefix (str): the prefix of the indent.

    Returns:
        str. the indented text.
    """
    lines = text.split("\n")
    return "\n".join("{}{}".format(prefix * count, line)
                     for line in lines)
