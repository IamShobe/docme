import textwrap


def indent(text, count=1, prefix="    "):
    lines = text.split("\n")
    return "\n".join("{}{}".format(prefix * count, line)
                     for line in lines)


wrapper = textwrap.TextWrapper(width=700,
                               replace_whitespace=False,
                               drop_whitespace=False)

wrapper_indent = textwrap.TextWrapper(
    subsequent_indent="    ",
    width=700,
    replace_whitespace=False,
    drop_whitespace=False)
