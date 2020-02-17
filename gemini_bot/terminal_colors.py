"""
Terminal coloring
"""

def warning(string):
    return f"\u001b[31;1m{string}\u001b[0m"

def success(string):
    return f"\u001b[32;1m{string}\u001b[0m"

def message(string):
    return f"\u001b[1m{string}\u001b[0m"
