"""
20. Valid Parentheses  (Easy)

Given a string containing only '(', ')', '{', '}', '[' and ']', determine if
the input is valid: every open bracket is closed by the same type, and brackets
close in the correct order (proper nesting).

Approach: stack. Push every opening bracket. On a closing bracket, the top of
the stack must be its matching opener — if the stack is empty or the top
doesn't match, the string is invalid. At the end the stack must be empty
(no unclosed openers).

Time:  O(n)
Space: O(n)   worst case all opening brackets
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("{[]}") is True
    assert Solution().isValid("]") is False
    assert Solution().isValid("(") is False
    print("ok")
