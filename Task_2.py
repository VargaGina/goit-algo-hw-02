from collections import deque

def is_palindrome(s):
    s = ''.join(s.lower().split())
    d = deque(s)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


if __name__ == "__main__":
    test = "No lemon, no melon"
    print(f"'{test}' is a palindrome: {is_palindrome(test)}")