def check_whitespace(lines):
    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno+1
        if "\t" in line:
            yield lno+1, "OMG TABS!!!1"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno+1, "trailing whitespace"

text = input()
check_whitespace(text)  