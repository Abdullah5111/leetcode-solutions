"""
58. Length of Last Word  (Easy)

Time:  O(n)
Space: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert Solution().lengthOfLastWord("luffy is still joyboy") == 6
    assert Solution().lengthOfLastWord("a") == 1
    assert Solution().lengthOfLastWord("word   ") == 4
    print("ok")
