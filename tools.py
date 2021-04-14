import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def safe_cast(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        sys.exit("sth wrong cast")