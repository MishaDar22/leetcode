def foo(string: str) -> bool:
    """
    Check if brackets in the string are balanced.
    Returns True if brackets are balanced, False otherwise.
    """
    stack = []
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    for char in string:
        if char in brackets:  # Opening bracket
            stack.append(char)
        elif char in brackets.values():  # Closing bracket
            if not stack:  # Stack is empty but we found closing bracket
                return False
            if char != brackets[stack.pop()]:  # Mismatched bracket
                return False

    return len(stack) == 0  # True if all brackets are matched


some_str = '(jj(bf)chmf{ghmfhj}((((())))())[hngh]fghfm)'
foo(some_str)
