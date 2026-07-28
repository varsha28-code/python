----------------------------Backspace string compare-------------------
def process(s):
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return " ".join(stack)
s = input().strip()
t = input().strip()
print(process(s) == process(t))

--------------------------Valid parenthesis----------------------
def isValid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return "Invalid"
            stack.pop()
    return "Valid" if not stack else "Invalid"
s = input()
print(isValid(s))
