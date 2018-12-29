def indent(text, count=1, prefix="    "):
    lines = text.split("\n")
    return "\n".join("{}{}".format(prefix * count, line)
                     for line in lines)
