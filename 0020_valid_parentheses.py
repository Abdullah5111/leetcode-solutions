"""
20. Valid Parentheses  (Easy)

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
