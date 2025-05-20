def is_palindrome(s):
    x = str(s)
    return True if x == x[::-1] else False
